'''Esercizio 1
Scrivi un programma che trasforma in maiuscolo tutte le consonanti di una stringa in input da tastiera (le vocali sono a e i o u) '''


stringa = input('scrivi una stringa:')
#rende maiuscoli tutti i caratteri
stringa = stringa.upper()
#rende minuscole le vocali
stringa = stringa.replace('A', 'a')
stringa = stringa.replace('E', 'e')
stringa = stringa.replace('I', 'i')
stringa = stringa.replace('O', 'o')
stringa = stringa.replace('U', 'u')
print(stringa)