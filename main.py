from cnnClassifier import logger
import os
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


logger.info("Welcome to cnnClassifier")

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

CONFIG_FILE_PATH = os.path.join(os.getcwd(), "config", "config.yaml")
PARAMS_FILE_PATH = os.path.join(os.getcwd(), "params.yaml")

def read_yaml(path_to_yaml):
    """
    Reads a YAML file and returns its content.
    """
    try:
        logger.info(f"Attempting to read YAML file at: {os.path.abspath(path_to_yaml)}")
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return content
    except FileNotFoundError as e:
        logger.error(f"YAML file not found: {path_to_yaml}")
        raise e
    except Exception as e:
        raise e