import sys

from DbConnector import DbConnector
from insert_data.DatabaseSetup import DatabaseSetup
from Queries import Queries
import time
from datetime import timedelta

def initiateDatabase():
    connector = DbConnector() # Connect to the database
    initiate = DatabaseSetup(connector) # Initiate state object
    
    # Drops tables if they exist
    initiate.drop_tables()
    
    # Creates the tables for the database
    initiate.create_tables()
    
    # Inserts users to the database
    initiate.insert_users()
    
    # Traverses the activities and track points
    initiate.traverse_dataset()

def queries():
    # Connector to the database and create query object
    connector = DbConnector()
    query = Queries(connector)

    # Runs the query for number of Users
    query.numberOfUsers() 

    # Runs the query for number of Activities
    query.numberOfActivities() 

    # Runs the query for number of Track Points
    query.numberOfTrackPoints()

def main():
    # Sets up the database and inserts data
    start_time = time.now()
    print(timedelta(start_time))
    initiateDatabase()

    # Runs queries
    queries()
    end_time = time.now()
    print(timedelta(end_time))
    print(timedelta(seconds=end_time - start_time))


if __name__ == "__main__":
    main()