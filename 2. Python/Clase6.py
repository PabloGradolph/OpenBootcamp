# ------------------------------------------------------
# CLASES Y OBJETOS
# ------------------------------------------------------

# Paradigma de programación: POO (Programación Orientada a Objetos)

# Objeto: Representación de algo del mundo real en un lenguaje de programación.
# Método: Todas las acciones que puede hacer ese objeto.
# Propiedades/Atributos: Algo que pertenece a ese objeto y que puede mutar.

class Dino:
    _encendido = False

    def enciende(self):
        # Self. estoy haceindo referencia a una variable de mi clase
        # Si no lo ponemos, creamos una nueva variable shadowing dentro solo de la funcion enciende
        self._encendido = True

    def apaga(self):
        self._encendido = False

    def isEncendido(self):
        return self._encendido


d = Dino()
print(d._encendido)
d._encendido = True # Esto no lo deberíamos hacer con una variable que empiece por _
print(d._encendido)
d.enciende()

d2 = Dino()
d2.enciende()
print(d2.isEncendido())
d2.apaga()
print(d2.isEncendido())

# ------------------------------------------------------
# HERENCIA
# ------------------------------------------------------


class Juguete:
    _encendido = False

    def __init__(self):
        print("Estoy en el constructor de la clase Juguete")

    def enciende(self):
        self._encendido = True

    def apaga(self):
        self._encendido = False

    def isEncendido(self):
        return self._encendido


class Potato(Juguete):
    def quitar_oreja(self):
        pass

    def poner_oreja(self):
        pass


class Dinosaurio(Potato, Juguete): # Hereda de las dos, la herencia tiene que ir en dicho orden
    def ver_escamas(self):
        pass


print()
print("HERENCIA:")
p = Dino()
p.enciende()
print(p.isEncendido())
p.apaga()
print(p.isEncendido())

# Podemos ver las funciones y atributos que hay en dicho objeto o clase
print(dir(p))

# ------------------------------------------------------
# CONSTRUCTOR Y DESTRUCTOR
# ------------------------------------------------------


class Tiranosaurio(Juguete):
    color = None
    nombre = None

    def __init__(self, nombre): # Contructor
        # Juguete.__init__(self) # Heredamos el constructor
        super().__init__() # Otra opción más común para heredar de la superior.
        print("Estoy en el constructor de la clase Tiranosaurio", nombre)
        self.color = "Verde"
        self.nombre = nombre

    def __del__(self):
        print("Estoy en el destructor de la clase", self.__class__)


p = Tiranosaurio("midinosaurio")
print(p.color)
print(p.nombre)


# ------------------------------------------------------
# CLASES ESTÁTICAS
# ------------------------------------------------------

# Comparten un mismo espacio de memoria
# No se suelen usar mucho


class Estatica:
    numero = 1

    def incrementa():
        Estatica.numero += 1


print()
print("ESTÁTICAS:")
Estatica.incrementa()
print(Estatica.numero)

Estatica.incrementa()
print(Estatica.numero)

Estatica.incrementa()
print(Estatica.numero)


# ------------------------------------------------------
# LAS CLASES EN PYTHON POR DEBAJO SON DICCIONARIOS
# ------------------------------------------------------

_encendido = False


def enciende():
    global _encendido
    print("INVOCO A ENCIENDE")
    _encendido = True


def apaga():
    global _encendido
    _encendido = False


def is_encendido():
    return _encendido


diccionario = {
    '_encendido': False,
    'enciende': enciende,
    'apaga': apaga
}

print()
print("DICCIONARIO:")
diccionario['enciende']()

# ------------------------------------------------------
# CLASES ABSTRACTAS
# ------------------------------------------------------

# NO PODEMOS INSTANCIAR UNA CLASE ABSTRACTA
# Una clase abstracta sirve para definir un conjunto de funciones comunes a otras clases.


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self): # Cualquier clase que herede de esta debe tener este método.
        pass

    def di_hola(self):
        print("Hola")

class Perro(Animal):
    def sonido(self):
        print("Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau")

print()
print("CLASE ABSTRACTA:")
p = Perro()
p.sonido()
g = Gato()
g.sonido()
p.di_hola()
g.di_hola()

# ------------------------------------------------------
# RELACIONES
# ------------------------------------------------------

# En el mundo de la POO hay dos tipos de relaciones:
# Relaciones is-a (HERENCIA)
# Relaciones has-a (COMPOSICIÓN)

# Este segundo tipo de relaciones (no se si se escriben así) quiere decir que una clase está compuesta por otras.


class Motor:
    tipo = "Diesel"

class Ventanas:
    cantidad = 5

    def cambiar_cantidad(self, cantidad):
        self.cantidad = cantidad

class Ruedas:
    cantidad = 5

class Carroceria:
    ventanas = Ventanas()
    ruedas = Ruedas()

class Coche:
    motor = Motor()
    carroceria = Carroceria()

print()
print("COMPOSICIÓN:")
c = Coche()
print("Motor es", c.motor.tipo)
print("Ventanas:", c.carroceria.ventanas.cantidad)
c.carroceria.ventanas.cambiar_cantidad(3)
print("Ventanas:", c.carroceria.ventanas.cantidad)

# ------------------------------------------------------
# EJEMPLO COMPOSICIÓN
# ------------------------------------------------------
class Provedores:
    id_provedor = 0
    nombre = "Nombre"

class Categorias:
    idcategoria = 0
    nombre = "Nombre"


class Productos:
    idproducto = 0
    categoria_producto = Categorias()
    precio = 0
    tamaño = 0
    tipo_producto = 0
    CIFProvedor = Provedores()

print()
print("EJEMPLO COMPOSICIÓN:")
p = Productos()
print(p.CIFProvedor.nombre)
print(p.categoria_producto.idcategoria)