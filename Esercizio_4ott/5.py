'''Esercizio 5: Scrivi un programma che chiede in input all'utente una stringa e visualizza i primi 3 caratteri, seguiti da 3 punti di sospensione e quindi gli ultimi 3 caratteri'''
#OPZIONE 1
stringa = input('Inserisci una stringa con più di 6 caratteri: ')
while len(stringa) <6:
      stringa = input('Inserisci una stringa con più di 6 caratteri: ')
if len(stringa) >= 6:
    print(stringa[:3], '...', stringa[-3:])

#OPZIONE 2
stringa = ''
while len(stringa) <6:
    stringa = input('Inserisci una stringa con più di 6 caratteri: ')
print(stringa[:3], '...', stringa[-3:])