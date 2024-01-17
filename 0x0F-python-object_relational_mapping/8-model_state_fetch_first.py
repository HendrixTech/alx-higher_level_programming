#!/usr/bin/python3

"""
This is a script that prints the first State object
from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sesssionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """

    db_link = "mysql+mysqldb://{}:{}@localhost:3306{}".format(
            argv[1], argv[2], argv[3])

    engine = create_engine(db_link)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state is not None:
        print('{0}: {1}'.format(state.id, state.name))
    else:
        print("Nothing")
