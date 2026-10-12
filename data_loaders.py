
from pathlib import Path

import logging
import pandas as pd
import json
import yaml

# Do not call logging.basicConfig() here.
# Use the logging configuration from Part 1.
logger = logging.getLogger(__name__)


def load_csv(filepath):
    """Load a CSV file into a DataFrame.
    filepath is a Path object.
    """
    df = pd.read_csv(filepath)
    logger.info(f"Loaded CSV file: {filepath} ({len(df)} rows)")
    return df
    pass
    


def load_json(filepath):
    """Load a JSON file into a Python object (dict or list).
    filepath is a Path object.
    """
    with open (filepath, "r") as file:
        json_file = json.load(file)
    logger.info(f"Loaded JSON file: {filepath}")
    return json_fil
    pass
    


def load_yaml(filepath):
    """Load a YAML file into a Python object.
    filepath is a Path object.
    """
    with open (filepath, "r") as file:
        yaml_file = yaml.safe_load(file)
    logger.info(f"Loaded YAML file: {filepath}")
    return yaml_file
    pass
    


def load_data(filepath):
    """Load a file based on its extension.
    filepath is a string, such as 'fixtures/sample.csv'
    """
    path = Path(filepath)
    file_type = path.suffix.lower()
    if file_type == ".csv":
        loaded_csv = load_csv(path)
        return loaded_csv
    elif file_type == ".json":
        loaded_json = load_json(path)
        return loaded_json
    elif file_type == ".yaml":
        loaded_yaml = load_yaml(path)
        return loaded_yaml
    else:
        logger.error(f"Unsupported file format: {file_type}")
        raise ValueError(f"Unsupported file format: {file_type}")
    pass

    
