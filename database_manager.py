import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from ws_models import Base,engine # Assuming this is where your models are defined
from common.config_and_logger import config, logger_db_manager

def drop_and_create_database(engine, database_name):
    logger_db_manager.info(f'- accessed: drop_and_create_database -')
    with engine.connect() as connection:
        try:
            connection.execute(text(f"DROP DATABASE IF EXISTS {database_name};"))
            connection.execute(text(f"CREATE DATABASE {database_name};"))
            logger_db_manager.info(f"Database {database_name} dropped and recreated successfully.")
        except SQLAlchemyError as e:
            logger_db_manager.info(f"An error occurred: {e}")

def create_tables( database_name):
    logger_db_manager.info(f'- accessed: create_tables -')
    new_engine_str = f"mysql+pymysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_SERVER}/{config.MYSQL_DATABASE_NAME}"
    new_engine = create_engine(new_engine_str)
    Base.metadata.create_all(new_engine)
    logger_db_manager.info("Tables created successfully.")

if __name__ == "__main__":
    logger_db_manager.info(f'--- Started What Sticks 11 Database Manager ---')
    drop_and_create_database(engine, config.MYSQL_DATABASE_NAME)
    create_tables(config.MYSQL_DATABASE_NAME)
