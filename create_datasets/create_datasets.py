import pandas as pd
import numpy as np
import random
from faker import Faker

# Initialize faker for realistic data
fake = Faker('en_IN')

# Create government schemes dataset
def create_schemes_dataset():
    schemes_data = []
    
    # Central government schemes
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
        }
    ]
    
    # State-specific schemes (examples)
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
        }
    ]
    
    schemes_data = central_schemes + state_schemes
    df = pd.DataFrame(schemes_data)
    df.to_csv("data/government_schemes.csv", index=False)
    print(f"Created government schemes dataset with {len(schemes_data)} schemes")

# Create citizen profiles dataset
def create_citizen_profiles():
    citizens = []
    
    states = ["Maharashtra", "Uttar Pradesh", "Bihar", "West Bengal", "Tamil Nadu", 
              "Kerala", "Karnataka", "Gujarat", "Rajasthan", "Punjab"]
    categories = ["Farmer", "Laborer", "Small Business", "Student", "Professional", 
                 "Homemaker", "Senior Citizen", "Unemployed"]
    
    for i in range(100):
        citizen = {
            "citizen_id": f"C{1000 + i}",
            "name": fake.name(),
            "age": random.randint(18, 80),
            "income": random.randint(50000, 500000),
            "state": random.choice(states),
            "area": random.choice(["Urban", "Rural"]),
            "category": random.choice(categories),
            "aadhaar_number": fake.aadhaar_id(),
            "phone_number": fake.phone_number()
        }
        citizens.append(citizen)
    
    df = pd.DataFrame(citizens)
    df.to_csv("data/citizen_profiles.csv", index=False)
    print(f"Created citizen profiles dataset with {len(citizens)} citizens")

# Create application tracking dataset
def create_applications_dataset():
    applications = []
    
    schemes = ["PMKISAN", "PMAY", "UJJWALA", "MH_FARM", "UP_SCHOLAR"]
    statuses = ["Submitted", "Under Review", "Approved", "Rejected", "Disbursed"]
    
    for i in range(200):
        application = {
            "application_id": f"APP{5000 + i}",
            "citizen_id": f"C{1000 + random.randint(0, 99)}",
            "scheme_id": random.choice(schemes),
            "application_date": fake.date_between(start_date='-1y', end_date='today'),
            "status": random.choice(statuses),
            "last_update": fake.date_between(start_date='-6m', end_date='today'),
            "officer_remarks": random.choice(["", "Documents pending", "Verification completed", "Eligibility confirmed"])
        }
        applications.append(application)
    
    df = pd.DataFrame(applications)
    df.to_csv("data/applications_tracking.csv", index=False)
    print(f"Created applications dataset with {len(applications)} applications")

if __name__ == "__main__":
    # Create data directory if it doesn't exist
    import os
    os.makedirs("data", exist_ok=True)
    
    create_schemes_dataset()
    create_citizen_profiles()
    create_applications_dataset()
    print("All datasets created successfully!")