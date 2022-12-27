# INPUT / OUTPUT EN PYTHON

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# FORMATEO DE CADENAS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Forma mala/atnigüa
numero = 511
texto = "quijote"
otromas = 1.2

print("El numero es %d y el texto es %s y tiene %f" % (numero, texto, otromas))
print("Valor flotante: %.1f" % otromas) # Después del punto introducimos el número de decimales que queremos.

# Forma un poco más moderna a partir de Python 2.6
print("El número es {} y el texto es {} y tiene {}"
      .format(numero, texto, otromas))
print("El número es {1} y el texto es {0} y tiene {2}"
      .format(numero, texto, otromas))
print("El número es {n1} y el texto es {texto} y tiene {otromas}"
      .format(n1=numero, texto=texto, otromas=otromas))

# Mejor forma a partir de Python 3.6
print(f"El numero es {numero} y el texto es {texto.upper()} y tiene {otromas}")

def suma(a, b):
    return a + b

# Pueden implementar directamente funciones.
print(f"El numero es {suma(numero,numero)} y el texto es {texto.upper()} y tiene {otromas}")


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CONVERSIÓN A CADENAS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

num = 511
print(type(num))

numtxt = str(num)
print(type(numtxt))

# repr para generar salidas de depuración y desarrollo
print(repr(num))

class Juguete:
    nomre = ""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # Para imprimir por pantalla el objeto que seleccionamos
    # Implicitamente hace un str(objeto)
    # Salidas informales
    def __str__(self):
        return f"Mi nombre es {self.nombre} y mi precio es {self.precio}"

    # Salidas técnicas de depuración y desarrollo
    # Representación
    def __repr__(self):
        return f"Potato({self.nombre},{self.precio})"

    # Si una clase no tiene str y si repr al imprimir se ejecutará repr
    # Al revés no pasa


j1 = Juguete("Potato", 10.5)
print(j1)

demo = j1
print(type(demo))
demo = str(j1)
print(type(demo))
print(demo)

print(repr(j1))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MÉTODOS EN CADENAS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import pprint
pprint.pprint(dir(''))

cadena = "en un lugar de la manchA"
numero = "5"
print(cadena.title())
print(cadena.count('a'))
print(cadena.lower().count('a'))
print(cadena.isdigit())
print(numero.isdigit())
print(numero.isalnum()) #Alfanumérico
print(numero.isalpha()) #Alfabético

cadena = "en un lugar de la manchA      "
print(cadena)
print(cadena.strip())
print(cadena.lstrip())
print(cadena.rstrip())
print(cadena.split())
print(cadena.startswith("en"))
print(cadena.endswith("en"))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# FICHEROS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# r: lectura
# a: append
# w: escritura
# x: create

# t: texto
# b: binary

# +



def escribe(fichero, datos):
    f = open(fichero, "w")

    for linea in datos:
        if not linea.endswith('\n'):
            linea += '\n'

        f.write(linea)

    f.close()

lista = [
    'una linea',
    'dos lineas\n',
    'tres lineas'
]

escribe('mifichero.txt', lista)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# SERIALIZACIÓN DE DATOS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Guardar datos en un fichero binario de forma que los puedo recuperar posteriormente.

import pickle

class Juguetes:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def getNombre(self):
        return self.nombre

j1 = Juguetes("Potato", 10.5)
print(j1.getNombre())

# Serializamos los datos del objeto
f = open('datos.bin', 'wb')
pickle.dump(j1, f)
f.close()

# Quiero recuperar esos datos
f = open('datos.bin', 'rb')
potato = pickle.load(f)
f.close()

print(type(potato))
print(potato.getNombre(), 'precio: ', potato.precio)

'''
class Estado:
    players = Players()
    status = Status()
    life_remaining = 12
    armor = False

f = open('gamestatus.dat', 'rb')
e = pickle.dumps(f, e)
f.close()
'''