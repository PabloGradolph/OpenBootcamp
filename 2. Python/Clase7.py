# MÓDULOS: EJECUTANDO MÓDULOS COMO SCRIPTS. ÁMBITOS.

# Un módulo es un fichero con extensión .py
# Cuando ejecuto directamente sin importar, el módulo se llama __main__. Cuando importo si que toma el nombre del
# fichero.
# Un paquete es un directorio pero con un fichero dentro especial.
# Para buscar paquetes con funcionalidades interesantes pypi.org
# O mejor todavía buscar en un buscador normal.


import sys
import pprint # Este sirve para imprimir bonito.
import operaciones
from Operaciones import suma # Este es un paquete. Necesita el fichero __init__.py
# Si quieres hacer from paquete import * tenemos que meter la variable especial __all__ = ["lo que sea"] en __init__.py


def main():
    res = operaciones.suma(2, 2)
    res_resta = operaciones.resta(5, 3)
    print("Hola en main(): ", res, res_resta)

    print(operaciones.como_me_llamo())
    print(dir(operaciones))

    op = operaciones.Operador()
    print(op.multiplicacion(4, 2))

    pprint.pprint(sys.path)

    print(suma.suma(2, 2))

def prueba():
    globals()['variable'] = 7
    # Es lo mismo que escribir:
    # global variable
    # variable = 7
    valor = 5
    estado = False
    pprint.pprint(locals()) # Mostramos la tabla de símbolos en el ámbito local (dentro de la función)
    # globals es lo mismo pero del porgrama completo, a nivel global.

class Hola:

    def patata(self):
        print("toma")

def multi(a, b):
    return a * b

def div(a, b):
    return a / b


if __name__ == '__main__':
    main()
    pprint.pprint(globals()) # Ámbitos (globals y locals)
    # Reconoce lo que hay hasta ahí en nuestro programa.
    # Ejemplo de uso. globals() devuelve un diccionario.
    variable = 5
    print(variable)

    globals()['variable'] = 6
    print(variable)

    prueba()
    print(variable)

    h = Hola()
    globals()['h'].patata()