import os

import psycopg
from dotenv import load_dotenv


load_dotenv()

database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise ValueError("DATABASE_URL was not found in the .env file")


with psycopg.connect(database_url) as connection:
    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """)

        tables = cursor.fetchall()


print("Tables in PostgreSQL:")

for table in tables:
    print(f"- {table[0]}")