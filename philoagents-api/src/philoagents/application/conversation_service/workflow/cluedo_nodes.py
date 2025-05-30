import json
from langchain_core.messages import RemoveMessage
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt import ToolNode

from philoagents.application.conversation_service.workflow.cluedo_chains import (
    # get_context_summary_chain,
    # get_conversation_summary_chain,
    get_crime_case_chain,
    get_suspect_response_chain,
)
from philoagents.application.conversation_service.workflow.cluedo_state import (
    SuspectState
)
from philoagents.application.conversation_service.workflow.tools import tools
from philoagents.config import settings
from philoagents.domain.suspect_factory import SuspectFactory

retriever_node = ToolNode(tools)


async def crime_case_node(state: SuspectState, config: RunnableConfig):
    suspect_list = [
        SuspectFactory.get_suspect(sid).__str__()
        for sid in SuspectFactory.get_available_suspects()
    ]
    crime_case_chain = get_crime_case_chain()

    crime_case = await crime_case_chain.ainvoke(
        {
            "suspect_list": suspect_list,
        },
        config,
    )
    state["case_description"] = crime_case.case_description
    state["summary_case"] = crime_case.summary_case
    state["weapon"] = crime_case.weapon
    state["location"] = crime_case.location
    state["crime_scene"] = crime_case.crime_scene
    state["victim"] = crime_case.victim
    state["culprit"] = crime_case.culprit
    return crime_case

async def select_suspect_node(state: SuspectState):
    """
    Select a suspect from the available suspects and set the state with the suspect's context, name, perspective, and style.
    This function lists all available suspects, prompts the user to select one, and updates the state accordingly.
    Args:
        state (SuspectState): The current state of the conversation.
    Returns:
        SuspectState: The updated state with the selected suspect's information.
    Raises:
        ValueError: If the selected suspect ID is not valid.
    """
    suspects = [SuspectFactory.get_suspect(sid) for sid in SuspectFactory.get_available_suspects()]
    suspect_list = "\n".join(
        f"- {suspect.id}: {suspect.name}" for suspect in suspects
    )
    print (f"Available suspects:\n{suspect_list}")
    # Ask the user to select a suspect
    selected_suspect_id = input("Please enter the ID of the suspect you want to talk to: ")
    if selected_suspect_id not in [suspect.id for suspect in suspects]:
        raise ValueError(f"Invalid suspect ID: {selected_suspect_id}. Available IDs are: {[suspect.id for suspect in suspects]}")

    state["selected_suspect_id"] = selected_suspect_id
    suspect = SuspectFactory.get_suspect(selected_suspect_id)
    print(f"You have selected: {suspect.name} ({suspect.id})")
    state["suspect_name"] = suspect.name
    state["suspect_perspective"] = suspect.perspective
    state["suspect_style"] = suspect.style
    return state

async def conversation_node(state: SuspectState, config: RunnableConfig):
    summary = state.get("summary", "")
    conversation_chain = get_suspect_response_chain()

    response = await conversation_chain.ainvoke(
        {
            "messages": state["messages"],
            "suspect_name": state["suspect_name"],
            "suspect_perspective": state["suspect_perspective"],
            "suspect_style": state["suspect_style"],
            "summary": summary,
            "case_description": state["case_description"],
            "crime_scene": state["crime_scene"],
        },
        config,
    )
    
    return {"messages": response}


# async def summarize_conversation_node(state: SuspectState):
#     summary = state.get("summary", "")
#     summary_chain = get_conversation_summary_chain(summary)

#     response = await summary_chain.ainvoke(
#         {
#             "messages": state["messages"],
#             "suspect_name": state["suspect_name"],
#             "summary": summary,
#         }
#     )

#     delete_messages = [
#         RemoveMessage(id=m.id)
#         for m in state["messages"][: -settings.TOTAL_MESSAGES_AFTER_SUMMARY]
#     ]
#     return {"summary": response.content, "messages": delete_messages}


# async def summarize_context_node(state: SuspectState):
#     context_summary_chain = get_context_summary_chain()

#     response = await context_summary_chain.ainvoke(
#         {
#             "context": state["messages"][-1].content,
#         }
#     )
#     state["messages"][-1].content = response.content

#     return {}


# async def connector_node(state: SuspectState):
#     return {}