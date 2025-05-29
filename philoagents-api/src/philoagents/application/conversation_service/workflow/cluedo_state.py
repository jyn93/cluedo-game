from langgraph.graph import MessagesState


class SuspectState(MessagesState):
    """State class for the LangGraph workflow. It keeps track of the information necessary to maintain a coherent
    conversation between the Suspect and the user.

    Attributes:
        suspect_context (str): The historical and philosophical context of the suspect.
        suspect_name (str): The name of the suspect.
        suspect_perspective (str): The perspective of the suspect about AI.
        suspect_style (str): The style of the suspect.
        summary (str): A summary of the conversation. This is used to reduce the token usage of the model.
    """

    suspect_context: str
    suspect_name: str
    suspect_perspective: str
    suspect_style: str
    summary: str


def state_to_str(state: SuspectState) -> str:
    if "summary" in state and bool(state["summary"]):
        conversation = state["summary"]
    elif "messages" in state and bool(state["messages"]):
        conversation = state["messages"]
    else:
        conversation = ""

    return f"""
SuspectState(suspect_context={state["suspect_context"]}, 
suspect_name={state["suspect_name"]}, 
suspect_perspective={state["suspect_perspective"]}, 
suspect_style={state["suspect_style"]}, 
conversation={conversation})
        """


class CrimeCaseState(MessagesState):
    """State class for the LangGraph workflow. It keeps track of the information necessary to maintain a coherent
    conversation between the Suspect and the user.

    Attributes:
        crime_scene (str): The description of the crime scene.
        victim (str): The name of the victim.
        suspects (list): A list of suspects in the case.
        evidence (list): A list of evidence related to the case.
    """
    crime_scene: str
    victim: str
    suspects: list
    culprits: list
    inocent: list
    evidence: list

def crime_case_state_to_str(state: CrimeCaseState) -> str:
    return f"""
CrimeCaseState(crime_scene={state["crime_scene"]}, 
victim={state["victim"]}, 
suspects={state["suspects"]}, 
evidence={state["evidence"]})
    """