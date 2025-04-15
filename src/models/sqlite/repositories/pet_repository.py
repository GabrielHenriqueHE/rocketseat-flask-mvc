from typing import List
from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.pet import PetsTable

class PetRepository:
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def get_all_pets(self) -> List:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []
            
    def delete_pet(self, name: str) -> None:
        with self.__db_connection as database:
            try:
                pet = database.session.query(PetsTable).filter(PetsTable.name == name).first()
                database.session.delete(pet)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception