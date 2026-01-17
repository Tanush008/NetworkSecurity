import os
import sys
import numpy as np
import pandas as pd

"""defining the common const variable for trainging pipeline"""
TARGET_COLUMN = "Result"
PIPELINE_NAME :str= "NetworkSecurity"
ARTIFACT_DIR :str= "Artifacts"
FILE_NAME:str = "phisingData.csv"

TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")

""""data ingestion related const start with Data ingestion name"""

DATA_INGESTION_COLLECTION_NAME :str= "NetworkData"
DATA_INGESTION_DATABASE_NAME :str= "SecurityDB"
DATA_INGESTION_DIR_NAME :str = "data_ingestion"
DATA_INGESTION_FEATURES_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR :str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT:float = 0.2

""" data validation related const start with data valid name"""
DATA_VALIDATION_DIR_NAME :str= "data_validation"
DATA_VALIDATION_VALID_DIR_NAME :str= "validation"
DATA_VALIDATION_INVALID_DIR_NAME :str = "invalidation"
DATA_VALIDATION_DRIFT_REPORT_DIR:str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_NAME :str = "report.yaml"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"


"""data trnsformation related const start with trans name"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

## kkn imputer to replace nan values
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}
DATA_TRANSFORMATION_TRAIN_FILE_PATH: str = "train.npy"

DATA_TRANSFORMATION_TEST_FILE_PATH: str = "test.npy"
