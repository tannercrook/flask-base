# PostgreSQL
import psycopg2
from psycopg2 import extras

def connection():
    conn = psycopg2.connect(host="host",database="db",user="user",password="password")
    c = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    return c, conn