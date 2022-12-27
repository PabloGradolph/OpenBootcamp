# Control de flujo en un programa
a = 6
b = 6

# > Mayor
# >= Mayor o igual
# == Exáctamente igual
# <= Menor o igual
# < Menor

resultado = a < b
print(resultado)

if a == b:
    print(f'{a} = {b}')

# Switches
# La parlabra reservada es match

valor = 2

match valor:
    case 1:
        print("Valor es 1")
    case 2:
        print("Valor es 2")
    case 3:
        print("Valor es 3")

# Hay un else en los bucles for.
lista = ["hola", '', 'adios']

for palabra in lista:
    if palabra == 'mensaje':
        print("Encuentro la palabra mensaje")
        break
# Para que salte el else del for no se puede romper el bucle.
else:
    print("No encuentro nada")
