import os
from pathlib import Path
import logging
list_of_files = [
   ".github/workflows/.gitkeep",
   "src/__init__",
   "src/components/data_ingestion.py",
   "src/components/data_transformation.py",
   "src/components/model_trainer.py",
   "src/components/model_evaluation.py",
   "src/pipeline/training_pipeline.py",
   "src/pipeline/prediction_pipeline.py",
   "src/utils/utils.py",
   "src/logger/logging.py",
   "src/exception/exception.py"
   "tests/unit/__init__.py",
   "tests/integration/__init.py",
   "init_setup.sh",
   "requirements.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "experiments/experiments.ipynb",
]

for file in list_of_files:
    file_path=Path(file)
    filedir,filename=os.path.split(file_path)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file :{filename}")
    if (not os.path.exists(file_path) ) or (os.path.getsize(file_path)==0):    
        with open(file_path,"w") as f:
            pass
        
    