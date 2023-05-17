"""    ===========Ejercicio=========
Codifique en Python una clase que represente a un animal. Un animal tiene las siguientes 
características comunes:
• Nombre.
• Raza.
• Edad.
• Peso. Debe crear dos instancias u objetos de la clase Animal, cuyos objetos son un caballo y 
un león, con las siguientes características particulares:
Caballo: 
 Nombre Zeus, Edad 5 años, Raza Pura sangre, Peso 450 kg
León:
 Nombre Boulder, Edad 10 años, Raza Atlas, Peso 130 kg
"""
class Animal():
    def __init__(self, nombre, edad, raza, peso):
        
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso
    
    def mostrar_caracteristicas(self):
        print("Se mustran características particulares")

class Caballo(Animal):
    def mostrar_caracteristicas(self):
        print("Caballo: \r")
        print(dibujo[0], "\r")
        print(f"Nombre: {self.nombre} \nEdad: {self.edad} \nRaza: {self.raza} \nPeso: {self.peso} \n")

class Leon(Animal):
    def mostrar_caracteristicas(self):
        print("León: \r")
        print(dibujo[1], "\r") 
        print(f"Nombre: {self.nombre} \nEdad: {self.edad} \nRaza: {self.raza} \nPeso: {self.peso}")
        
dibujo = ['''
            .''
  ._.-.___.' (`\ 
 //(        ( `'   Art by Veronica Karlsson
'/ )\ ).__. ) 
' <' `\ ._/'\ 
   `   \     \       
''',
'''
   /";;:;;"\ 
 (:;/\,-,/\;;)
(:;{  d b  }:;)  Art by ldb
 (:;\__Y__/;;)-----------,,_
  ,..\  ,..\      ___/___)__`\ 
 (,,,)~(,,,)`-._##____________)
'''
    
]

anim_1 = Caballo("Zeus", "5 años", "Pura sangre", "450 Kg")

anim_2 = Leon("Boulder", "10 años", "Atlas", "130 Kg")

anim_1.mostrar_caracteristicas()
anim_2.mostrar_caracteristicas()