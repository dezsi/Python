# #import primul_nostru_modul
# from primul_notru_modul import my_sum as suma
# # import math
# # from math import sum
# # import random
# # from random import choice
# # if __name__ == '__main--':
# #     print(my_sum(4,5))
# #     # print(primul_nostru_modul.my_sum(1,4))
#
# # my_var = inpt("NUMAR INTREG: ")
# # my_int = None
# # try:
# #     my_int = 'test'
# #     print("exceptie generica", e)
# # else:
# #     print("daca nu apare exceptie ", my_int)
# # finally:
# #     print("afiseaza in orice caz")
# # print(my_int)


# # import random module
# import random
#
# # Print multiline instruction
# # performstring concatenation of string
# print("Winning Rules of the Rock paper scissor game as follows: \n"
#       + "Rock vs paper->paper wins \n"
#       + "Rock vs scissor->Rock wins \n"
#       + "paper vs scissor->scissor wins \n")
#
# while True:
#     print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
#
#     # take the input from user
#     choice = int(input("User turn: "))
#
#     # OR is the short-circuit operator
#     # if any one of the condition is true
#     # then it return True value
#
#     # looping until user enter invalid input
#     while choice > 3 or choice < 1:
#         choice = int(input("enter valid input: "))
#
#     # initialize value of choice_name variable
#     # corresponding to the choice value
#     if choice == 1:
#         choice_name = 'Rock'
#     elif choice == 2:
#         choice_name = 'paper'
#     else:
#         choice_name = 'scissor'
#
#     # print user choice
#     print("user choice is: " + choice_name)
#     print("\nNow its computer turn.......")
#
#     # Computer chooses randomly any number
#     # among 1 , 2 and 3. Using randint method
#     # of random module
#     comp_choice = random.randint(1, 3)
#
#     # looping until comp_choice value
#     # is equal to the choice value
#     while comp_choice == choice:
#         comp_choice = random.randint(1, 3)
#
#     # initialize value of comp_choice_name
#     # variable corresponding to the choice value
#     if comp_choice == 1:
#         comp_choice_name = 'Rock'
#     elif comp_choice == 2:
#         comp_choice_name = 'paper'
#     else:
#         comp_choice_name = 'scissor'
#
#     print("Computer choice is: " + comp_choice_name)
#
#     print(choice_name + " V/s " + comp_choice_name)
#
#     # condition for winning
#     if ((choice == 1 and comp_choice == 2) or
#             (choice == 2 and comp_choice == 1)):
#         print("paper wins => ", end="")
#         result = "paper"
#
#     elif ((choice == 1 and comp_choice == 3) or
#           (choice == 3 and comp_choice == 1)):
#         print("Rock wins =>", end="")
#         result = "Rock"
#     else:
#         print("scissor wins =>", end="")
#         result = "scissor"
#
#     # Printing either user or computer wins
#     if result == choice_name:
#         print("<== User wins ==>")
#     else:
#         print("<== Computer wins ==>")
#
#     print("Do you want to play again? (Y/N)")
#     ans = input()
#
#     # if user input n or N then condition is True
#     if ans == 'n' or ans == 'N':
#         break
#
# # after coming out of the while loop
# # we print thanks for playing
# print("\nThanks for playing")

# import random
# player = input("care este numele tau ?")
# while
#    # player = input("care este numele tau ?")
#     optiuni = ["piatra", "hartie", "foarfeca"]
#
#     print(f" salut {player1}, optiunile tale sunt: {optiuni1}")
#
#     player_choice = input("Alege o varianta: ").lower()
#
#     calculator = random.choice(optiuni)
#     print(f"Calculatorul a ales {calculator}")
#     if player.choice == calculator:
#     print("egalitate, reia jocul")
#     elif player_choice == "piatra":
#         if calculator == "hartie":
#             print("ai pierdut")
#         else:
#         print("ai castigat")
# elif player_choice == "hartie":
#     if calculator == "piatra":
#         print("ai pierdut")
#     else:
#         print("ai castigat")
# elif player_choice == "foarfeca":
#     if calculator == "hartie":
#         print("ai pierdut")
#     else:
#         print("ai castigat")
# realegere = [y/n]
# repetare = input("vrei sa joci din nou? y/n")
# if repetare == 'n'
#     break






import sys

utilizator = input(f"Numele tau este: ")
while True:
    S = ['1','2','3','4','5','6','7','8', '9']
    #optiuni_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Buna {utilizator} alege prima cifra din CNP care poate sa fie  {S}")
    break
input_utilizator1 = input("Alege un numar dintre: \n1 / 2 - născuți între 1 ianuarie 1900 și 31 decembrie 1999\n3 / 4 - născuți între 1 ianuarie 1800 și 31 decembrie 1899 \n3 / 4 - născuți între 1 ianuarie 1800 și 31 decembrie 1899 \n5 / 6 - născuți între 1 ianuarie 2000 și 31 decembrie 2099 \n7 / 8 - pentru persoanele străine rezidente în România.\n9 - pentru persoanele străine.  ").lower()

if input_utilizator1 in ('1','2'):
    print("1 / 2 - născuți între 1 ianuarie 1900 și 31 decembrie 1999")
elif input_utilizator1 in ('3', '4'):
    print("3 / 4 - născuți între 1 ianuarie 1800 și 31 decembrie 1899")
elif input_utilizator1 in ('5', '6'):
    print("5 / 6 - născuți între 1 ianuarie 2000 și 31 decembrie 2099")
elif input_utilizator1 in ('7', '8'):
    print("7 / 8 - pentru persoanele străine rezidente în România")
elif input_utilizator1 in ('9'):
    print("9 - pentru persoanele străine")
else:
    print("Ai gresit numarul, mai incearca")
    sys.exit()


input_utilizator2 = range(0, 100, 1)
AA = int(input('Ultimele doua cifre din anul tau de nastere:   '))

if AA in input_utilizator2:
    print(AA, 'este anul tau de nastere.')
else:
    print(AA, 'ai gresit , mai incearca.')
    sys.exit()

input_utilizator3 = input("Luna de nastere, alcatuita din 2 cifre: ")
if input_utilizator3 in ['01','02','03','04','05','06','07','08', '09', '10', '11', '12']:
    for LL in input_utilizator3:
        print(LL)
else:
    print("Ai gresit")
    sys.exit()

input_utilizator4 = input("Ziua ta de nastere, alcatuita din 2 cifre: ")
if input_utilizator4 in ['01','02','03','04','05','06','07','08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21','22','23','24','25','26','27','28','29', '30', '31']:
    for ZZ in input_utilizator4:
        print(ZZ)
else:
    print("Ai gresit")
    sys.exit()

input_utilizator5 = input("Codul judetului din care faci parte, alcatuita din 2 cifre de la 01 -> 52 ")
JJ = input_utilizator5
if input_utilizator5 == '01':
    print("Alba")
elif input_utilizator5 == '02':
    print("Arad")
elif input_utilizator5 == '03':
    print("Arges")
elif input_utilizator5 == '04':
    print("Bacau")
elif input_utilizator5 == '05':
    print("Bihor")
elif input_utilizator5 == '06':
    print("Bistrita Nasaud")
elif input_utilizator5 == '07':
    print("Botosani")
elif input_utilizator5 == '08':
    print("Brasov")
elif input_utilizator5 == '09':
    print("Braila")
elif input_utilizator5 == '10':
    print("Buzau")
elif input_utilizator5 == '11':
    print("Caras-Severin")
elif input_utilizator5 == '12':
    print("Cluj")
elif input_utilizator5 == '13':
    print("Constanta")
elif input_utilizator5 == '14':
    print("Covasna")
elif input_utilizator5 == '15':
    print("Dambovita")
elif input_utilizator5 == '16':
    print("Dolj")
elif input_utilizator5 == '17':
    print("Galati")
elif input_utilizator5 == '18':
    print("Gorlj")
elif input_utilizator5 == '19':
    print("Harghita")
elif input_utilizator5 == '20':
    print("Hunedoara")
elif input_utilizator5 == '21':
    print("Ialomita")
elif input_utilizator5 == '22':
    print("Iasi")
elif input_utilizator5 == '23':
    print("Ilfov")
elif input_utilizator5 == '24':
    print("Maramures")
elif input_utilizator5 == '25':
    print("Mehedinti")
elif input_utilizator5 == '26':
    print("Mures")
elif input_utilizator5 == '27':
    print("Neamt")
elif input_utilizator5 == '28':
    print("Olt")
elif input_utilizator5 == '29':
    print("Prahova")
elif input_utilizator5 == '30':
    print("Satu Mare")
elif input_utilizator5 == '31':
    print("Salaj")
elif input_utilizator5 == '32':
    print("Sibiu")
elif input_utilizator5 == '33':
    print("suceava")
elif input_utilizator5 == '34':
    print("Teleorman")
elif input_utilizator5 == '35':
    print("Timis")
elif input_utilizator5 == '36':
    print("Tulcea")
elif input_utilizator5 == '37':
    print("Vaslui")
elif input_utilizator5 == '38':
    print("Valcea")
elif input_utilizator5 == '39':
    print("Vrancea")
elif input_utilizator5 == '40':
    print("Bucuresti")
elif input_utilizator5 == '41':
    print("Bucuresti S.1")
elif input_utilizator5 == '42':
    print("Bucuresti S.2")
elif input_utilizator5 == '43':
    print("Bucuresti S.3")
elif input_utilizator5 == '44':
    print("Bucuresti S.4")
elif input_utilizator5 == '45':
    print("Bucuresti S.5")
elif input_utilizator5 == '46':
    print("Bucuresti S.6")
elif input_utilizator5 == '47':
    print("Calarasi")
elif input_utilizator5 == '48':
    print("Giurgiu")
else:
    print("Ai gresit")
    sys.exit()


import random
input_utilizator6 = ("Codul din care faci parte, alcatuita din 3 cifre de la 001 -> 999 ")
NNN = input_utilizator6
print("Codul din care faci parte: ", random.randrange(1, 1000))

input_utilizator7 = input("Cifra de control:  ")
C = input_utilizator7
print(C)

# print(str(input_utilizator1 + input_utilizator2 +input_utilizator3 + input_utilizator4 + input_utilizator5 + input_utilizator6))

CNP =str(S) + str(AA) + str(LL) + str(ZZ) + str(JJ) + str(NNN) + str(C)
print(CNP)

def validare(CNP):
    CNP = compact(CNP)
    if not isdigits(CNP):
        raise InvalidFormat()
    if CNP[0] not in '123456789':
        raise InvalidComponent()
    if len(CNP) != 13:
        raise InvalidLength()
def is_valid(CNP):
    try:
        return bool(validate(CNP))
    except ValidationError:
        return False
print(CNP)





