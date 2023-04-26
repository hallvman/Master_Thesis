import DbConnector
from tabulate import tabulate

class Queries:

    def __init__(self, connection: DbConnector):
        self.connection = connection
        self.db_connection = self.connection.db_connection
        self.cursor = self.connection.cursor

    def numberOfUsers(self):
        try:
            query = "SELECT Count(*) FROM Master_Thesis_DB.USER"
            print(f"\nTrying to run query: {query}\n")
            self.cursor.execute(query) # Execute the query
            rows = self.cursor.fetchall() # fetch the rows
            print(f"Number of Users:\n {tabulate(rows)}")
        except Exception as e:
            print(f"Error Message: {e}")

    def numberOfActivities(self):
        try:
            query = "SELECT Count(*) FROM Master_Thesis_DB.ACTIVITY"
            print(f"\nTrying to run query: {query}\n")
            self.cursor.execute(query) # Execute the query
            rows = self.cursor.fetchall() # Fetch the rows
            print(f"Number of Activities:\n {tabulate(rows)}")
        except Exception as e:
            print(f"Error Mesaage: {e}")

    def numberOfTrackPoints(self):
        try:
            query = "SELECT Count(*) FROM Master_Thesis_DB.TRACK_POINTS"
            print(f"\nTrying to run query: {query}\n")
            self.cursor.execute(query) # Execute the query
            rows = self.cursor.fetchall() # Fetch the rows
            print(f"Number of Track_Points:\n {tabulate(rows)}")
        except Exception as e:
           print(f"Error Mesaage: {e}") 