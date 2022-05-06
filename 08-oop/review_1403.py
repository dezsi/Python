class ClasaMea:

    gamma = 0   # atribut/ variabila de clasa

    def __init__(self):  # constructor
        self.alpha = 1   # variabila de instance
        self.__delta = 3 # variabila de instanta privata

obj = ClasaMea()         # instantiere a clasei ClasaMea
obj.beta = 2             # variabila de instanta si poate exista doar in interiorul obj

print(obj._dict__)       #