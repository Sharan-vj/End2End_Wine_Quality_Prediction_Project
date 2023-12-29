# Import
import os
from pathlib import Path
import logging

# Logging Information
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Module Configuration
project_name = str(input('Enter your project module name: '))
file_list = [
    # GitHub Meta Folder
    ".github/workflows/.gitkeep",

    # Project Module
    f"module/{project_name}/__init__.py",
    f"module/{project_name}/components/__init__.py",
    f"module/{project_name}/utils/__init__.py",
    f"module/{project_name}/utils/common.py",
    f"module/{project_name}/config/__init__.py",
    f"module/{project_name}/config/configuration.py",
    f"module/{project_name}/pipeline/__init__.py",
    f"module/{project_name}/entity/__init__.py",
    f"module/{project_name}/entity/config_entity.py",
    f"module/{project_name}/constant/__init__.py",

    # Other related files
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "schema.yaml",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "main.py",
    "other/trial.ipynb",
    "Template/index.html"
]

# Module Building 
for filepath in file_list:

    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f"{filename} is already created")
