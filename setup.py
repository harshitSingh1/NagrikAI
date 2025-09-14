#!/usr/bin/env python3

import os
import subprocess
import sys

def run_command(command):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error: {e.stderr}")
        return None

def main():
    print("Setting up NagrikAI...")
    
    # Check if Python is installed
    python_version = run_command("python --version")
    if python_version:
        print(f"Python version: {python_version}")
    else:
        print("Python is not installed or not in PATH")
        sys.exit(1)
    
    # Create virtual environment
    print("Creating virtual environment...")
    if not os.path.exists(".venv"):
        run_command("python -m venv .venv")
        print("Virtual environment created.")
    else:
        print("Virtual environment already exists.")
    
    # Install requirements
    print("Installing dependencies...")
    if os.name == 'nt':  # Windows
        pip_cmd = ".venv\\Scripts\\pip install -r requirements.txt"
    else:  # Unix/Linux/Mac
        pip_cmd = ".venv/bin/pip install -r requirements.txt"
    
    result = run_command(pip_cmd)
    if result:
        print("Dependencies installed successfully.")
    else:
        print("Failed to install dependencies.")
        sys.exit(1)
    
    print("\nSetup completed successfully!")
    print("\nTo run the application:")
    if os.name == 'nt':  # Windows
        print("  .venv\\Scripts\\activate")
        print("  python app.py")
    else:  # Unix/Linux/Mac
        print("  source .venv/bin/activate")
        print("  python app.py")

if __name__ == "__main__":
    main()