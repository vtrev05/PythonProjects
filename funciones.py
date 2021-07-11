def mi_funcion(**niños):
    print("el mayor de todos es " + niños["apellido"])

mi_funcion(nombre = "Tobias", apellido = "harris")

x = lambda a, b : a * b
print(x(5, 6))

rango = range(10, 40, 2)
for valor in rango:
    print(rango)