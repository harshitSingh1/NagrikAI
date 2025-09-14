from ibm_watsonx_orchestrate.agent_builder.tools import tool
import random

@tool
def track_status(application_id: str = "APP-0001") -> dict:
    """
    Returns mock status update for an application/grievance.
    In real implementation: integrate with UMANG/official portals.
    """
    statuses = [
        "Received by department",
        "Under review",
        "Approved",
        "Rejected - missing documents",
        "Disbursed/Resolved"
    ]
    update = {
        "application_id": application_id,
        "current_status": random.choice(statuses),
        "last_updated": "2025-09-06"
    }
    return update
