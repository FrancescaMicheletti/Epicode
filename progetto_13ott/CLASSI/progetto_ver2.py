import pandas as pd
from progetto_13ott.CLASSI.Model.GroupBy import GroupBy
from progetto_13ott.CLASSI.Model.Having import Having
from progetto_13ott.CLASSI.Model.Join import Join
from progetto_13ott.CLASSI.Model.OrderBy import OrderBy
from progetto_13ott.CLASSI.Model.Query import Query, SubQuery
from progetto_13ott.CLASSI.Model.Select import Select
from progetto_13ott.CLASSI.Model.Where import Where
import progetto_13ott.versione1.funzioni as f


#### DATI DB ####
user = 'root'
password = 'password'
host = '127.0.0.1'
database = 'ecommerce'

# Query 1
tab = 'ordine'
attr = ('spedizione.nome tipo_spedizione', 'pagamento.nome metodo_pagamento', 'count(spedizione.nome) numero_ordini')
join1 = ('pasp01', 'ordine.paspid', 'pasp01.paspid')
join2 = ('spedizione', 'pasp01.spid', 'spedizione.spid')
join3 = ('pagamento', 'pagamento.paid', 'pasp01.paid')
cond = 'pasp01.spid = 2'
attr_group = 'spedizione.nome, pagamento.nome'

s1 = Select(tab, attr)
w1 = Where(cond)
j1 = [Join(*join1), Join(*join2), Join(*join3)]
gb1 = GroupBy(attr_group)

q1 = Query()
q1.set_select(s1)
q1.set_join(j1)
q1.set_where(w1)
q1.set_groupby(gb1)

#Query 9
attr_q = 'sum(conteggio)'
tab_sq = 'ecommerce.ordine '
attr_sq = ('ordine.uid', 'count(ordine.uid) conteggio', 'ordine.oid')
attr_group_sq = 'ordine.uid'
having_cond_sq = 'conteggio > 1'
alias_sq = 'utenti_fidelizzati'

s_sq = Select(tab_sq, attr_sq)
gb_sq = GroupBy(attr_group_sq)
h_sq = Having(having_cond_sq)

sq2 = SubQuery()
sq2.set_select(s_sq)
sq2.set_groupby(gb_sq)
sq2.set_having(h_sq)
sq2.set_alias(alias_sq)

s2 = Select(sq2, attr_q)
q2 = Query()
q2.set_select(s2)

query_list = [q1.stmt, q2.stmt]

for i, q in enumerate(query_list):
    print('-----------QUERY---------------' )
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




