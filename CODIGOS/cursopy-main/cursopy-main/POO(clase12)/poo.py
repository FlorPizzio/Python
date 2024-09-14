class Animal:
    def comer(self):
        print("Como muchas veces el dias")
    def dormir(self):
        print("Duermo muchas horas")

class Perro(Animal):
    def sonido(self):
        print("Puedo ladrar")

#llamada al programa principal
print("----Herencias en python----")
print("Clase padre, soy un Animal")

Animal_definicion = Animal()
Animal_definicion.comer()
Animal_definicion.dormir()

print("-----Clase hija, soy un Perro-----")
Perro_definicion = Perro()
Perro_definicion.comer()
Perro_definicion.dormir()
