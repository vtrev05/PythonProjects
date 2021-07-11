 
#ejemplo:
texto_usuario = input("Introduzca un texto: ")
espacios = 0
puntos = 0
comas = 0

for letra in texto_usuario:
    if letra == " ":
        espacios += 1
    elif letra == ".":
        puntos += 1
    elif letra == ",":
        comas += 1

print("Espacios: {}, Puntos: {}, Comas: {}".format(espacios, puntos, comas))