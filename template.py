import os
from pathlib import Path
import logging

logging.basicConfig(format="[ %(asctime)s ] : %(message)s",level=logging.INFO)
#for logging the logs generated during runtime

project_name = "textSummariser"

#.github- we will be using this during CI/CD deployment using the yaml file; whenever we will commit
#our code to github, this file will automatically deploy this in cloud.
#.gitkeep-hidden file which makes sure we don't upload an empty file to Github, to be 
#deleted later on.
#__init__.py - converts the folder into a local package which allows us to import 
#functionalities of one folder/file to another.
#common.py- this will contain all the utilities

#We create the src folder so that we will be able to import all the files from the src folder

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",#creating constructor file for creating the package 
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",   
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml", #will contain all the model params
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

#Code for looping through the list of files and creating them

for filepath in list_of_files:
    filepath = Path(filepath)   #Path detects the OS and automatically assigns the correct path format
    filedir, filename = os.path.split(filepath)
    #Check if filedir not empty
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for the file {filename}")

    #Creating the file inside the created dir
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file : {filepath}")
    
    else:
        logging.info(f"{filepath} already exists!")
