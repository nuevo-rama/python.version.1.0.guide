class Options:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def showOptions(self):
        print(self._a)
        print(self._b)
        print(self._c)

    def selectOption(self, var):
        sel = True
        while sel == True:
            if var == self._a:
                print(self._a)
                print("Your option is: " + var)
                sel = False
            elif var == self._b:
                print(self._b)
                print("Your option is: " + var)
                sel = False
            elif var == self._c:
                print(self._c)
                print("Your option is: " + var)
                sel = False
            else:
                print("Your option is: " + var)
                print("No es una opción válida, vuelve a escribir una opción")
                var = reOption()

menu1 = Options('1', '2', '3')

#menu1.showOptions()

def reOption():
    var = input("""Select an option:
                        1. Home
                        2. About
                        3. Contact
                        """)
    return var

menu1.selectOption(reOption())
