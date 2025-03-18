import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read the yaml file and return the ConfigBox object
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Reading the yaml file from the path: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("The yaml file is empty")
    except Exception as e:  
        logger.error(e)
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create directories from the list of directories
    """
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Creating directory: {path}")
        except Exception as e:
            logger.error(e)
            raise e
        
@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save the data in the json format
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
        logger.info(f"Saving the data in the json format at the path: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load the data from the json file
    Args:
    path : Path : Path to the json file
    Returns:
    ConfigBox : data as class attributes (ConfigBox object) instead of dict 
    """
    with open(path, "r") as json_file:
        data = json.load(json_file)
        logger.info(f"Loading the data from the json file at the path: {path}")
        return ConfigBox(data)
        
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save the data in the binary format
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Saving the data in the binary format at the path: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load the data from the binary file
    """
    data = joblib.load(filename=path)