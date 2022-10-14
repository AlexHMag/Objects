class Padre(object):
    def __init__ (self, age, tall):
        self.age = age
        self.tall = tall

class Hijo(Padre):
    def __init__(self, age, tall, bro):
        super().__init__(age, tall)
        self.bro = bro

Juan = Hijo(15, 168, 2)

print("Me llamo Juan y tengo " + str(Juan.bro) + " hermanos, " + str(Juan.age) + " años y mido " + str(Juan.tall))
