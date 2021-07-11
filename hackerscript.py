import os


def main():
    open("PARA TI.txt", "a")                    #la w sirve para crear un txt en modo escritura (crea un archivo nuevo), r es modo lectura
    print(os.getlogin())                        # por lo que necesita que el arcvhivo esté ya creado y con a seguiríamos escribiendo encima del archivo.

if __name__ == "__main__":
    main()