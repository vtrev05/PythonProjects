from random import randint
import os

VIDA_INICIAL_PIKA = 80
VIDA_INICIAL_SQUIRTLE = 90

TAMANO_BARRA_DE_VIDA = 20

#Se pone en mayus para identificar rapidamente que son valores que no se van a tocar ni modificar. son constantes

vida_pika = VIDA_INICIAL_PIKA
vida_squirtle = VIDA_INICIAL_SQUIRTLE

while vida_pika > 0 and vida_squirtle > 0:
    #se desenvuelven los turnos de comabte

    #turno pika
    print("turno de pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        #bola voltio
        print("pikachu utilizó bola voltio")
        vida_squirtle -= 10
    else:
        print("pikachu utilizó onda trueno")
        vida_squirtle -= 11

    if vida_squirtle < 0:
        vida_squirtle = 0
    if vida_pika < 0:
        vida_pika = 0

    print("la vida de pika es: {}, la vida de squirtle es: {}".format(vida_pika, vida_squirtle))

    barras_de_vida_pika = int(vida_pika * TAMANO_BARRA_DE_VIDA / VIDA_INICIAL_PIKA)
    print("Pika:       [{}{}]".format("*" * barras_de_vida_pika, " " *(TAMANO_BARRA_DE_VIDA - barras_de_vida_pika)), vida_pika, VIDA_INICIAL_PIKA)

    barras_de_vida_squirtle = int(vida_squirtle * TAMANO_BARRA_DE_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("squirtle:   [{}{}]".format("*" * barras_de_vida_squirtle, " " * (TAMANO_BARRA_DE_VIDA - barras_de_vida_squirtle)), vida_squirtle, VIDA_INICIAL_SQUIRTLE)


    input("enter para continuar")
    os.system("cls")

    #turno de squirtle
    print("turno squirtle")

    ataque_squirtle = None
    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B":
      ataque_squirtle = input("¿Qué ataque quieres hacer? [P]lacaje, pistola [A]gua, [B]urbuja: ")

    if ataque_squirtle == "P":
        print("squirtle utilizó placaje")
        vida_pika -= 10
    elif ataque_squirtle == "A":
        print("squirtle utilizó pistola agua")
        vida_pika -= 12
    elif ataque_squirtle == "B":
        print("squirtle utilizó burbuja")
        vida_pika -= 9

    if vida_pika > vida_squirtle:
        print("Pikachu gana")
    else:
        print("Squirtle gana")

