'''Esercizio 4: Scrivi un programma chiede in input all'utente una misura in metri
e la converte in miglia, piedi e pollici'''

misura_m = float(input('scrivi una misura in metri: '))
misura_miglia = misura_m * 0.000621371
print ('miglia: ',misura_miglia)
misura_piedi = misura_m * 3.28084
print ('piedi: ', misura_piedi)
misura_pollici = misura_m * 39.3701
print ('pollici: ', misura_pollici)