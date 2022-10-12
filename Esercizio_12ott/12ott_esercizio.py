import mysql.connector


def connection_database(user, password, host, database):
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


def query_select_join(select, frm,  join1=None,  on1a=None, on1b=None, join2=None,
                 on2a=None, on2b=None, where=None, groupby=None, orderby=None):
    """
    Crea una stringa SQL per fare una selezione anche tramite join
    :param select: colonne da selezionare
    :param frm: tabella da cui si vogliono selezionare le colonne
    :param join1: prima tabella con cui si vuole fare il join
    :param on1a: colonna della tabella di partenza con i valori tramite cui è possibile il join
    :param on1b: colonna della prima tabella join1 con i valori tramite cui è possibile il join
    :param join2: seconda tabella con cui si vuole fare il join
    :param on2a: colonna della tabella join1 con i valori tramite cui è possibile il join
    :param on2b: colonna della seconda tabella join2 con i valori tramite cui è possibile il join
    :param where: condizione
    :param groupby: colonna tramite cui si vogliono raggruppare i valori
    :param orderby: colonna tramite cui si vogliono ordinare i valori
    :return stringa SQL
    """
    stmt = 'select %s from %s ' % (select, frm)
    if join1 is not None:
        stmt = stmt + "join %s " % join1
    if on1a is not None:
        stmt = stmt + "on %s " % on1a
    if on1b is not None:
        stmt = stmt + "= %s " % on1b
    if join2 is not None:
        stmt = stmt + "join %s " % join2
    if on2a is not None:
        stmt = stmt + "on %s " % on2a
    if on2b is not None:
        stmt = stmt + "= %s " % on2b
    if where is not None:
        stmt = stmt + "where %s " % where
    if groupby is not None:
        stmt = stmt + "group by %s " % groupby
    if orderby is not None:
        stmt = stmt + "order by %s " % orderby
    #stmt = stmt + ';'
    return stmt

def query_select(select, frm, where=None, groupby=None, orderby=None):
    """
    Crea una stringa SQL per fare una selezione senza join
    :param select: colonne da selezionare
    :param frm: tabella da cui si vogliono selezionare le colonne
    :param where: condizione
    :param groupby: colonna tramite cui si vogliono raggruppare i valori
    :param orderby: colonna tramite cui si vogliono ordinare i valori
    :return stringa SQL
    """
    stmt = 'select %s from %s ' % (select, frm)
    if where is not None:
        stmt = stmt + "where %s " % where
    if groupby is not None:
        stmt = stmt + "group by %s " % groupby
    if orderby is not None:
        stmt = stmt + "order by %s " % orderby
    #stmt = stmt + ';'
    return stmt


def query_insert(table, attributes, values):
    """
    Permette di scrivere una query SQL per inserire una nuova riga in una tabella
    :param table: tabella in cui inserire la riga
    :param attributes: attributi della tabella di cui si vogliono aggiungere i valori - tupla
    :param values: valori che si vogliono aggiungere, nell'ordine di attributes - tupla
    :return stringa SQL
    """
    if len(attributes) == len(values):
        # controllo che il numero degli attributi sia pari al numero di valori
        attributes = ','.join(attributes)  # con join unisco separandoli con virgola
        values = "'{0}'".format("','".join(values))  # con join unisco separandoli con virgola ma mantenendo gli apici
        stmt = 'insert into %s(%s) values(%s);' % (table, attributes, values)
        return stmt


def query_delete(table, condition):
    """
    Permette di scrivere una query SQL per eliminare righe in una tabella se soddisfano una determinata condizione
    :param table: tabella da cui cancellare le righe
    :param condition: condizione da soddisfare
    :return stringa SQL
    """
    stmt = 'delete from %s where %s;' % (table, condition)
    return stmt


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

tabella = 'disco'
attributi = ('NroSerie', 'TitoloAlbum', 'Anno', 'Prezzo')
valori = ('133', 'titolo12', '2012', '35')
condizione = 'NroSerie = 130'

query1 = ('NomeCantante', 'canzone', 'ESECUZIONE', 'canzone.CodiceReg', 'ESECUZIONE.CodiceReg', 'AUTORE',
              'ESECUZIONE.TitoloCanzone', 'AUTORE.TitoloCanzone', 'Nome=NomeCantante and Nome like "d%";')
query2 = ('TitoloAlbum', 'DISCO', 'CONTIENE', 'DISCO.NroSerie', 'CONTIENE.NroSerieDisco', 'ESECUZIONE',
              'CONTIENE.CodiceReg', 'ESECUZIONE.CodiceReg', 'ESECUZIONE.anno is NULL;')
subsubquery3 = ('CodiceReg', 'canzone S2', 'S2.NomeCantante <> S1.NomeCantante')
subquery3 = ('S1.NomeCantante', 'canzone as S1', 'CodiceReg not in')
query3 = ('distinct NomeCantante', 'canzone', 'NomeCantante not in (%s (%s));'
          %(query_select(*subquery3), query_select(*subsubquery3)))
subquery4 = ('S1.NomeCantante', 'canzone as S1','ESECUZIONE', 'esecuzione.CodiceReg', 'S1.CodiceReg',
             'canzone as S2', 'esecuzione.CodiceReg','S2.CodiceReg', 'S1.NomeCantante <> S2.NomeCantante')
query4 =('NomeCantante', 'canzone', 'NomeCantante not in (%s);'%query_select_join(*subquery4))

##INTERROGAZIONI##
if __name__ != '__main__':
    conn = connection_database('root', 'password', '127.0.0.1', 'discografia')
    try:
        c = conn.cursor()
        q1 = query_select_join(*query1)
        q2 = query_select_join(*query2)
        q3 = query_select(*query3)
        q4 = query_select(*query4)#* serve per prendere ogni valore della tupla e passarlo come stringa
        execute_query(c, q1)
        print_result(c)
        execute_query(c, q2)
        print_result(c)
        execute_query(c, q3)
        print_result(c)
        execute_query(c, q4)
        print_result(c)
    except:
        conn.rollback()
    finally:
        if conn is not None:
            close_connection(conn)

 ##INSERIMENTO##
if __name__ != '__main__':
    conn = connection_database('root', 'password', '127.0.0.1', 'discografia')
    try:
        c = conn.cursor()
        i = query_insert(tabella, attributi, valori)
        if i is not None:
            execute_query(c, i)
            conn.commit()
            print_result(c)
        else:
            print('La query non è andata a buon fine, inserire un numero di valori pari al numero degli attributi')
    except:
        conn.rollback()
    finally:
        if conn is not None:
            close_connection(conn)

##CANCELLAZIONE##
if __name__ != '__main__':
    conn = connection_database('root', 'password', '127.0.0.1', 'discografia')
    try:
        c = conn.cursor()
        d = query_delete(tabella, condizione)
        execute_query(c, d)
        conn.commit()
    except:
        conn.rollback()
    finally:
        if conn is not None:
            close_connection(conn)



