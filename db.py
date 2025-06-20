import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

# DB 연결
def get_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        db=os.getenv('DB_NAME'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

# SELECT 쿼리 실행
def fetch_value(query, params=None):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params or ())
            result = cursor.fetchall()
            return result
    finally:
        conn.close()

# INSERT/UPDATE/DELETE 쿼리 실행
def execute_query(query, params=None):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params or ())
        conn.commit()
    finally:
        conn.close()
