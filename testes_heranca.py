from abc import ABC, abstractclassmethod

class Figura(ABC):
    def __init__(self, cor):
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @abstractclassmethod
    def circunferencia(self):
        pass

class Circulo(Figura):
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.__raio = raio
    
    @property
    def raio(self):
        return self.__raio

    @raio.setter
    def raio(self, raio):
        self.__raio = raio

    def circunferencia(self):
        return 3.1415 * self.__raio * self.__raio

circulo_instance = Circulo('Azul', 10)
print(circulo_instance.cor)

# abaixo, nao funciona pq existe abstract method na flasse Figura
#figura_instance = Figura('Amarela')
#print(figura_instance.cor)
