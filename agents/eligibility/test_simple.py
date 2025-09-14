# Simple test to verify the tool works
from eligibility.eligibility import eligibility_checker

# Test with proper data types
result = eligibility_checker({
    "age": 29,
    "income": 10000,
    "state": "Uttar Pradesh",
    "rural": True,
    "category": "Farmer"
})

print("Test result:")
print(result)