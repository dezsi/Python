# lista = []
# for item in 'Ana are mere':
#     list.append(item)


# lista = [item for item in 'ana are mere']
# print (lista)

# a = 'ana are mere'
# lista =[e for i, e in enumerate(lista(a)) if i % 2 == 0]
# print(lista)


# my_numbers = [1, 2, 3, 4, 5]
# lista_numere = [item ** 2 for item in my_numbers if item % 2 ==0]
# print(lista_numere)


# lista_produse = [ ' ciocolate', 'suc', 'mere', 'miere', 'apa']
# lista_noua = [x for x in lista_produse if "a" in x]
# print(lista_noua)


# lista = [ x for x in range(10)] if x < 5
# print(lista)

# a, b = 10, 20
# min = a if a <b else b
# # if a < b
# #     min = a
# # else:
# #     min = b
#
# print(min)

# lista_produse = [ ' ciocolate', 'suc', 'mere', 'miere', 'apa']
# lista_noua = [x if x != 'suc' else 'apa minerala' for x in lista_produse]
# print(lista_noua)

#
# lista_numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def functie_nr_pare(number):
#     if number %2 == 0:
#         return True
#     return False
#
# iterator_numere_pare = filter(functie_nr_pare, lista_numere)
#
# print(list(iterator_numere_pare))



# litere = [ 'a' , 'b', 'c', 'd', 'e', 'i', 'j']
# def filter_vocala(letter):
#     vocale = ['a', 'e', 'i', 'o', 'u']
#     turn True if letter in vocale else False
#
# print(filter_vocale(litere))