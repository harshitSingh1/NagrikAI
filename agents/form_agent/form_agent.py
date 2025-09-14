from ibm_watsonx_orchestrate.agent_builder.tools import tool

# Mock OCR parser for demo
@tool
def auto_fill_form(citizen_name: str = "Unknown", aadhaar: str = "XXXXXXXXXXXX", income: int = 0) -> dict:
    """
    Auto-fills government scheme form using mock OCR/document parsing.
    In real implementation, replace with LayoutLMv3 + DigiLocker integration.
    """
    form = {
        "citizen_name": citizen_name,
        "aadhaar": aadhaar,
        "income": income,
        "status": "Form auto-filled successfully"
    }
    return form
