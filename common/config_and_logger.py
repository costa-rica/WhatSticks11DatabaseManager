import os
from ws_config import ConfigWorkstation, ConfigDev, ConfigProd
import logging
from logging.handlers import RotatingFileHandler

match os.environ.get('WS_CONFIG_TYPE'):
    case 'dev':
        config = ConfigDev()
        print('- WhatSticks11DatabaseManager/config: Development')
    case 'prod':
        config = ConfigProd()
        print('- WhatSticks11DatabaseManager/config: Production')
    case _:
        config = ConfigWorkstation()
        print('- WhatSticks11DatabaseManager/config: Local')



#Setting up Logger
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
formatter_terminal = logging.Formatter('%(asctime)s:%(filename)s:%(name)s:%(message)s')

#initialize a logger
logger_db_manager = logging.getLogger(__name__)
logger_db_manager.setLevel(logging.DEBUG)

if not os.path.exists(config.PROJECT_RESOURCES):
    os.makedirs(config.PROJECT_RESOURCES)

#where do we store logging information
file_handler = RotatingFileHandler(os.path.join(config.PROJECT_RESOURCES,'database_manger.log'), mode='a', maxBytes=5*1024*1024,backupCount=2)
file_handler.setFormatter(formatter)

#where the stream_handler will print
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter_terminal)

logger_db_manager.addHandler(file_handler)
logger_db_manager.addHandler(stream_handler)