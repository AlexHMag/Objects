class Perro(object):
    def __init__ (self):
        print("Estos son de la familia de los perros")

    def ladrar (self):
        print("GUAU GUAU")

    def gruñir (self):
        print("GRRR GRRR")

class Caniche(Perro):
    """
    def ladrar(self):
        print("guau guau guau")
    """
    def gruñir(self):
        print("grrrr grrrr grrrr")

class Pastor_Aleman(Perro):
    def ladrar(self):
        print("GuaUU! GuaUU!")

    def gruñir(self):
        print("Agrrrrr! Agrrrr!")

class Hibrido(Caniche, Pastor_Aleman):
    def ladrarx(self, veces):
        for cuantas in range(veces):
            super(Hibrido, self.ladrar())


Tommy = Pastor_Aleman()
Repro = Caniche()
Cucha = Hibrido()

Cucha.ladrarx(4) #El ladrido sera heredado del primero escrito y si se quitan todos sera el de Perro