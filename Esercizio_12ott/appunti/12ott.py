import sys
import mysql.connector

def connection_database(user, password, host, database):
    try:
        conn = mysql.connector.connect(user = user, password = password, host = host, database = database)
        return conn
    except mysql.connector.errors.DatabaseError as db_error:
        print(db_error.msg)
    return None

def query():
# todo
def execute_query():
# todo
def print_result():
# todo
def close_connection():
# todo

if __name__ == '__main__':
    conn = connection_database(sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4])
    #i parametri sys si passano da terminale
    #cd cartella_file_python
    #python3 file_python.py
    #scrivo i parametri
    #da pycharm li metto in Parameters da edit configurations
    try:
        c = conn.cursor()
        q = query()
        execute_query(c,q)
        print_result(c)
    finally:
        if conn is not None:
            cloe_connection(conn)