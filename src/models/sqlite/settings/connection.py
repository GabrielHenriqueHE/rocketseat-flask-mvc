from sqlalchemy import create_engine

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = 'sqlite:///storage.db'
        self.__engine = None

    def connect(self) -> None:
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine
    
connection_handler = DBConnectionHandler()