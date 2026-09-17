import os
from textSummarizer.config.configuration import ConfigurationManager

def test_config_manager():
    config_mgr = ConfigurationManager()
    ingestion_config = config_mgr.get_data_ingestion_config()
    assert ingestion_config is not None
    assert os.path.exists(config_mgr.config_filepath)

def test_data_validation_config():
    config_mgr = ConfigurationManager()
    validation_config = config_mgr.get_data_validation_config()
    assert validation_config.STATUS_FILE is not None
