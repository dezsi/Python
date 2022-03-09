1.)
def sum_treinumere_daca_sunt_egale(x, y, z):
    sum = x + y + z
    if x == y == z:
        sum = sum * 3
    return sum

print(sum_treinumere_daca_sunt_egale(1, 2, 3))

2.)
lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def elimina_print_treia_numar(lista):
    pozitia = 3 - 1
    index = 0
    lungime_lista = (len(lista))

    while lungime_lista > 0:
        index = (pozitia + index) % lungime_lista

        print(lista.pop(index))
        lungime_lista -= 1

elimina_print_treia_numar(lista)

3.)

import itertools as it

dictionar={"1": "abc","2": "s","3": "o","4": "n","5": "lm","6": "jk","7": "gi","8": "def","9": "abc"}
all_keys = sorted(dictionar)
combinatii = it.product(*(dictionar[nume] for nume in all_keys))
print(list(combinatii))