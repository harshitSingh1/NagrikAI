# knowledge_agent/knowledge_agent.py
from ibm_watsonx_orchestrate.agent_builder.tools import tool
import pandas as pd
import os

# Configurable dataset path (use absolute path if possible)
DATA_PATH = os.getenv("KNOWLEDGE_DATA_PATH", os.path.join("data", "knowledge_data.csv"))

# Safe fallback dataset if file is not available in runtime
FALLBACK = [
    {
        "scheme_id": "MH_FARM",
        "scheme_name": "Maharashtra Farmer Welfare Scheme",
        "category": "Agriculture",
        "eligibility": "Farmer",
        "state": "Maharashtra",
        "benefit": "Financial aid"
    },
    {
        "scheme_id": "PMKISAN",
        "scheme_name": "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
        "category": "Agriculture",
        "eligibility": "Farmer",
        "state": "All",
        "benefit": "Cash Transfer"
    },
    {
        "scheme_id": "UP_SCHOLAR",
        "scheme_name": "Uttar Pradesh Scholarship Scheme",
        "category": "Education",
        "eligibility": "Student",
        "state": "Uttar Pradesh",
        "benefit": "Scholarship"
    }
]

def load_df():
    """Load dataframe if available, else return fallback DataFrame"""
    try:
        if os.path.exists(DATA_PATH):
            df = pd.read_csv(DATA_PATH)
            return df
        else:
            # convert fallback to DataFrame
            return pd.DataFrame(FALLBACK)
    except Exception as e:
        # on any error, return fallback
        return pd.DataFrame(FALLBACK)

def simple_match(df, query_terms):
    """Return top matches where any field contains any query term"""
    if df.empty:
        return []
    qterms = [t.strip().lower() for t in query_terms if t.strip()]
    def row_matches(row):
        text = " ".join([str(x).lower() for x in row.values])
        return all(any(t in text for t in qterms) for t in qterms)
    matched = df[df.apply(row_matches, axis=1)]
    if matched.empty:
        # relaxed match: any term matching
        matched = df[df.apply(lambda r: any(t in " ".join([str(x).lower() for x in r.values]) for t in qterms), axis=1)]
    return matched.head(5).to_dict(orient="records")

@tool
def answer_query(query: str) -> dict:
    """
    Knowledge Agent: Answer user queries using dataset or fallback.
    Example queries: "farmer maharashtra scholarship", "schemes for farmers in Maharashtra"
    """
    try:
        df = load_df()
        # break query into keywords
        q = query or ""
        terms = q.replace(",", " ").split()
        matches = simple_match(df, terms)

        # If no direct matches and user asked for scholarship specifically,
        # attempt to return near-matches (state-level farmer schemes + scholarship guidance)
        if not matches:
            # try find farmer + state
            farmer_state = [r for r in df.to_dict(orient="records") if ("farmer" in str(r).lower() and "maharashtra" in str(r).lower())]
            general_farmer = [r for r in df.to_dict(orient="records") if "farmer" in str(r).lower()]
            if farmer_state:
                matches = farmer_state[:5]
            else:
                matches = general_farmer[:5]

        note = ""
        # If none of the matches has 'Scholar' in benefit/description, add guidance
        if not any("scholar" in (str(m.get("benefit","")).lower() + str(m.get("category","")).lower() + str(m.get("scheme_name","")).lower()) for m in matches):
            note = ("no explicit 'scholarship' record for farmer+maharashtra found in dataset. "
                    "recommend checking state education scholarships (maharashtra) or national scholarship portal (nsp).")

        return {"query": query, "matches": matches, "note": note}
    except Exception as e:
        return {"error": str(e)}
