from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_Transformation import DataTransformation
import sys

if __name__=="__main__":
    try:
        trainingPipelineConfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingPipelineConfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Intiate the data ingestion")
        dataingestionartifact = data_ingestion.intiate_data_ingestion()
        print("data ingestion is complete")
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(trainingPipelineConfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Intiate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data validation is complete")
        print(data_validation_artifact)
        data_transformation_config=DataTransformationConfig(trainingPipelineConfig)
        logging.info("data Transformation started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data Transformation completed")
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
        