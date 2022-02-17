# Herencia, Encapsulamiento, Polimorfismo, Abstracion 

class Persona:
    nombre = ""
    apellido = ""
    genero = ""
    direccion = ""

    def comer(self):
        return "Funcion Comer de Persona"

    def correr(self):
        return "Funcion Correr de Persona"

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

    def __init__(self, nombre = "John", apellido = "Doe", genero = "M", direccion = ""):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.direccion = direccion


class Estudiante(Persona):

    estudios = ""

    def __init__(self, nombre = "John", apellido = "Doe", genero = "M", estudios = "Ninguno", direccion = ""):
        super().__init__(nombre, apellido, genero, direccion)
        self.estudios = estudios


persona_1 = Persona()
persona_1.nombre = "Luis"
persona_1.apellido = "Rodriguez"

persona_2 = Persona()
persona_2.nombre = "Katherine"
persona_2.apellido = "Krauss"

estudiante_1 = Estudiante()
estudiante_1.nombre = "Anyelina"
estudiante_1.apellido = "Cordoba"
estudiante_1.genero = "F"
estudiante_1.estudios = "Ingenieria Automotriz"
estudiante_1.direccion = "Av Maipu 3210"


estudiante_2 = Estudiante("Frank", "Lobo", "M", "Ingenieria Mecanica", "Av Copacavana 2901")

print(persona_1.nombre_completo())
print(persona_2.nombre_completo())
print(estudiante_1.nombre_completo(), estudiante_1.genero, estudiante_1.direccion)
print(estudiante_2.nombre_completo())
print(estudiante_2.genero)