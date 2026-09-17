import os
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.constants import CONFIG_FILE_PATH

def test_config_manager():
    config_mgr = ConfigurationManager()
    ingestion_config = config_mgr.get_data_ingestion_config()
    assert ingestion_config is not None
    assert os.path.exists(CONFIG_FILE_PATH)

def test_data_validation_config():
    config_mgr = ConfigurationManager()
    validation_config = config_mgr.get_data_validation_config()
    assert validation_config.STATUS_FILE is not None
