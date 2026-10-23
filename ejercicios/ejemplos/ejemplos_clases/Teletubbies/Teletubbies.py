# Diseñar e implementar en Python una clase que represente a un Teletubby, aplicando los conceptos fundamentales de la Programación Orientada a Objetos (POO): atributos de clase, atributos de instancia (públicos y privados), métodos de instancia y encapsulamiento.

class Teletubbies:
    saludo_oficial = "!!Tubby Abrazo¡¡"
    
    def __init__(self, nombre, color, antena, objeto_favorito):
        self.nombre = nombre
        self.color = color
        self.antena = antena
        self.objeto_favorito = objeto_favorito
        
        self.__nivel_hambre = 50
        self.__nivel_felicidad = 100
        
    
    def saludar(self):
        print(f"Soy {self.nombre}, mi color es {self.color}. Y la forma de mi antena es {self.antena}.")
    
    def jugar(self):
        print(f"{self.nombre} está jugando con su {self.objeto_favorito} y está disfrutando")
        self.__nivel_hambre += 20
        self.__nivel_felicidad += 10
        
    def comer_tubby_papilla(self):
        print(f"{self.nombre} está comiendo una tubby papilla")
        self.__nivel_hambre = 0
        self.__nivel_felicidad += 20
    
    def ver_estado(self):
        return print(f"{self.nombre} tiene una felicidad de: {self.__nivel_felicidad} y con una barra de hambre de {self.__nivel_hambre}")
    def __str__(self):
       return f"Mi teletubbie es: {self.nombre} de color {self.color} y de antena {self.antena}"

    @classmethod
    def saludo(cls):
        print(cls.saludo_oficial)