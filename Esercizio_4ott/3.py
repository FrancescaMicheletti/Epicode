'''Esercizio 3: Scrivi un programma che chiede all'utente in input:
i litri di benzina nel serbatoio
L'efficienza espressa in km per litro
Il prezzo della benzina per litro
Quindi visualizza il costo per 100 km e quanta distanza può percorrere l'auto con la benzina nel serbatoio'''

litri_benzina = float(input('litri di benzina nel serbatoio: '))
efficienza = float(input('l\'efficienza espressa in km/l: '))
prezzo = float(input('prezzo: '))
costo_100_km = 100 / efficienza * prezzo
print('costo per 100 km: ', costo_100_km)
distanza = efficienza * litri_benzina
print ('distanza: ', distanza)