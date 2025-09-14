# create_knowledge_data.py
import pandas as pd
import random

schemes = [
    "PM-KISAN", "Pradhan Mantri Awas Yojana", "Ayushman Bharat", "MGNREGA",
    "Beti Bachao Beti Padhao", "Mid-Day Meal", "Startup India", "Standup India"
]

categories = ["Agriculture", "Housing", "Healthcare", "Employment", "Women", "Education", "Business", "Finance"]
states = ["Uttar Pradesh", "Maharashtra", "Bihar", "Madhya Pradesh", "Rajasthan", "Tamil Nadu", "Karnataka", "West Bengal"]

rows = []
for i in range(120):
    rows.append({
        "scheme_name": random.choice(schemes),
        "category": random.choice(categories),
        "eligibility": random.choice(["Farmer", "Women", "Student", "Worker", "All Citizens"]),
        "state": random.choice(states),
        "benefit": random.choice([
            "Cash Transfer", "Subsidy", "Insurance Cover", "Scholarship", "Employment Guarantee", "Housing Support"
        ])
    })

df = pd.DataFrame(rows)
df.to_csv("data/knowledge_data.csv", index=False)
print("Knowledge dataset created at data/knowledge_data.csv")
