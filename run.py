#!/usr/bin/env python3

import os
import sys
import subprocess

def main():
    # Check if virtual environment exists
    if not os.path.exists(".venv"):
        print("Virtual environment not found. Running setup...")
        subprocess.run([sys.executable, "setup.py"])
    
    # Activate virtual environment and run app
    if os.name == 'nt':  # Windows
        python_cmd = ".venv\\Scripts\\python"
    else:  # Unix/Linux/Mac
        python_cmd = ".venv/bin/python"
    
    os.system(f"{python_cmd} app.py")

if __name__ == "__main__":
    main()