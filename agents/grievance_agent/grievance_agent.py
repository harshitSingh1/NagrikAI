from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool
def file_grievance(complaint_text: str = "No complaint provided") -> dict:
    """
    Mock grievance classification & routing.
    In real implementation: Granite LLM + gov authority mapping.
    """
    # Simple keyword-based routing
    if "payment" in complaint_text.lower():
        dept = "Finance Department"
    elif "ration" in complaint_text.lower():
        dept = "Food & Supplies Department"
    elif "electricity" in complaint_text.lower():
        dept = "Energy Department"
    else:
        dept = "General Public Grievance Cell"

    ticket = {
        "complaint": complaint_text,
        "routed_to": dept,
        "ticket_id": "GREV-" + str(hash(complaint_text))[:6],
        "status": "Filed & under review"
    }
    return ticket
