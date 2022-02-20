# Ingresando una palabra y una letra
# Contar la cantidad de veces que aparece la letra ingresada en la palabra

def countOccurrences (word, letterOk):
    counter = 0
    for x in word:
        if letterOk == x:
            counter = counter + 1

    return counter

word = input("Escribe una palabra: ")
letter = input("Ingresa una letra: ")
letterOk = letter.lower()

res = countOccurrences(word, letterOk)

print (res, "veces aparece la letra '", letter , "' en la palabra '", word, "'")
