#!/usr/bin/python3

"""
This is a script that prints the State object with the
name passed as argument from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and print the state object with
    name passed as argument
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    search_state = argv[4]

    state = session.query(State).filter(State.name == search_state).first()

    if state is not None:
        print('{0}'.format(state.id))
    else:
        print('Not found')
