# my_lambda = lambda x, y: x + y
# #denumire functie = lambda param1, param2: corp_functie
# my_sum = my_lambda(2, 3)
# print(my_sum)
#
#
# def my_lambda(x,y):
#     return x + y


# diferenta = lambda x, y, z: x-y-z
# dif = diferenta(4, 3)
# print(dif)


players = [{
    "first_name": "Ion",
    "last_name": 'gheorghe',
    'varsta':12
},
{
    "first_name": "andreea",
    "last_name": 'popa',
    'varsta':15
},
{
    "first_name": "isabela",
    "last_name": 'enache',
    'varsta':25
}
]

jucatori_sortati = sorted(players, key=lambda jucator: jucator['first_name'])
print(jucatori_sortati)