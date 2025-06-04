from functools import lru_cache

from langgraph.graph import END, START, StateGraph
# from langgraph.prebuilt import tools_condition

# from philoagents.application.conversation_service.workflow.edges import (
#     should_summarize_conversation,
# )
from philoagents.application.conversation_service.workflow.cluedo_nodes import (
    conversation_node,
    crime_case_node,
    select_suspect_node,
    get_question_node,
    get_decision_continue_conversation_node,
    get_decision_select_or_exit_node
)
from philoagents.application.conversation_service.workflow.cluedo_state import SuspectState


def decision_conversation(state: SuspectState):
    return state["decision_conversation"]

def decision_exit(state: SuspectState):
    return state["decision_exit"]

@lru_cache(maxsize=1)
def create_workflow_graph():
    graph_builder = StateGraph(SuspectState)

    # Add all nodes
    graph_builder.add_node("crime_case_node", crime_case_node)
    graph_builder.add_node("select_suspect_node", select_suspect_node)
    graph_builder.add_node("get_question_node", get_question_node)
    graph_builder.add_node("conversation_node", conversation_node)
    graph_builder.add_node("get_decision_continue_conversation_node", get_decision_continue_conversation_node)
    graph_builder.add_node("get_decision_select_or_exit_node", get_decision_select_or_exit_node)
    
    # Define the flow
    graph_builder.add_edge(START, "crime_case_node")
    graph_builder.add_edge("crime_case_node", "select_suspect_node")
    graph_builder.add_edge("select_suspect_node", "get_question_node")
    graph_builder.add_edge("get_question_node", "conversation_node")
    graph_builder.add_edge("conversation_node", "get_decision_continue_conversation_node")
    graph_builder.add_conditional_edges(
        "get_decision_continue_conversation_node",
        decision_conversation,
        {
            "yes": "get_question_node",
            "no": "get_decision_select_or_exit_node"
        }
    )
    graph_builder.add_conditional_edges(
        "get_decision_select_or_exit_node",
        decision_exit,
        {
            "select": "select_suspect_node",
            "exit": END
        }
    )
    
    return graph_builder

# Compiled without a checkpointer. Used for LangGraph Studio
graph = create_workflow_graph().compile()
