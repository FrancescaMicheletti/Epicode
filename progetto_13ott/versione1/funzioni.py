import mysql.connector
from sqlalchemy import create_engine
#### CONNESSIONE A DBMS MYSQL CON CONNETTORE ####
def connection_database_conn(user, password, host, database):
    """
    Stabilisce la connessione con un database
    :param user: username
    :param password: password
    :param host: indirizzo, solitamente localhost
    :param database: nome del database
    :return connettore
    """
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host, database=database)
        return conn
    except mysql.connector.errors.DatabaseError as db_error:
        print(db_error.msg)
    return None


def execute_query(cursor, query_stmt):
    """
    Permette di eseguire una query SQL
    :param cursor: cursore da funzione conn.cursor()
    :param query_stmt: query SQL, ad es da query_select(), query_insert(), query_delete()
    """
    cursor.execute(query_stmt)
    print('Query -%s- eseguita correttamente' % query_stmt.split(' ')[0])


def print_result(cursor):
    """
    Permette di stampare i risultati di una query SQL
    :param cursor: cursore da funzione conn.cursor()
    """
    for i in cursor.fetchall():
        print(i)


def close_connection(conn):
    """
    Permette di chiudere la connessione al server
    :param conn: cursore da funzione connection_database()
    """
    conn.close()


####CONNESSIONE A DBMS MYSQL CON PANDAS####
def connect_database_pandas(u, pw, host_add, db):
    """
    Crea engine per la connessione a un database tramite pandas e sql_alchemy
    :param u: username
    :param pw: password
    :param host_add: indirizzo dell'host, se local host '127.0.0.1
    :param db: nome del database
    :return connettore per sql tramite pandas
    """
    db_connection_str = f"mysql+pymysql://{u}:{pw}@{host_add}/{db}"
    db_conn = create_engine(db_connection_str)
    return db_conn


#### FUNZIONI PER QUERIES PARAMETRIZZATE ####
def select_from(cols, table):
    """
    Restituisce una stringa SQL per la porzione select di una query
    :param cols: (tuple) colonne che si vogliono selezionare
    :param table: (str) tabella da cui si vogliono selezionare i dati
    :return stringa SELECT attributi FROM tabella
    """
    if type(cols) == str:
        q = f"SELECT {cols} FROM {table}"
    else:
        q = f"SELECT {','.join(cols)} FROM {table}"
    return q


def select_distinct_from(cols, table):
    """
    Restituisce una stringa SQL per la porzione select distinct di una query
    :param table: (str) tabella da cui si vogliono selezionare i dati
    :param cols: (list of str) attributi che si vogliono selezionare
    :return SELECT DISTINCT attributi FROM tabella
    """
    return f"SELECT DISTINCT {','.join(cols)} FROM {table}"


def f_join(query, table, on1, on2):
    """
    Restituisce una stringa SQL per la porzione join di una query
    :param query: (str) query select oppure select distinct
    :param table: (str) tabella con cui si vuole fare il join
    :param on1: (str) attributo della tabella di partenza con i valori tramite cui è possibile il join
    :param on2: (str) attributo della tabella table con i valori tramite cui è possibile il join
    :return query inserita JOIN tabella ON attributo1 = attributo2
    """
    return f"{query} JOIN {table} ON {on1} = {on2}"


def f_where(query, condition):
    """
        Restituisce una stringa SQL per la porzione where di una query
        :param query: (str) query select oppure select distinct
        :param condition: (str) condizione su cui fare il where
        :return query inserita WHERE condizione
    """
    return f"{query} WHERE {condition}"


def f_groupby(query, column_g):
    """
        Restituisce una stringa SQL per la porzione group by di una query
        :param query: (str) query select oppure select distinct
        :param column_g: (tuple) attributo/i tramite cui si vogliono raggruppare i valori
        :return query inserita GROUP BY attributi
    """
    return f"{query} GROUP BY {column_g}"


def f_orderby(query, column_o):
    """
        Restituisce una stringa SQL per la porzione order by di una query
        :param query: (str) query select oppure select distinct
        :param column_g: (tuple) attributo/i tramite cui si vogliono ordinare i valori
        :return query inserita ORDER BY attributi
    """
    return f"{query} ORDER BY {column_o}"


def f_having(query, condition):
    """
        Restituisce una stringa SQL per la porzione having di una query
        :param query: (str) query select oppure select distinct
        :param condition: (str) condizione
        :return query inserita HAVING condizione
    """
    return f"{query} HAVING {condition}"


def query(query):
    """
        Restituisce una stringa SQL per una query
        :param query: (str) query
        :return query;
    """
    return f"{query};"  # aggiunge ';' alla fine della query


def subquery(query, alias):
    """
        Restituisce una stringa SQL per una subquery
        :param query: (str) query
        return (subquery as alias)
    """
    return f"({query}) as {alias}"  # aggiunge il un alias per la subquery, che viene chiusa tra parentesi