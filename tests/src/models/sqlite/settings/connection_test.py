import pytest
from sqlalchemy.engine import Engine

from src.models.sqlite.settings.connection import DBConnectionHandler

def test_db_connection():
    connection_handler = DBConnectionHandler()

    assert connection_handler.get_engine() is None
    
    connection_handler.connect()
    engine = connection_handler.get_engine()

    assert engine is not None
    assert isinstance(engine, Engine)