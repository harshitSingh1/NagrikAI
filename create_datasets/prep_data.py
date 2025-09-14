import pandas as pd

# Load datasets
train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")
metadata = pd.read_csv("data/metadata.csv")

print("Train shape:", train.shape)
print("Test shape:", test.shape)
print("Metadata shape:", metadata.shape)

# Example: aggregate meter readings per building
agg = train.groupby("building_id")["meter_reading"].mean().reset_index()
agg.columns = ["building_id", "avg_meter_usage"]

# Merge with metadata
merged = metadata.merge(agg, on="building_id", how="left")
print(merged.head())

# Save for Eligibility Agent
merged.to_csv("data/eligibility_data.csv", index=False)
