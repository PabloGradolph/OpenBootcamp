# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# GUI (INTERFACES DE USUARIO): TKINTER
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# TCL/tk es un lenguaje de programación que podemos usar a través de tkinter en python.
# Los componentes o widgets se ponen en contenedores (ventanas o ...)
import sys
import tkinter

# PON Y QUITA COMENTARIOS EN CADA SECCIÓN PARA QUE SE EJECUTE ESA PARTE.
window = tkinter.Tk()
print(type(window))
print(dir(window))

'''
# Tres tipos de geometrías:
label_saludo = tkinter.Label(window, text='Hola', bg='yellow', fg='blue')

# Geometría de pack
label_saludo.pack(ipadx=50, ipady=50, fill='x', expand=True, side='left')

label_adios = tkinter.Label(window, text='Adios', bg='red', fg='white')
label_adios.pack(ipadx=50, ipady=100, fill='both', expand=True, side='right')
'''

'''
# Geometría mediante un grid
# Es como una matriz con filas y columnas (rollo excel)
from tkinter import ttk # Para que el tkinter tenga más estilo

# (0,0) (1,0) (2,0)
# (0,1) (1,1) (2,1)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Label Entry (2,0)
# Label Entry (2,1)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# Username
username_label = ttk.Label(window, text='Username:')
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

username_entry = ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

# Password
password_label = ttk.Label(window, text='Password:')
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

password_entry = ttk.Entry(window, show='*')
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

# Button
login_button = ttk.Button(window, text='Login')
login_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)
'''

'''
# Geometría mediante place
# Posicionamiento exacto con coordenadas.

from tkinter import ttk
import random

colors = ['blue', 'red', 'yellow', 'purple', 'green', 'black']


#for x in range(0,10):
#   color = random.randint(0, len(colors))
#   color2 = random.randint(0, len(colors))
#   label = tkinter.Label(window, text='etiqueta', bg=colors[color], fg=colors[color2])
#   label.place(x=random.randint(0,100), y=random.randint(0,100))


label1 = tkinter.Label(window, text='Posicionamiento absoluto', bg='blue', fg='white')
label1.place(x=10, y=50)

label2 = tkinter.Label(window, text='Otro más', bg='red', fg='yellow')
label1.place(relx=0.10, rely=0.15, relwidth=0.5, anchor='ne')
'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# WIDGETS QUE PODEMOS USAR
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Trabajamos con grids que es lo más utilizado.
from tkinter import ttk # Para que el tkinter tenga más estilo

# (0,0) (1,0) (2,0)
# (0,1) (1,1) (2,1)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Label Entry (2,0)
# Label Entry (2,1)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Frames

'''
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

frame = ttk.Frame(window)
frame['relief'] = 'sunken'

label = ttk.Label(frame, text='hola')
label.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=50)

frame.grid(column=0, row=0, sticky=tkinter.W)

window.mainloop()
sys.exit(0)
'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# List box
'''
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

lista = ['Windows', 'macOS', 'Linux', 'MS DOS', 'AmigaOS', 'BeOS', 'OS/2']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=100, listvariable=lista_items)
listbox.grid(column=0, row=0, sticky=tkinter.W)

window.mainloop()
'''
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Radio Buton

'''
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

seleccionado = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text='Si', value='1', variable=seleccionado)
r2 = ttk.Radiobutton(window, text='No', value='2', variable=seleccionado)
r3 = ttk.Radiobutton(window, text='Quizá', value='3', variable=seleccionado)

r1.grid(column=0, row=0, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)

seleccionado2 = tkinter.StringVar()

rs1 = ttk.Radiobutton(window, text='Si2', value='1', variable=seleccionado2)
rs1.grid(column=1, row=0, pady=5, padx=5)

window.mainloop()
'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Check
'''
def mifuncion():
    print("clicado")


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

seleccionado = tkinter.StringVar()
checkbox = ttk.Checkbutton(window, text='acepto las condiciones', variable=seleccionado, command=mifuncion())
checkbox.grid(row=0, column=0)

window.mainloop()
'''

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# PARADIGMA DE LA PROGRAMACIÓN ORIENTADA A EVENTOS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Lista de eventos:
'''
window = tkinter.Tk()

def salir(event):
    print("Adios")
    window.quit()

def saludar(event):
    print("Han hecho click en saludar")

def saludar_doble_click(event):
    print("Han hecho DOBLE click en saludar")


boton = tkinter.Button(window, text='Haz click')
boton.pack()
boton.bind('<Button-1>', saludar)
boton.bind('<Double-1>', saludar_doble_click)

botonSalir = tkinter.Button(window, text='Salir')
botonSalir.pack()
botonSalir.bind('<Button-1>', salir)

window.mainloop()
'''