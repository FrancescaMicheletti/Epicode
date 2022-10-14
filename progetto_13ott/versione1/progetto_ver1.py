#### IMPORT ####
import pandas as pd
import funzioni as f

#### DATI DB ####
user = 'root'
password = 'password'
host = '127.0.0.1'
database = 'ecommerce'

#### QUERIES ####
# Quanti ordini sono stati consegnati con corriere? Qual è il metodo di pagamento scelto per questi ordini?
query1 = f.query(f.f_groupby(f.f_where(f.f_join(f.f_join(f.f_join(f.select_from
                                                      (('spedizione.nome tipo_spedizione',
                                                        'pagamento.nome metodo_pagamento',
                                                        'count(spedizione.nome) numero_ordini'), 'ordine'),
                                                      'pasp01', 'ordine.paspid', 'pasp01.paspid'),
                                               'spedizione', 'pasp01.spid', 'spedizione.spid'),
                                        'pagamento', 'pagamento.paid', 'pasp01.paid'), 'pasp01.spid = 2'),
                         ('spedizione.nome, pagamento.nome')))

# Quanti ordini sono stati consegnati in posta? Qual è il metodo di pagamento scelto per questi ordini?
query2 = f.query(f.f_groupby(f.f_where(f.f_join(f.f_join(f.f_join(f.select_from
                                                      (('spedizione.nome tipo_spedizione',
                                                        'pagamento.nome metodo_pagamento',
                                                        'count(spedizione.nome) numero_ordini'), 'ordine'),
                                                      'pasp01', 'ordine.paspid', 'pasp01.paspid'),
                                               'spedizione', 'pasp01.spid', 'spedizione.spid'),
                                        'pagamento', 'pagamento.paid', 'pasp01.paid'), 'pasp01.spid = 3'),
                         ('spedizione.nome, pagamento.nome')))

# Quanti sono gli utenti iscritti alla newsletter?
query3 = f.query(f.f_where(f.select_from('count(utente.newsletter) numero_iscritti_newsletter', 'ecommerce.utente'),
                       'utente.newsletter = 1'))

# Quanti utenti hanno partita iva?
query4 = f.query(
    f.f_where(f.select_from('count(utente.piva) numero_partiteiva', 'ecommerce.utente'), 'utente.piva IS NOT NULL'))

# Quanti utenti hanno come provincia Pistoia nel loro indirizzo principale ?
query5 = f.query(f.f_where(f.select_from(('provincia', 'conteggio'),
                                   f.subquery(f.f_groupby(f.f_where(f.select_from(
                                       ('indirizzo.provincia provincia', 'count(indirizzo.provincia) conteggio'),
                                       'ecommerce.indirizzo'), 'indirizzo.principale = 1'),
                                                      'indirizzo.provincia'), 'q')), "provincia = 'Pistoia'"))

# Qual è il numero medio di articoli per ordine?
query6 = f.query(f.select_from('round(AVG(num_articoli))',
                           f.subquery(f.f_groupby(f.select_from(('oid', 'sum(quantita) num_articoli'), 'ecommerce.orpr01'),
                                              'orpr01.oid'), 'media_num_art')))

# Qual è l'importo medio lordo speso per ordine?
query7 = f.query(f.select_from('AVG(spesa_tot)',
                           f.subquery(
                               f.f_groupby(f.select_from(('oid', 'sum(quantita*prezzo) spesa_tot'), 'ecommerce.orpr01'),
                                         'orpr01.oid'), 'spesa_lorda_media')))

# Qual è il numero di utenti che hanno fatto almeno un ordine?
query8 = f.query(f.select_from('sum(conteggio)',
                           f.subquery(f.f_having(f.f_groupby(
                               f.select_from(('ordine.uid', 'count(ordine.uid) conteggio', 'ordine.oid'),
                                           'ecommerce.ordine'),
                               'ordine.uid'), 'conteggio >= 1'), 'utenti_attivi')))

# Qual è il numero di utenti che hanno fatto più di un ordine?
query9 = f.query(f.select_from('sum(conteggio)',
                           f.subquery(f.f_having(f.f_groupby(
                               f.select_from(('ordine.uid', 'count(ordine.uid) conteggio', 'ordine.oid'),
                                           'ecommerce.ordine'),
                               'ordine.uid'), 'conteggio > 1'), 'utenti_fidelizzati')))

# Quale è la categoria più venduta? Con quanti pezzi?
query10 = f.query(f.select_from(('cat', 'max(art_per_cat)'), f.subquery(f.f_groupby(f.f_join(f.f_join(f.select_from(
    ('prodotto.pid', 'categoria.cid', 'categoria.nome cat', 'sum(orpr01.quantita) art_per_cat'), 'ecommerce.orpr01'),
    'prodotto', 'orpr01.pid', 'prodotto.pid'),
    'categoria', 'categoria.cid', 'prodotto.cid'), 'categoria.cid'),
    'cat_piu_venduta')))

# Numero di prodotti in catalogo per marca in ordine alfabetico
query11 = f.query(
    f.f_orderby(f.f_groupby(f.f_join(f.select_from(('marca.nome', 'count(prodotto.pid) num_prodotti'), 'ecommerce.marca'),
                               'prodotto', 'prodotto.mid', 'marca.mid'),
                        'marca.mid'),
              'marca.nome'))

query_list = [query1, query2, query3, query4, query5, query6, query7, query8, query9, query10, query11]

for i, q in enumerate(query_list):
    print('-----------QUERY %s---------------' % (i + 1))
    ##INTERROGAZIONI CON CONNETTORE##
    if __name__ == '__main__':
        conn = f.connection_database_conn(user, password, host, database)
        try:
            c = conn.cursor()
            f.execute_query(c, q)
            f.print_result(c)
        except:
            conn.rollback()
        finally:
            if conn is not None:
                f.close_connection(conn)
    ##INTERROGAZIONI CON PANDAS##
    db_connection = f.connect_database_pandas(user, password, host, database)
    result_pd = pd.read_sql(q, db_connection)
    print(result_pd)
