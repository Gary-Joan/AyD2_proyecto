import abc

class Platillo(abc.ABC):#INTERFAZ DE PLATILLO

    @abc.abstractmethod
    def get_ingredientes(self):
        pass

class PlatilloA(Platillo):
    def __init__(self):
        self.Ingredientes = "Ingredientes de platillo A"    

    def get_ingredientes(self):
        return self.Ingredientes

class PlatilloB(Platillo):
    def __init__(self):
        self.Ingredientes = "Ingredientes de platillo B"    

    def get_ingredientes(self):
        return self.Ingredientes