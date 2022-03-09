board = [' ' for x in range(10)]
def insertLetter(letter, pos):
    board[pos] = letter
def spaceIsFree(pos):
    return board[pos] == " "
def printBoard(board):
    print(" " + board[1] + "| " + board[2] + "| " + board[3])
    print("---------")
    print(" " + board[4] + "| " + board[5] + "| " + board[6])
    print("---------")
    print(" " + board[7] + "| " + board[8] + "| " + board[9])
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))
def playMove():
    run = True
    while run:
        move = input("Introduce 'X' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10 :
                if spaceIsFree(move):
                    run = False
                    insertLetter("x", move)
                else:
                    print("Acest spatiu este deja ocupat")
            else:
                print("Te rog selecteaza un numar dint interval")
        except:
            print("Selecteaza un numar. ")
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in ['o','x']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    if 5 in possibleMoves:
        move = 5
        return move
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    return move
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]
def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True
def main():
    print("Bine ai venit la x si 0")
    printBoard(board)
    while not(isBoardFull(board)):
        if not(isWinner(board, "o")):
            playMove()
            printBoard(board)
        else:
            print("0 a castigat! ")
            break
        if not(isWinner(board, "x")):
            move  = compMove()
            if move == 0:
                print("Egalitate")
            else:
                insertLetter("o", move)
                print("PC-ul a ales pozitia'o' ", move, ":")
                printBoard(board)
        else:
            print("X'a castigat")
            break
    if isBoardFull(board):
        print("Egalitate")

main()


# import datetime
#
#
#
#
# def compact(number):
#     """Convert the number to the minimal representation. This strips the
#     number of any valid separators and removes surrounding whitespace."""
#     return clean(number, ' -').strip()
#
#
# def calc_check_digit(number):
#     """Calculate the check digit for personal codes."""
#     # note that this algorithm has not been confirmed by an independent source
#     weights = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
#     check = sum(w * int(n) for w, n in zip(weights, number)) % 11
#     return '1' if check == 10 else str(check)
#
#
# def get_birth_date(number):
#     """Split the date parts from the number and return the birth date."""
#     number = compact(number)
#     centuries = {
#         '1': 1900, '2': 1900, '3': 1800, '4': 1800, '5': 2000, '6': 2000,
#     }  # we assume 1900 for the others in order to try to construct a date
#     year = int(number[1:3]) + centuries.get(number[0], 1900)
#     month = int(number[3:5])
#     day = int(number[5:7])
#     try:
#         return datetime.date(year, month, day)
#     except ValueError:
#         raise InvalidComponent()
#
#
# def validate(number):
#     """Check if the number is a valid VAT number. This checks the length,
#     formatting and check digit."""
#     number = compact(number)
#     if not isdigits(number):
#         raise InvalidFormat()
#     # first digit should be a known one
#     # (7,8=foreign resident, 9=other foreigner but apparently only as NIF)
#     if number[0] not in '123456789':
#         raise InvalidComponent()
#     if len(number) != 13:
#         raise InvalidLength()
#     # check if birth date is valid
#     get_birth_date(number)
#     # TODO: check that the birth date is not in the future
#     # number[7:9] is the county, we ignore it for now, just check last digit
#     if calc_check_digit(number[:-1]) != number[-1]:
#         raise InvalidChecksum()
#     return number
#
#
# def is_valid(number):
#     """Check if the number is a valid VAT number."""
#     try:
#         return bool(validate(number))
#     except ValidationError:
#         return False




# utilizator = input(f"Numele tau este: ")
# while True:
#     S = ['1','2','3','4','5','6','7','8', '9']
#     #optiuni_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print(f"Buna {utilizator} alege prima cifra din CNP care poate sa fie  {S}")
#     break
# input_utilizator1 = input("Alege un numar dintre: \n1 / 2 - născuți între 1 ianuarie 1900 și 31 decembrie 1999\n3 / 4 - născuți între 1 ianuarie 1800 și 31 decembrie 1899 \n3 / 4 - născuți între 1 ianuarie 1800 și 31 decembrie 1899 \n5 / 6 - născuți între 1 ianuarie 2000 și 31 decembrie 2099 \n7 / 8 - pentru persoanele străine rezidente în România.\n9 - pentru persoanele străine.  ").lower()
# if input_utilizator1 in ('1','2'):
#     print("1 / 2 - născuți între 1 ianuarie 1900 și 31 decembrie 1999")
# elif input_utilizator1 in ('3', '4'):
#     print("3 / 4 - născuți între 1 ianuarie 1800 și 31 decembrie 1899")
# elif input_utilizator1 in ('5', '6'):
#     print("5 / 6 - născuți între 1 ianuarie 2000 și 31 decembrie 2099")
# elif input_utilizator1 in ('7', '8'):
#     print("7 / 8 - pentru persoanele străine rezidente în România")
# elif input_utilizator1 in ('9'):
#     print("9 - pentru persoanele străine")
# else:
#     print("Ai gresit numarul, mai incearca")
#
# input_utilizator2 = input("Ultimele doua cifre din anul tau de nastere:  ")
# AA = input_utilizator2
# if AA == range(0, 100):
#     print(AA)
# else:
#     print("Ai gresit")
#
# input_utilizator3 = input("Luna de nastere, alcatuita din 2 cifre: ")
# if input_utilizator3 in ['01','02','03','04','05','06','07','08', '09', '10', '11', '12']:
#     for n in input_utilizator3:
#         print(n)
# else:
#     print("Ai gresit")
#
# input_utilizator4 = input("Ziua ta de nastere, alcatuita din 2 cifre: ")
# if input_utilizator4 in ['01','02','03','04','05','06','07','08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21','22','23','24','25','26','27','28','29', '30', '31']:
#     for n in input_utilizator4:
#         print(n)
# else:
#     print("Ai gresit")
#
# input_utilizator5 = input("Codul judetului din care faci parte, alcatuita din 2 cifre de la 01 -> 52 ")
# JJ = input_utilizator5
# if input_utilizator5 == '01':
#     print("Alba")
# elif input_utilizator5 == '02':
#     print("Arad")
# elif input_utilizator5 == '03':
#     print("Arges")
# elif input_utilizator5 == '04':
#     print("Bacau")
# elif input_utilizator5 == '05':
#     print("Bihor")
# elif input_utilizator5 == '06':
#     print("Bistrita Nasaud")
# elif input_utilizator5 == '07':
#     print("Botosani")
# elif input_utilizator5 == '08':
#     print("Brasov")
# elif input_utilizator5 == '09':
#     print("Braila")
# elif input_utilizator5 == '10':
#     print("Buzau")
# elif input_utilizator5 == '11':
#     print("Caras-Severin")
# elif input_utilizator5 == '12':
#     print("Cluj")
# elif input_utilizator5 == '13':
#     print("Constanta")
# elif input_utilizator5 == '14':
#     print("Covasna")
# elif input_utilizator5 == '15':
#     print("Dambovita")
# elif input_utilizator5 == '16':
#     print("Dolj")
# elif input_utilizator5 == '17':
#     print("Galati")
# elif input_utilizator5 == '18':
#     print("Gorlj")
# elif input_utilizator5 == '19':
#     print("Harghita")
# elif input_utilizator5 == '20':
#     print("Hunedoara")
# elif input_utilizator5 == '21':
#     print("Ialomita")
# elif input_utilizator5 == '22':
#     print("Iasi")
# elif input_utilizator5 == '23':
#     print("Ilfov")
# elif input_utilizator5 == '24':
#     print("Maramures")
# elif input_utilizator5 == '25':
#     print("Mehedinti")
# elif input_utilizator5 == '26':
#     print("Mures")
# elif input_utilizator5 == '27':
#     print("Neamt")
# elif input_utilizator5 == '28':
#     print("Olt")
# elif input_utilizator5 == '29':
#     print("Prahova")
# elif input_utilizator5 == '30':
#     print("Satu Mare")
# elif input_utilizator5 == '31':
#     print("Salaj")
# elif input_utilizator5 == '32':
#     print("Sibiu")
# elif input_utilizator5 == '33':
#     print("suceava")
# elif input_utilizator5 == '34':
#     print("Teleorman")
# elif input_utilizator5 == '35':
#     print("Timis")
# elif input_utilizator5 == '36':
#     print("Tulcea")
# elif input_utilizator5 == '37':
#     print("Vaslui")
# elif input_utilizator5 == '38':
#     print("Valcea")
# elif input_utilizator5 == '39':
#     print("Vrancea")
# elif input_utilizator5 == '40':
#     print("Bucuresti")
# elif input_utilizator5 == '41':
#     print("Bucuresti S.1")
# elif input_utilizator5 == '42':
#     print("Bucuresti S.2")
# elif input_utilizator5 == '43':
#     print("Bucuresti S.3")
# elif input_utilizator5 == '44':
#     print("Bucuresti S.4")
# elif input_utilizator5 == '45':
#     print("Bucuresti S.5")
# elif input_utilizator5 == '46':
#     print("Bucuresti S.6")
# elif input_utilizator5 == '47':
#     print("Calarasi")
# elif input_utilizator5 == '48':
#     print("Giurgiu")
# else:
#     print("Ai gresit")
#
# import random
# # input_utilizator6 = ("Codul din care faci parte, alcatuita din 3 cifre de la 001 -> 999 ")
# # NNN = input_utilizator6
# print("Codul din care faci parte: ", random.randrange(1, 999))
#
# input_utilizator7 = input("Cifra de control:  ")
# C = input_utilizator7
# print(C)