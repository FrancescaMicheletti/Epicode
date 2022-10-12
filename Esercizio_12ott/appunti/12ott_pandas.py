import pandas as pd

##SERIES##
data = pd.Series([6, 7, 9, 1, 10, 0])
# costruttore delle Series prende in input una lista di elementi;
#print(data)
# colnna di sinistra sono gli indici, la colonna di dx sono gli elementi della serie;
# dtype = tipo di dati inseriti nella serie (in questo caso intero di dimensione 64 bit)

d = [6, 7, 9, 1, 10, 0]
i = ['a', 'b', 'c', 'd', 'e', 'f']
#data = pd.Series(d, index=i)
# costruttore delle Series prende in input una lista di elementi;
# possiamo passare come secondo parametro la lista degli indici che vogliamo settare index = []
#print(data)

# accedo agli elementi della serie tramite gli indici
#print(data['c'])

#student_dict = {'Testa': 24, 'Micheletti': 19, 'Colavito': 30, 'Casciaro': 22}
# ogni chiave ha un singolo valore
#students = pd.Series(student_dict)
# costruttore delle Series prende in input anche un dizionario (già con indici);
# attenzione, rimane un array monodimensionale inidicizzato

#print(students)
#print(students['Colavito'])

# slicing sulle serie, l'estremo superiore è incluso; ottengo una nuova serie
#students_sliced = students['Micheletti':'Casciaro']

##DATAFRAME##
# Tabelle bidimensionali, una sorta di dizionario di series

d = {'Testa': [30, 12, 21, 30, 12, 21], 'Micheletti': [21, 30, 19, 30, 12, 21],
     'Colavito': [25, 26, 25, 30, 12, 21], 'Casciaro': [30, 23, 24, 30, 12, 21]}
# ogni chiave ha associato una lista di valori (della stessa lunghezza)
df = pd.DataFrame(d)
#print(df)

#print(df.head())  # la funzione restituisce di default le prime 5 righe del dataframe
#print(df.tail(3))  # la funzione restituisce di default le ultime 5 righe del dataframe, altrimenti n righe in input

#print(df.index)  # la funzione restituisce gli indici delle righe
#print(df.columns)  # la funzione restituisce una lista con i nomi delle colonne
#print(df.values)  # la funzione restituisce i valori del dataframe sotto forma di array di numpy
#print(df.describe())  # la funzione restituisce varie statistiche

df.sort_index(axis=1, ascending=True, inplace=True)  # ordina colonne o righe in base agli indici
# #axis (0 →righe, 1→colonne), ascending (True, False),
# inplace (True applica le modifiche a df senza dover eseguire l'assegnazione, False richiede l'assegnazione)
#print(df)

df.sort_values(by='Colavito', inplace=True)  # ordina le righe in base ai valori di una specifica colonna
#print(df)

# possibile ricavare lista di tuple connettendosi a SQL e poi trasformarla in pandas DF

# selezionare i dati di un'intera colonna
micheletti = df['Micheletti']  # restituisce una serie

# selezionare i dati di più colonne
risultati = df[['Micheletti', 'Casciaro']]
#print(risultati)

# selezionare i dati
risultati2 = df.loc[0]  # voglio la prima riga (indice 0) della tabella,
#print(risultati2)

# con loc è possibile selezionare i dati anche su multi asse su righe e colonne
# voglio selezionare tutte le righe (:) della colonna 'Testa'
risultati3 = df.loc[:, ['Testa']]
#print(risultati3)
risultati4 = df.loc[2:4, ['Testa']]  # seleziono il sottoinsieme delle righe

# con iloc è possibile selezionare i dati per posizione, posso usare lo slicing
risultati5 = df.iloc[1] # seleziono i dati per posizione 1
#print(risultati5)

#Filtrare i dati tramite indicizzazione booleana
risultato_bool = df['Casciaro']>24
#print(risultato_bool)

risultato6 = df[df>23] #inserisce solo i valori che rispettano la condizione
#print(risultato6)

#posso combinare le condizioni

risultato7 = df[(df>23) & (df!=30)] #combino le condizioni
# python: and pandas: &
# python: or pandas: |
# python: not pandas: !=
#print(risultato7)

#aggiungere una colonna al dataframe (colonne non necessariamente omogenee per il tipo di dato
df['Competenze'] = ['php', 'java', 'java', 'php', 'python','python'] #df[nomecolonna] = [lista di valori]

risultato8 = df[df['Competenze'].str.startswith('p')]  #voglio prendere i dati per cui
                                                       # i valori della colonna competenze iniziano per p
risultato8 = df[df['Competenze'].str.endswith('n')]

#print(risultato8)
#attenzione: gli indici di riga non cambiano, sono quelli che sono stati assegnati all'inizio

l = ['java', 'python']
risultato9 = df[df['Competenze'].isin(l)]
#print(risultato9)

#cambiare indici del df
df['Numeri'] = ['uno', 'due', 'tre', 'quattro', 'cinque','sei'] #inserisco nuova colonna con nuovi indici
#print(df)
df.set_index(['Numeri'], inplace=True) #nuovi indici, che userò per ricavare i dati dal df
#print(df)
#print(df.loc['uno'])

#si possono resettare gli indici
df.reset_index('Numeri', inplace =True) #reset degli indici ('Numeri') che diventa colonna del df
#print(df)

#cambiare i valori di una singola cella del df
df.at[1, 'Competenze'] = 'C++' #df.at[indiceriga, nomecolonna]
df.iat[2, 5] = 'C++' #df.at [posizioneriga, posizionecolonna]
#print(df)

#applicare una funzione al df
def converti(stringa):
     if stringa == 'uno':
          return 1
     elif stringa == 'due':
          return 2
     else:
          return 0

#df['col_trasformata'] = df['Numeri'].apply(converti) #seleziono la colonna.apply(nomemetodo)
#al metodo passo il nome del metodo, che è l'applicazione del metodo con parametri ciò su cui noi possiamo
#print(df)

#join (di default 'inner', specifico con how 'left', 'right, 'outer', 'inner',
# 'cross' prodotto cartesiano da entarmbi i df preservando l'ordine delle chiavi di sx)

#creo un secondo df
d2 = {'Comp': ['php', 'java', 'python', 'R', 'julia', 'c'], 'Peso': [5,4,3,2,10,8]}
df_comp = pd.DataFrame(d2)
#print(df, '\n', df_comp)

df_merged = pd.merge(df, df_comp, left_on='Competenze', right_on=('Comp'))
#(df_sx, df_dx, left_on = colonnadfsx, right_on =colonnadfdx)

#se le colonne nei 2 df hanno lo stesso nome pd.merge(df, df_comp, on = nomecolonnaincomune)
d2 = {'Competenze': ['php', 'java', 'python', 'R', 'julia', 'c'], 'Peso': [5,4,3,2,10,8]}
df_comp2 = pd.DataFrame(d2)
df_merged2 = pd.merge(df, df_comp2, on='Competenze')
#print(df_merged2)

#aggiungere una riga
df_comp = df_comp.append({'Comp': 'Javascript', 'Peso': 11}, ignore_index=True)
#in input prende un dizionario chiavi colonne valor valori da aggiungere

nuova_riga = pd.DataFrame([{'Comp': 'Tableau', 'Peso': 15}])
df_comp = pd.concat([df_comp, nuova_riga], ignore_index = True) #usando pd.concat
#print(df)

#raggruppamento
df_grouped = df.groupby(['Competenze']).mean()    #attenzione devo sempre applicare una funzione di aggregazione
                                                  # (in questo caso mean)

df_grouped = df.groupby(['Competenze', 'Numeri']).mean()     #se uso 2 gruppi diversi, avrò 2 indici
                                                            #→df supportano i multi indice per le righe
#print(df_grouped)

#leggere un file
#csv
df_read = pd.read_csv('voti_all.csv', sep = ',', header=0) #si può passare anche il sito internet che punta al file (slide 33)
print(df_read.columns, df_read.head())
#excel
#df_excel = pd.read_excel(file.xlsx, sheet_name = 'nome', index_col = )
#json
#df_json = pd.read_json(file.json, orient) per orient leggere documentazione
#esportare un df in csv
df_read.describe().to_csv('export.csv', sep=';', header=True)
df_read.describe().to_json('export.json')