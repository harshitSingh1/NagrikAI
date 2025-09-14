from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool
def greeting() -> str:
    """Returns a greeting message"""
    return "Hello World from NagrikAI setup!"
