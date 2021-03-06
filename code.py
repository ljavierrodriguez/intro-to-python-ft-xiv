"""
    Tipos de Datos: String, Number, Boolean, Listas (Lists, Tuples, sets), Dict, None

    String: "", ''' ''', """ """

    Number: 1 -1 1.1

    Boolean: True o False

"""

# Comentario Simple

nombre_completo = "Luis Rodriguez"

numero = 23

activo = True

notas = [12, 14, 28, 19, 40] # list notas[2]

status = ('active', 'inactive', 'suspended', 'canceled') # status[2]

frutas = {'Fresas', 'Duraznos', 'Bananas', 'Peras', 'Manzanas'} 

user = None

persona = {
    "nombre": "Luis",
    "apellido": "Rodriguez"
}

persona["apellido"]


numero = 1 if 4 > 5 else 0 # ternario en python

print(numero)

nombre = "Luis"
apellido = "Rodriguez"

edad = 40

nombre_completo1 = nombre + " " + apellido + "Tiene " + str(edad) + " años."


nombre_completo2 = f"{nombre} {apellido}, Tiene {edad} años."

nombre_completo3 = "%s %s %s" % (nombre, apellido, edad)

print(nombre_completo3 + ", Tiene " + str(edad) + " años.")