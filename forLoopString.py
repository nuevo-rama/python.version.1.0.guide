# Ingresando una palabra y una letra
# Contar la cantidad de veces que aparece la letra ingresada en la palabra

word = input("Escribe una palabra: ")
letter = input("Ingresa una letra: ")
letterOk = letter.lower()

counter = 0

for x in word:
    if letterOk == x:
        counter = counter + 1

print (counter, "veces aparece la letra '", letter , "' en la palabra '", word, "'")
