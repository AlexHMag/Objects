class Diferencia(object):
    def over(self, a):
        if type(a) == int:
            print("Es un numero")
        elif type(a) == str:
            print("Es texto cabron....")
        elif type(a) == float:
            print("No me gustan las comas")
        else:
            print("Que coño?")

test = Diferencia()

test.over(69.3)

