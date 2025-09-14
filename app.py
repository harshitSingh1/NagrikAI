from flask import Flask, render_template, request, jsonify, session
import os
import json
from datetime import datetime
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET', 'nagrikai-secret-key-2024')

# Government schemes database
GOVERNMENT_SCHEMES = [
    {
        "id": "PMKISAN",
        "name": "Pradhan Mantri Kisan Samman Nidhi",
        "category": "Agriculture",
        "min_income": 0,
        "max_income": 150000,
        "min_age": 18,
        "max_age": 100,
        "states": ["All"],
        "rural_only": True,
        "occupations": ["Farmer"]
    },
    {
        "id": "PMAY",
        "name": "Pradhan Mantri Awas Yojana",
        "category": "Housing",
        "min_income": 0,
        "max_income": 300000,
        "min_age": 21,
        "max_age": 70,
        "states": ["All"],
        "rural_only": False,
        "occupations": ["All"]
    },
    {
        "id": "UJJWALA",
        "name": "Pradhan Mantri Ujjwala Yojana",
        "category": "Petroleum",
        "min_income": 0,
        "max_income": 150000,
        "min_age": 18,
        "max_age": 100,
        "states": ["All"],
        "rural_only": False,
        "occupations": ["Women", "BPL"]
    },
    {
        "id": "MH_FARM",
        "name": "Maharashtra Farmer Welfare Scheme",
        "category": "Agriculture",
        "min_income": 0,
        "max_income": 200000,
        "min_age": 21,
        "max_age": 65,
        "states": ["Maharashtra"],
        "rural_only": True,
        "occupations": ["Farmer"]
    },
    {
        "id": "UP_SCHOLAR",
        "name": "Uttar Pradesh Scholarship Scheme",
        "category": "Education",
        "min_income": 0,
        "max_income": 250000,
        "min_age": 15,
        "max_age": 25,
        "states": ["Uttar Pradesh"],
        "rural_only": False,
        "occupations": ["Student", "SC/ST"]
    }
]

# Simulated agent responses
def simulate_eligibility_agent(profile):
    """Simulate eligibility agent response"""
    eligible_schemes = []
    
    for scheme in GOVERNMENT_SCHEMES:
        # Check age eligibility
        if profile['age'] < scheme['min_age'] or profile['age'] > scheme['max_age']:
            continue
            
        # Check income eligibility
        if profile['income'] < scheme['min_income'] or profile['income'] > scheme['max_income']:
            continue
            
        # Check state eligibility
        if scheme['states'] != ["All"] and profile['state'] not in scheme['states']:
            continue
            
        # Check rural/urban eligibility
        if scheme['rural_only'] and not profile['rural']:
            continue
            
        # Check occupation eligibility
        if scheme['occupations'] != ["All"] and profile['category'] not in scheme['occupations']:
            continue
            
        eligible_schemes.append({
            "scheme_name": scheme['name'],
            "category": scheme['category']
        })
    
    return {
        "eligible": len(eligible_schemes) > 0,
        "eligible_schemes": eligible_schemes,
        "message": f"Found {len(eligible_schemes)} eligible schemes" if eligible_schemes else "No eligible schemes found"
    }

def simulate_form_agent(form_data):
    """Simulate form agent response"""
    return {
        "success": True,
        "application_id": f"APP-{datetime.now().strftime('%Y%m%d')}-{random.randint(1000, 9999)}",
        "message": "Application submitted successfully! You will receive updates via SMS."
    }

def simulate_grievance_agent(grievance_data):
    """Simulate grievance agent response"""
    departments = {
        "Payment Issues": "Finance Department",
        "Application Delays": "Processing Department",
        "Service Quality": "Quality Assurance Department",
        "Corruption": "Vigilance Department",
        "Other": "General Grievance Cell"
    }
    
    department = departments.get(grievance_data['category'], "General Grievance Cell")
    
    return {
        "success": True,
        "ticket_id": f"GRV-{datetime.now().strftime('%Y%m%d')}-{random.randint(1000, 9999)}",
        "department": department,
        "message": "Grievance filed successfully. You will receive updates within 48 hours."
    }

def simulate_tracking_agent(tracking_data):
    """Simulate tracking agent response"""
    statuses = [
        "Application Received",
        "Under Review",
        "Documents Verified",
        "Approval Pending",
        "Approved - Funds Disbursed"
    ]
    
    # Generate a deterministic status based on the tracking ID
    status_index = hash(tracking_data.get('application_id', '')) % 5
    
    return {
        "application_id": tracking_data.get('application_id', 'UNKNOWN'),
        "status": statuses[status_index],
        "last_updated": datetime.now().strftime('%d-%m-%Y %H:%M'),
        "estimated_completion": "15-20 working days"
    }

def simulate_knowledge_agent(query):
    """Simulate knowledge agent response"""
    query_lower = query.lower()
    
    if 'farmer' in query_lower and 'maharashtra' in query_lower:
        return {
            "title": "Schemes for Farmers in Maharashtra",
            "content": """
            <p>Based on your query, here are some relevant schemes for farmers in Maharashtra:</p>
            <ul>
                <li><strong>Maharashtra Farmer Welfare Scheme</strong> - Financial assistance to farmers in Maharashtra</li>
                <li><strong>PM-KISAN</strong> - Income support to all landholding farmers</li>
                <li><strong>Crop Insurance Scheme</strong> - Protection against crop failure</li>
                <li><strong>Soil Health Card Scheme</strong> - Helps farmers monitor soil health</li>
            </ul>
            <p>You can check your eligibility for these schemes using the Eligibility tab.</p>
            """
        }
    elif 'student' in query_lower:
        return {
            "title": "Educational Schemes",
            "content": """
            <p>Based on your query, here are some relevant schemes for students:</p>
            <ul>
                <li><strong>National Scholarship Portal</strong> - Scholarships for various categories of students</li>
                <li><strong>Mid-Day Meal Scheme</strong> - Nutritious meals in government schools</li>
                <li><strong>Beti Bachao Beti Padhao</strong> - Scheme for girl child education</li>
                <li><strong>Pre-Matric Scholarship for Minorities</strong> - Financial support for minority students</li>
            </ul>
            """
        }
    elif 'housing' in query_lower or 'awas' in query_lower:
        return {
            "title": "Housing Schemes",
            "content": """
            <p>Based on your query, here are some relevant housing schemes:</p>
            <ul>
                <li><strong>Pradhan Mantri Awas Yojana (PMAY)</strong> - Housing for all by 2022</li>
                <li><strong>Rajiv Awas Yojana</strong> - Slum rehabilitation and affordable housing</li>
                <li><strong>State Housing Schemes</strong> - Various state-specific housing programs</li>
            </ul>
            """
        }
    else:
        return {
            "title": "Government Schemes Information",
            "content": """
            <p>India offers over 700 central and state government schemes across various categories including:</p>
            <ul>
                <li><strong>Agriculture</strong> - PM-KISAN, Crop Insurance, etc.</li>
                <li><strong>Housing</strong> - Pradhan Mantri Awas Yojana</li>
                <li><strong>Health</strong> - Ayushman Bharat, PM-JAY</li>
                <li><strong>Education</strong> - Scholarship schemes, Mid-Day Meal</li>
                <li><strong>Social Welfare</strong> - Pension schemes, disability benefits</li>
            </ul>
            <p>Please be more specific with your query for detailed information about a particular scheme.</p>
            """
        }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_eligibility', methods=['POST'])
def check_eligibility():
    try:
        data = request.json
        citizen_profile = {
            "age": int(data.get('age', 0)),
            "income": int(data.get('income', 0)),
            "state": data.get('state', ''),
            "rural": data.get('rural', 'urban') == 'rural',
            "category": data.get('category', '')
        }
        
        # Simulate eligibility agent response
        result = simulate_eligibility_agent(citizen_profile)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            "eligible": False,
            "message": f"Error checking eligibility: {str(e)}",
            "eligible_schemes": []
        }), 500

@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        data = request.json
        
        # Simulate form agent response
        result = simulate_form_agent(data)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error submitting form: {str(e)}"
        }), 500

@app.route('/file_grievance', methods=['POST'])
def file_grievance():
    try:
        data = request.json
        
        # Simulate grievance agent response
        result = simulate_grievance_agent(data)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error filing grievance: {str(e)}"
        }), 500

@app.route('/check_status', methods=['POST'])
def check_status():
    try:
        data = request.json
        
        # Simulate tracking agent response
        result = simulate_tracking_agent(data)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error checking status: {str(e)}"
        }), 500

@app.route('/knowledge_query', methods=['POST'])
def knowledge_query():
    try:
        data = request.json
        query = data.get('query', '')
        
        # Simulate knowledge agent response
        result = simulate_knowledge_agent(query)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "title": "Error",
            "content": f"Error processing query: {str(e)}"
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')