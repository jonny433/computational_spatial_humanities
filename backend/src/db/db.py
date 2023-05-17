import os
import psycopg2


class DB:
    def __init__(self,
                 host: str = os.getenv("POSTGRES_HOST", "localhost"),
                 port: int = os.getenv("POSTGRES_PORT", 5432),
                 database_name: str = os.getenv("POSTGRES_DATABASE_NAME", "mydb"),
                 user: str = os.getenv("POSTGRES_USER", "postgres"),
                 password: str = os.getenv("POSTGRES_PASSWORD", "postgres")
                 ):
        self.host = host
        self.port = port
        self.database = database_name
        self.user = user
        self.password = password
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.conn.cursor()
            print("Connected to database")
        except Exception as e:
            print("Could not connect to database:", e)

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Disconnected from database")

    def execute_query(self, query):
        print("HALLO")
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print("Query executed successfully")
        except Exception as e:
            print("Error executing query:", e)

# import pandas as pd
# data = {
#     "lon": [52.4, 52.4],
#     "lat": [91.5, 93.4]
# }
# df = pd.DataFrame(data)
#
# db = DB()
#
#
# db.disconnect()
