class Listas1():

    def __init__(self):

        self.pedirNombre(self.pedirNumero())

    def pedirNumero(self):

        num = int(input("Ingrese el numero de elementos a guardar: "))

        print("La lista contendrá: ", num, " nombre/s")

        return num

    def pedirNombre(self, num):

        i = 0
        lista = []

        while i < num:

            lista.append(str(input("Ingrese el nombre a guardar: ")))
            print(f"Nombre {i}: ", lista[i], "\n")
            i = i + 1

        print(f"La lista creada es: \n{lista}")

        return lista


lista1 = Listas1()
print("Victor Suros")
