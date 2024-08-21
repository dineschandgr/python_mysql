import pymysql


class dbconfig:

    @staticmethod
    def open_connection():
        conn = pymysql.connect(
            host='mysqldb',
            user='root',
            password="password",
            db='user_schema',
        )
        return conn

    @staticmethod
    def close_connection(conn):
        conn.close()