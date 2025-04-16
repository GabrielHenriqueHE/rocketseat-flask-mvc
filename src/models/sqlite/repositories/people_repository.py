from typing import List
from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.entities.pet import PetsTable

class PeopleRepository:
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        with self.__db_connection as database:
            try:
                person = PeopleTable(first_name=first_name, last_name=last_name, age=age, pet_id=pet_id)
                database.session.add(person)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    def get_person(self, person_id: int) -> PeopleTable:
        with self.__db_connection as database:
            try:
                person = (
                    database.session
                        .query(PeopleTable)
                        .outerjoin(PetsTable, PetsTable.id == PeopleTable.pet_id)
                        .filter(PeopleTable.id == person_id)
                        .with_entities(
                            PeopleTable.first_name,
                            PeopleTable.last_name,
                            PetsTable.name.label('pet_name'),
                            PetsTable.type)
                        .first()
                )
                
                return person
            except NoResultFound:
                return None