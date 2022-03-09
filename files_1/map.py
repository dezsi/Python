# def adunare(n):
#     return n + n


# lista_numere = [1, 2, 3, 4, 6]
# lista_numere_2 = [5, 6, 7, 8]
# # rezultat = map(adunare, lista_numere)
# # print(list(rezultat))
#
#
# rezultat = map(lambda n, m: n + m, lista_numere, lista_numere_2)
# print(list(rezultat))

#
# def adunare(lista_numere, lista_numere_2):
#     suma = 0
#     lista_adunare = []
#     # for i in range(0, min([len(lista_adunare), len(lista_numere_2)])):
#     for i, v in enumerate(lista_numere):
#         for j, w in enumerate(lista_numere_2):
#             # lista_numere[i] + lista_numere_2[j]
#             suma = v + w
#             lista_adunare.append(suma)
#     return lista_adunare
#
# print(adunare(lista_numere, lista_numere_2))



# def my_function():
#    task = input("Enter task #: ")  # Generate data
#    date = input('Enter a date in YYYY-MM-DD format: ')
#    year, month, day = map(int, date.split('-'))
#    # date1 = datetime.date(year, month, day)
#    name = input("Enter name: ")
#    category = input("Enter category: ")
#
#    print(task, date, name, category)  # Prints the line of user data
#
#    input1 = input(
#     "Append to inventory list? Y/N  || anything else to exit")  # Asks user to append the data to the output file.
#
#    if input1 == "Y" or input1 == "y":
#        with open('LIST.csv', 'a', newline='') as fd:  # Pull up a separate csv to write to, an output for collected data
#
#           fd.write = csv.writer(csv_file, delimiter = ',')
#           w.writerow([task, date, name, category])  # Need to write the previously pulled up line to new csv
#           print("INVENTORY UPDATED")
#           user_input = input('Do you want to add one more entry: Enter [Y/N]')
#           if user_input.lower() == 'y':
#               my_function()
#           else:
#               exit()
# my_function()


# import csv

#
# def manualentry():
#
#     #Open csv file at start
#     outfile = open('INV.csv', 'a', newline='')
#     w = csv.writer(outfile)  # Need to write the user input to the .csv file.
#
#     #Everything wrapped in a while True loop, you can change to any loop accordingly
#     while True:
#         task = input("Enter task #: ")  # Generate data
#         date = input('Enter a date in YYYY-MM-DD format: ')
#         year, month, day = map(int, date.split('-'))
#         # date1 = datetime.date(year, month, day    QW2SAFRETGXDBFVCDSEWQA  )
#         name = input("Enter name: ")
#         category = input("Enter category: ")
#         print(task, date, name, category)  # Prints the line of user data
#         input4 = input("Append to inventory list? Y/N")  # Asks user to append the data to the output file.
#         if input4.lower() == "y":
#             w.writerow([(task, date, name, category)])  # <-This is the portion that seems to fall apart.
#             print("INVENTORY UPDATED")
#         if input4.lower() == "n":
#             print("SKIPPING. RESTARTING....")
#         #If you see stop, stop writing, close the file and exit
#         if input4.lower() == 'stop':
#             print('Not writing anymore! Stopping')
#             outfile.close()
#             exit()
#         else:
#             print("Invalid entry restarting program.")
# manualentry()

# import csv
# rows = []
# with open("INV.csv", 'r') as file:
#     csvreader = csv.reader(file)
#     header = next(csvreader)
#     for row in csvreader:
#         rows.append(row)
# print(header)
# print(rows)

from prettytable import prettytable
from prettytable import from_csv


#innen
# n = int(input("enter a n value:"))
# d = {}
#
# for i in range(n):
#     keys = input() # here i have taken keys as strings
#     values = int(input()) # here i have taken values as integers
#     d[keys] = values
# print(d)




import sys
import csv
import operator
import pandas as pd

def manualentry():

    #Open csv file at start
    outfile = open('INV.csv', 'a', newline='')
    w = csv.writer(outfile)  # Need to write the user input to the .csv file.

    #Everything wrapped in a while True loop, you can change to any loop accordingly
    while True:
        task = input("Enter task #: ")  # Generate data
        date = input('Enter a date in YYYY-MM-DD format: ')
        year, month, day = map(int, date.split('-'))
        name = input("Enter name: ")
        category = input("Enter category: ")
        print(task, date, name, category)  # Prints the line of user data
        input4 = input("Append to inventory list? Y/N")  # Asks user to append the data to the output file.
        if input4.lower() == "y":
            w.writerow([(task, date, name, category)])
            print("INVENTORY UPDATED")
        if input4.lower() == "n":
            print("Nothing will be updated")
        print("This is the task list")
        with open('INV.csv', mode="r") as csv_file:
            reader = csv.reader(csv_file)

            for item in reader:
                print(item)
        print("What do you want to do with the list?")
        choice = input("""
                               A: Display list
                               B: Sort Ascending
                               C: Filter
                               D: Add 
                               E: Remove
        
                               Please enter your choice: """)
        if choice == "A" or choice == "a":
            # INV = pd.read_csv('INV.csv')
            # print(INV)
            with open('INV.csv', newline='') as f:
                reader = csv.reader(f)
                data = list(reader)
            print(data)
        if choice == "B" or choice == "b":
            with open('INV.csv', newline='') as f:
                reader = csv.reader(f)
                data = list(reader)
            print(data.sort())
        if choice == "C" or choice == "c":
            reader = csv.reader(open(r'INV.csv'), delimiter=' ')
            filtered = filter(lambda p: 'teme' == p[2], reader)
            csv.writer(open(r'INV.csv', 'w'), delimiter=' ').writerows(filtered)
        if choice == "D" or choice == "d":
            with open('INV.csv', 'a') as fd:
                fd.write(task)
        if choice == "E" or choice == "e":
            data = pd.read_csv('INV.csv')
            data.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')
    exit()

#df.to_csv('my_csv.csv', mode='a', header=False)

manualentry()






