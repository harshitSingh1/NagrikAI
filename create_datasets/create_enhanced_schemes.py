import pandas as pd
import random

# Create a more comprehensive government schemes dataset
def create_enhanced_schemes():
    schemes = []
    
    # Central Government Schemes
    central_schemes = [
        {
            "scheme_id": "PMKISAN",
            "scheme_name": "Pradhan Mantri Kisan Samman Nidhi",
            "department": "Agriculture",
            "level": "Central",
            "min_age": 18,
            "max_age": 100,
            "min_income": 0,
            "max_income": 150000,
            "rural_only": True,
            "categories": ["Farmer"],
            "states": "All",
            "description": "Financial assistance to small and marginal farmers"
        },
        {
            "scheme_id": "PMAY",
            "scheme_name": "Pradhan Mantri Awas Yojana",
            "department": "Housing",
            "level": "Central",
            "min_age": 21,
            "max_age": 70,
            "min_income": 0,
            "max_income": 300000,
            "rural_only": False,
            "categories": ["All"],
            "states": "All",
            "description": "Housing for all by 2022"
        },
        {
            "scheme_id": "UJJWALA",
            "scheme_name": "Pradhan Mantri Ujjwala Yojana",
            "department": "Petroleum",
            "level": "Central",
            "min_age": 18,
            "max_age": 100,
            "min_income": 0,
            "max_income": 150000,
            "rural_only": False,
            "categories": ["Women", "BPL"],
            "states": "All",
            "description": "Free LPG connections to women from BPL households"
        },
        {
            "scheme_id": "PMJAY",
            "scheme_name": "Ayushman Bharat Pradhan Mantri Jan Arogya Yojana",
            "department": "Health",
            "level": "Central",
            "min_age": 0,
            "max_age": 100,
            "min_income": 0,
            "max_income": 500000,
            "rural_only": False,
            "categories": ["BPL"],
            "states": "All",
            "description": "Health insurance for economically vulnerable families"
        }
    ]
    
    # State-specific schemes
    state_schemes = [
        {
            "scheme_id": "MH_FARM",
            "scheme_name": "Maharashtra Farmer Welfare Scheme",
            "department": "Agriculture",
            "level": "State",
            "min_age": 21,
            "max_age": 65,
            "min_income": 0,
            "max_income": 200000,
            "rural_only": True,
            "categories": ["Farmer"],
            "states": "Maharashtra",
            "description": "Financial aid to farmers in Maharashtra"
        },
        {
            "scheme_id": "UP_SCHOLAR",
            "scheme_name": "Uttar Pradesh Scholarship Scheme",
            "department": "Education",
            "level": "State",
            "min_age": 15,
            "max_age": 25,
            "min_income": 0,
            "max_income": 250000,
            "rural_only": False,
            "categories": ["Student", "SC/ST"],
            "states": "Uttar Pradesh",
            "description": "Scholarship for SC/ST students in UP"
        },
        {
            "scheme_id": "KL_OLDAGE",
            "scheme_name": "Kerala Old Age Pension",
            "department": "Social Welfare",
            "level": "State",
            "min_age": 60,
            "max_age": 100,
            "min_income": 0,
            "max_income": 100000,
            "rural_only": False,
            "categories": ["Senior Citizen"],
            "states": "Kerala",
            "description": "Monthly pension for senior citizens in Kerala"
        }
    ]
    
    schemes_data = central_schemes + state_schemes
    df = pd.DataFrame(schemes_data)
    df.to_csv("data/government_schemes_enhanced.csv", index=False)
    print(f"Created enhanced government schemes dataset with {len(schemes_data)} schemes")

if __name__ == "__main__":
    create_enhanced_schemes()