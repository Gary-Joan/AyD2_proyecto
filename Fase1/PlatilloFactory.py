import abc
from Platillo import Platillo, PlatilloA, PlatilloB # IMPORTACION DE PLATILLOS Y LA INTERFAZ DE PLATILLOS

class PlatilloFactory(abc.ABC):  #INTERFAZ DE FACTORY
    
    @abc.abstractmethod
    def nuevo_platillo(self,nombre_platillo):
        pass

class PlatilloStore(PlatilloFactory): #IMPLEMENTACION DE FACTORY

    def nuevo_platillo(self,nombre_platillo=''):
        Platillos = dict(platilloA = PlatilloA(), platilloB = PlatilloB())
        return Platillos[nombre_platillo]

#SE CREA EL FACTORY
menu = PlatilloStore()

#OBJECTOS DE FACTORY
platillo = menu.nuevo_platillo('platilloA')
print(isinstance(platillo,PlatilloA))
print(platillo.get_ingredientes())

platillo2 = menu.nuevo_platillo('platilloB')
print(isinstance(platillo2,PlatilloB))
print(platillo2.get_ingredientes())
