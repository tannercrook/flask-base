#import pymysql
import psycopg2


# MYSQL
# def connection():
#     conn = pymysql.connect(host="",
#                            user = "",
#                            passwd = "",
#                            db = "")
#     c = conn.cursor(pymysql.cursors.DictCursor)

#     return c, conn

# PostgreSQL
def connection():
    conn = psycopg2.connect()
    c = conn.cursor()
    return c, conn


