#!/usr/bin/env python3
"""
Clean Jupyter notebooks by removing execution metadata and outputs
"""
import json
import sys
from pathlib import Path

def clean_notebook(notebook_path):
    """Clean a single notebook file"""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Clean each cell
    for cell in notebook.get('cells', []):
        # Remove execution count
        if 'execution_count' in cell:
            cell['execution_count'] = None
        
        # Remove outputs
        if 'outputs' in cell:
            cell['outputs'] = []
        
        # Remove metadata execution info
        if 'metadata' in cell:
            cell['metadata'].pop('execution', None)
    
    # Clean notebook metadata
    if 'metadata' in notebook:
        if 'kernelspec' in notebook['metadata']:
            notebook['metadata']['kernelspec'].pop('display_name', None)
        notebook['metadata'].pop('execution', None)
    
    # Write cleaned notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print(f"✅ Cleaned: {notebook_path}")

def main():
    """Clean all notebooks in current directory"""
    notebooks = [
        "01-create-private-vpc.ipynb",
        "02-deploy-production-agent.ipynb", 
        "99-cleanup.ipynb"
    ]
    
    for notebook in notebooks:
        if Path(notebook).exists():
            clean_notebook(notebook)
        else:
            print(f"⚠️  Not found: {notebook}")
    
    print("\n🎉 All notebooks cleaned!")

if __name__ == "__main__":
    main()
