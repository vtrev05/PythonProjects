
edad = int(input("dime tu edad "))
tipo_de_carnet = input("dime tu tipo de carnet (E estudiante / P pensionista / F familia numerosa / N nada): ")


if (edad < 35 and edad > 25 and tipo_de_carnet == "E") or \
        edad < 10 or \
        (edad > 65 and tipo_de_carnet == "P") or \
        (tipo_de_carnet == "F"):

    print("se te aplica el descuento")
else:
    print("No se te aplica descuento")
