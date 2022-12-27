# INTRODUCCIÓN A LA BIBLIOTECA ESTÁNDAR DE PYTHON Y FUNCIONES BUILT-IN

# Las funciones built-in son funciones que el intérprete ya nos inyecta para que nosotros ya las podamos utilizar.
# La biblioteca estándar de python: Python Standar Library en Google.

# Paradigma de la programación multihilo.
import _thread
import time

def hora_actual(nombre_thread, tiempo_de_espera):
    count = 0

    while count < 5:
        time.sleep(tiempo_de_espera)
        count += 1
        print(f"Hilo: {nombre_thread} - {time.ctime(time.time())}")

_thread.start_new_thread(hora_actual, ("thread_uno", 1))
_thread.start_new_thread(hora_actual, ("thread_dos", 3))
print("He disparado ya los hilos")

while True:
    pass

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# LOGGING
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import logging

logging.basicConfig(level=logging.INFO)
logging.debug("prueba de debug")
logging.info("Arrancando programa")
logging.warning("Hace calor")
logging.error("test")
logging.critical("adios")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MAP, FILTER AND REDUCE
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mi_funcion(x):
    if x % 2 == 0:
        return True

    return False

# Al llamar a filter la función pasada tiene que devolver True o False.
# True "lo mete en la lista" (luego tenemos que hacer una lista de la variable" y False no.
# Extrae los valores de la lista que cumplen con ese valor
resultado = filter(mi_funcion, numeros)
print(list(resultado))

resultado = filter(lambda x: x % 2 == 0, numeros)
print(list(resultado))

# MAP implementa una función a todos los elementos de un iterable
def cuadrado(x):
    return x * x

resultado = map(cuadrado, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(resultado))

resultado = map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(resultado))

# Ahora hay que importar reduce
from functools import reduce

# reduce nos quiere generar un único resultado a partir de una lista.
# Las funciones con reduce necesitan dos parámetros.
def suma(a, b):
    print(f"a={a}, b={b}")
    return a + b

res = reduce(suma, [1, 2, 3, 4, 5])
print(res)

res = reduce(lambda a,b: a + b, [1, 2, 3, 4, 5])
print(res)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ZIP
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Zip devuelve una lista de tuplas combinando iterables
cursos = ['Java', 'Python', 'Git']
asistentes = [15, 20, 4]
demo = zip(cursos, asistentes)
print(list(demo))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ALL y ANY
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Sirven para verificar que todas o alguna de las condiciones de una lista se cumplan
listaA = [1 == 1, 2 == 2, 3 == 4]
res = any(listaA)
print(res)
res = all(listaA)
print(res)

# all = and and and and
# any = or or or or

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ROUND, MIN, POW, MAX, SORTED
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
a = 5.5
b = 5.4
c = 5.6
print(round(a))
print(round(b))
print(round(c))

print(min(2, 3, 4, 5, 9, 3, 1))
print(max(2, 3, 4, 5, 9, 3, 1))
print(pow(2, 4))

lista = ['z', 'c', 'd', 'a']
ordenada = sorted(lista, reverse=True, key=lambda x: str(x).startswith('a'))
print(ordenada)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# INPUT Y GETPASS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from getpass import getpass

user = input("username: ")
password = getpass("password: ")

# En pycharm salta pero si lo ejecutas en consola lo podemos hacer sin problema para que no se vea la contraseña
print(user, password)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

secreto = 50

valor = 0
while valor != secreto:
    valor = int(input("Introduce un número: "))

    if valor > secreto:
        print("Muy alto")
        continue

    if valor < secreto:
        print("Muy bajo")
        continue

print("¡Acertaste!")