#!/usr/bin/python3

"""
This is a script that prints all City objects from
the database hbtn_0e_14_usa:
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Access database and print
    all city objects.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    result = session.query(City, State).order_by(City.id).join(State)

    for city, state in result.all():
        print('{0}: ({1}) {2}'.format(state.name, city.id, city.name))

    session.commit()
    session.close()
