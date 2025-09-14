from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool
def eligibility_checker(building_id: int, income: int, category: str) -> dict:
    """
    Check citizen eligibility in a simple way without dataset.
    Example call: eligibility_checker(1, 10000, "farmer")
    """
    # Example rule set
    if income < 300000 and category.lower() in ["farmer", "worker", "student"]:
        return {
            "eligible": True,
            "reason": f"Citizen qualifies under scheme for {category.lower()}s"
        }
    else:
        return {
            "eligible": False,
            "reason": "Does not meet eligibility criteria"
        }
