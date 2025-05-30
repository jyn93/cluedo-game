from langgraph.graph import MessagesState


class SuspectState(MessagesState):
    """State class for the LangGraph workflow. It keeps track of the information necessary to maintain a coherent
    conversation between the Suspect and the user.

    Attributes:
        case_description (str): A description of the crime case.
        summary_case (str): A summary of the crime case.
        crime_scene (str): The description of the crime scene.
        victim (str): The name of the victim.
        weapon (str): The weapon used in the crime.
        location (str): The location where the crime happened.
        culprit (str): The name of the culprit.
        suspect_context (str): The historical and philosophical context of the suspect.
        suspect_name (str): The name of the suspect.
        suspect_perspective (str): The perspective of the suspect about AI.
        suspect_style (str): The style of the suspect.
        summary (str): A summary of the conversation. This is used to reduce the token usage of the model.
    """
    case_description: str = ""
    summary_case: str = ""
    crime_scene: str = ""
    victim: str = ""
    weapon: str = ""
    location: str = ""
    culprit: str = ""

    selected_suspect_id: str = None
    suspect_context: str = ""
    suspect_name: str = ""
    suspect_perspective: str = ""
    suspect_style: str = ""
    summary: str = ""


def state_to_str(state: SuspectState) -> str:
    if "summary" in state and bool(state["summary"]):
        conversation = state["summary"]
    elif "messages" in state and bool(state["messages"]):
        conversation = state["messages"]
    else:
        conversation = ""

    return f"""
SuspectState(case_description={state["case_description"]},
summary_case={state["summary_case"]}, 
crime_scene={state["crime_scene"]}, 
victim={state["victim"]},
weapon={state["weapon"]},
location={state["location"]}, 
culprit={state["culprit"]}, 
selected_suspect_id={state["selected_suspect_id"]},
suspect_context={state["suspect_context"]}, 
suspect_name={state["suspect_name"]}, 
suspect_perspective={state["suspect_perspective"]}, 
suspect_style={state["suspect_style"]}, 
conversation={conversation})
        """
