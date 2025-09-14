# NagrikAI – An Agentic AI Copilot for Every Indian Citizen

NagrikAI is a sophisticated multi-agent AI copilot designed to bridge the gap between Indian citizens and government services. It transforms complex bureaucratic procedures into simple, guided interactions.

## Features

- **Eligibility Agent**: Checks eligibility for 700+ government schemes
- **Form Agent**: Auto-fills application forms using document data
- **Grievance Agent**: Files and tracks grievances with appropriate authorities
- **Tracking Agent**: Monitors application status and sends reminders
- **Knowledge Agent**: Answers queries about government schemes and services

## Tech Stack

- **Backend**: Flask, Python
- **Frontend**: HTML5, CSS3, JavaScript
- **AI Agents**: IBM Watsonx Orchestrate
- **Data**: Sample datasets for demonstration

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/NagrikAI.git
cd NagrikAI
```
2. Install dependencies:
```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows
.\.venv\Scripts\activate.ps1

# Activate on Mac/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
3. Set up environment variables
```bash
# Create a .env file with your Watsonx credentials
WO_DEVELOPER_EDITION_SOURCE=orchestrate
WO_INSTANCE=your_instance_url
WO_API_KEY=your_api_key
FLASK_ENV=development
FLASK_DEBUG=True
```
4. Download Kaggle datasets (optional)
```bash
# Install Kaggle CLI
pip install kaggle

# Set up Kaggle credentials (place kaggle.json in ~/.kaggle/)
kaggle competitions download -c track3-india-ai-impact-gen-ai-hackathon -p data

# Extract the files
unzip data/track3-india-ai-impact-gen-ai-hackathon.zip -d data/
```

4. Run the application:
```bash
python app.py
```