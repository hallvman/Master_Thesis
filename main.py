import sys

from DbConnector import DbConnector
from insert_data.DatabaseSetup import DatabaseSetup

def connect():
    # Creates a connection with the database
    connector = DbConnector()
    # Creates a database setup object
    setup = DatabaseSetup(connector)
    # Drops the table if it is already created
    # setup.drop_tables()
    # Creates the tables if they don't already exist
    setup.create_tables()
    # Insert user.
    setup.insert_users()
    # Inserts activities and track points
    setup.traverse_dataset()

def main():
    connect()


if __name__ == "__main__":
    main()