import os
import psycopg2


from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.db_con = None

    def __enter__(self):
        try:
            self.db_con = psycopg2.connect(
                host=os.environ['PGHOST'],
                user=os.environ['PGUSER'],
                password=os.environ['PGPASSWORD'],
                database=os.environ['PGDATABASE'],
                port=os.environ['PGPORT']
            )
            self.cursor = self.db_con.cursor()
            return self
        except:
            raise

    def __exit__(self, exc_type, exc_val, traceback):
        self.db_con.close()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS my_table (
                    id SERIAL PRIMARY KEY)""")
        self.cursor.execute("TRUNCATE my_table RESTART IDENTITY;")
        self.cursor.execute("ALTER SEQUENCE my_table_id_seq RESTART WITH 1")
        self.cursor.execute("INSERT INTO my_table (ID) VALUES (1)")
        self.db_con.commit()

    def get_id(self):
        self.cursor.execute("SELECT id FROM my_table")
        value = self.cursor.fetchall()
        return value[0][0]

    def increment_id(self):
        self.cursor.execute(f"UPDATE my_table SET id = id + 1")
        self.db_con.commit()
