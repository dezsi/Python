import pandas
import pandas as pd


# 1.)
# dictionar_date = {
#     "masini": ['Dacia', 'Volvo', 'Renault'],
#     "culoare": [ 'rosu', 'alb', 'verde']
# }

# variabila = pd.DataFrame(dictionar_date)
# print(variabila)

# # 2.)
# masini = ['Dacia', 'Volvo', 'Renault']
# variabila = pd.Series(masini)
# print(variabila[0])

# 3.)
# masini = ['Dacia', 'Volvo', 'Renault']
# variabila = pd.Series(masini, index= ["x", "y", "z"])
# # print(variabila)
# print(variabila["x"])

# 4.)
# masini = {"x": "Dacia", "y": "Volvo", "z": "Renault"}
# variabila = pd.Series(masini)
# print(variabila)

# 5.)
# masini = {"x": "Dacia", "y": "Volvo", "z": "Renault"}
# variabila = pd.Series(masini, index = ["y", "z"])
# print(variabila)

# 6.)
# dictionar_date = {
#     "masini": ['Dacia', 'Volvo', 'Renault'],
#     "culoare": [ 'rosu', 'alb', 'verde']
# }
# variabila = pd.DataFrame(dictionar_date)
# print(variabila.loc[[0, 1]])  # row or variabila.loc[0]

#7.)
# dictionar_date = {
#     "masini": ['Dacia', 'Volvo', 'Renault'],
#     "culoare": [ 'rosu', 'alb', 'verde']
# }
# variabila = pd.DataFrame(dictionar_date, index = ["producator1", "producator2", " producator3"])
# # print(variabila.loc[[0, 1]])  # row or variabila.loc[0]
# # print(variabila)
# # print(variabilaloc["producator1"])
# # print(variabila.loc[0])
# # print(variabila.loc[["producator1", "producator2"]])

data = {
  "producator1": {
    "masini": "Dacia",
    "culoare": "rosu"
  },
  "producator2": {
    "masina": "volvo",
    "culoare": "alb"
  },
  "producator3": {
    "masina": "renault",
    "culoare": "verde"
  }
}

# variabila1 = pd.DataFrame(data)
# variabila1 = pd.read_json('data.json')
# url = 'https://api.exchangerate-api.com/v4/latest/USD'
# variabila1 = pd.read_json(url)
# print(variabila1)

variabila1 = pd.DataFrame(data)
fisier = variabila1.to_csv("data.cs")

