import psycopg2
import os
from psycopg2 import OperationalError
from dotenv import load_dotenv

load_dotenv()

# Establishing connection
try:
    connection = psycopg2.connect(
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        host = os.getenv("DB_HOST"),
        port = os.getenv("PORT")
    )
    print("Connection successful")
except OperationalError as e:
    print(f"Error: unable to connect to the database. {e}")

#create connection using the connection
cursor = connection.cursor()

try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
                 id SERIAL PRIMARY KEY,
                 name VARCHAR(100),
                 age INTEGER);
""")
    connection.commit()
    print("Table created succefully")
except Exception as e:
    print(f"Error creating table: {e}")

# Inserting data
try:
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("alice", 30))
    connection.commit()
    print("Data inserted successfully")
except Exception as e:
    print(f"Error inserting data. {e}")