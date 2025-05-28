#pgzero

""" [M8.L2] - Actividad Nº 1 - "Clicker Animal"
    Objetivo: Crear ventana del juego

    PACK DE ASSETS: https://kenney.nl/assets/animal-pack-redux
    FONDOS KODLAND: https://drive.google.com/drive/folders/1lXNvCF8q-IJ886xrCZmNt0ap1ElwGEU7
    
    Link a este archivo (en GitHub): 
    Link al historial (en GitHub):    https://github.com/rodrigovittori/Animal-Clicker-4456/commits/main/

    Paso 1º) #pgzero
    Paso 2º) Ancho y alto de la ventana (WIDTH y HEIGHT)
    Paso 3º) Título (TITLE) y FPS
    Paso 4º) Crear Actor "Fondo" con modelo "background.jpg"
    Paso 5º) Crear Actor "Animal" con modelo de Jirafa (giraffe.png) 
    Paso 6º) Dibujar los elementos en pantalla ( draw() )
    Paso 7º) Crear una variable "puntuacion" para registrar los clicks
    Paso 8º) Agregar el método on_mouse_down(button, pos)
    Paso 9º) Agregamos una condición en on_mouse_down() para contar los clicks
    Paso 10) Agregamos un screen.draw.text para mostrar la puntuación
"""

WIDTH = 600  # Ancho de la ventana
HEIGHT = 400 # Altura de la ventana

TITLE = "Animal Clicker" # Título de la ventana de juego
FPS = 60 # Fotogramas por segundo

fondo = Actor("background", size=(WIDTH, HEIGHT))
animal = Actor("giraffe", (150, 250))

#VARIABLES
puntuacion = 0

def draw():
    fondo.draw()
    animal.draw()
    screen.draw.text(str(puntuacion), center = (150, 70), color = "white", fontsize = 96)

def on_mouse_down(button, pos):
    global puntuacion

    if (button == mouse.LEFT):
        puntuacion += 1