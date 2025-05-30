import asyncio
import logging

from philoagents.application.conversation_service.workflow.cluedo_graph import create_workflow_graph
from philoagents.domain.suspect_factory import SuspectFactory

# Optional: Configure logging for more detailed output
# logging.basicConfig(level=logging.DEBUG)

async def main():
    # Create the workflow graph
    graph_builder = create_workflow_graph()
    graph = graph_builder.compile()

    # Prepare initial state
    suspects = [SuspectFactory.get_suspect(sid) for sid in SuspectFactory.get_available_suspects()]
    suspect_list = "\n".join(f"- {suspect.id}: {suspect.name}" for suspect in suspects)
    initial_state = {
        "messages": [],
        "suspect_list": suspect_list,
        # Add other required initial state keys if needed
    }

    print("[DEBUG] Initial state:", initial_state)

    # Run the workflow graph
    try:
        output_state = await graph.ainvoke(input=initial_state)
        print("[DEBUG] Final output state:", output_state)
    except Exception as e:
        print(f"[ERROR] Exception during workflow execution: {e}")

if __name__ == "__main__":
    asyncio.run(main())