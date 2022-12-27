#------------------------------------------------------
# DEFINICIÓN Y USO DE FUNCIONES
#------------------------------------------------------

# Las funciones son una manera de escribir código reutilizable.
# También permiten simplificar el código.
# Las funciones deben y sólo deben realizar una tarea concreta.
# El nombre de las funciones tienen que ser acordes a su tarea.

# Antes de poder utilizar una función, el intérprete debe haberla leído previamente.
# Primero las definimos y luego las invocamos.

def nombre():
    print("Nombre")

print("Antes")
nombre()
print("Después")

# Función con parámetros
def mi_funcion(nombre):
    print("Hola", nombre)

print()
mi_funcion("Pablo")

def sum(a, b):
    return a + b

resultado = sum(4, 5)
print()
print(resultado)

# Función dentro de funciones
def matematicas(a, b):
    def suma(a, b):
        print(a + b)
    
    def resta(a, b):
        print(a - b)
    
    suma(a, b)
    resta(a, b)

print()
matematicas(5, 3)

#------------------------------------------------------
# VARIABLE SHADOWING
#------------------------------------------------------

hoyHace = 12.0
def temperatura():
    hoyHace = 6.0
    print("La temperatura es de", hoyHace)

temperatura()
print(hoyHace)

# Podemos declarar la variable global
hoyHace = 12.0
def temperaturas():
    global hoyHace
    hoyHace = 6.0
    print("La temperatura es de", hoyHace)

temperaturas()
print(hoyHace)

#------------------------------------------------------
# Parámetros opcionales o por defecto
#------------------------------------------------------

def mi_nombre(nombre = "Juan"):
    print("Hola", nombre)

print()
mi_nombre() # Toma el que viene en la variable
mi_nombre("Pablo") # Toma el que se pasa por valor

def sumatorio(a=1, b=5, c=3):
    print(a + b + c)

print()
sumatorio() # Valores por defecto
sumatorio(3) # Se cambia el primero
sumatorio(1, 1, 1) # Cambiamos todos
sumatorio(c = 9) # Escogemos cual cambiar

#------------------------------------------------------
# Parámetros variables
#------------------------------------------------------

def sumaton(*args):
    resultado = 0
    print(args)

    for arg in args:
        resultado += arg
    
    print(resultado)

print()
sumaton(1, 2, 3, 4, 5, 6) # Se convierte en una tupla

def sums(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, "=", value)
    
    if 'coche' in kwargs and kwargs['coche'] == 'rojo':
        print("Tu coche es rojo")

print()
sums(vivienda="piso", coche="rojo") # Se convierte en diccionario

#------------------------------------------------------
# FUNCIONES SIN PRINTS
#------------------------------------------------------

# En general las funciones no usan prints dentro de ellas, sino que retornan valores
def resta(a, b):
    return a - b

print()
print(resta(2, 1))

def operaciones(a, b):
    return a + b, a - b, a * b, a / b

retornado = operaciones(2, 4) # Se convierte en tupla
print(retornado)
print(retornado[0])
# Otra forma
print()
suma, rest, multi, divi = operaciones(2, 4)
print(suma)
print(rest)
print(multi)
print(divi)

def sumador(**kwargs):
    inicial = kwargs['inicial'] if 'inicial' in kwargs else 0
    final = kwargs['final'] if 'final' in kwargs else 0 # Se llama operador ternario en python

    resultado = 0
    for i in range(inicial, final + 1):
        resultado += 1
    
    return resultado

print()
print(sumador())
print(sumador(inicial=15))
print(sumador(inicial=15, final=30))

#------------------------------------------------------
# FUNCIONES ANÓNIMAS O LAMBDA
#------------------------------------------------------

# Se utilizan para hacer funciones muy simples

print()
anonima = lambda nombre, nombre2: print('Hola', nombre, 'Adios', nombre2)
anonima("Pablo", "Juan")

sumatoria = lambda x: x+x
print(sumatoria(2))