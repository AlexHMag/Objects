class Padre(object):
    def __init__(self, ojos, cejas):
        self.ojos = ojos
        self.cejas = cejas

class Madre(object):
    def __init__(self, manos, piernas):
        self.manos = manos
        self.piernas = piernas

class Hijo(Padre, Madre):
    def __init__(self, ojos, cejas, manos, piernas):
        Padre.__init__(self, ojos, cejas)
        Madre.__init__(self, manos, piernas)


Tomas = Hijo("Marrones", "Negras", 2, 2)
print(Tomas.ojos, Tomas.cejas, Tomas.manos, Tomas.piernas)