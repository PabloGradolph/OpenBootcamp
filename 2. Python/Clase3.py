from re import M


a = 5
print(id(a))
a = 6
print(id(a))
a = 5
print(id(a))

# Enteros, strings y tuplas son invariables.
# Trabajamos con listas y diccionarios que ya lo tienes.
diccionario = {'clave1':1, 'clave2':2, 'clave3':3, 'clave4':4}
elemento_viejo = diccionario.pop('clave4')
print(elemento_viejo)
# Con del no te devuelve el valor borrado.

# Conjuntos o mejor llamados sets.
lista = [1, 2, 3, 1, 2, 3]
conjunto = {1, 2, 3, 1, 2, 3}
print(lista)
print(conjunto) # En un conjunto los elementos no se pueden repetir.
par = {0, 2, 4, 6, 8}
impar = {1, 2, 3, 4, 5}
print(par | impar)# Unión
print(par & impar)# Intersección
print(par - impar)# Diferencia
print(par ^ impar)# Diferencia simétrica

# Con qué trabajamos en python
numeros = 5
cadenas = 'hola'
booleano = True
flotante = 5.5
listas = ['a', 'b', 'c']
diccionarios = {'clave': 'valor'}
conjuntos = {1, 2, 3, 4, 1, 2, 3, 4}
mitexto = 'hola, esto es un texto'
print(mitexto.capitalize)
print(mitexto.title)
print(mitexto.lower)
print(mitexto.upper)
print(mitexto.replace('a', 'o'))
print(mitexto.find('esto'))
print(mitexto.split())
print(mitexto.split(','))
# Podemos concatenar métodos
listaTexto = mitexto.split()
print(' '.join(listaTexto))
texto = '5'
print(texto.isnumeric())

# Ahora vemos los operadores que también los tienes. Apunto alguno si no lo he visto.
a = 21
b = 5
print(a // b)
print(a % b)

''' 
Te faltan por ver:
&=
|=
^=
<<=
>>=
'''