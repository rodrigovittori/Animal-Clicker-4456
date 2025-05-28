#pgzero

""" PACK DE ASSETS: https://kenney.nl/assets/animal-pack-redux

    CARPETA FONDOS KODLAND: https://drive.google.com/drive/folders/1lXNvCF8q-IJ886xrCZmNt0ap1ElwGEU7
    
    Packs fondos Kenney: 
    > https://kenney.nl/assets/background-elements
    > https://kenney.nl/assets/background-elements-redux
    
    Link a este archivo (en GitHub): 
    Link al historial (en GitHub):    https://github.com/rodrigovittori/Animal-Clicker-4456/commits/main/
    
    --------------------------------------------------------------------------
    
    [M8.L2] - Actividad Nº 2 - "Aumentar la puntuacion"
    Objetivo: Agregar condición de collide-point al Actor y animaciones
    
    Paso 1º) Creamos una variable que controle el multiplicador de click
             > (cuántos puntos sumamos al hacer click sobre nuestro Actor)
    Paso 2º) Modificamos on_mouse_down() para que SOLO aumente la puntuación cuando el click sea sobre el Personaje
    Paso 3º) Agregamos una pequeña animación al hacer click sobre el personaje
"""

WIDTH = 600  # Ancho de la ventana
HEIGHT = 400 # Altura de la ventana

TITLE = "Animal Clicker" # Título de la ventana de juego
FPS = 60 # Fotogramas por segundo

fondo = Actor("background", size=(WIDTH, HEIGHT))
animal = Actor("giraffe", (150, 250))

#VARIABLES
puntuacion = 0 # puntos actuales
click_mult = 1 # multiplicador del valor por click

def draw():
    fondo.draw()
    animal.draw()
    screen.draw.text(str(puntuacion), center = (150, 70), color = "white", fontsize = 96)

def on_mouse_down(button, pos):
    global puntuacion

    if (button == mouse.LEFT):
        if(animal.collidepoint(pos)): # Si el click fue sobre el PJ:
            puntuacion += click_mult

            # Animación:
            animal.y = 200
            animate(animal, tween = "bounce_end", duration = 0.5, y = 250)
            # https://pygame-zero.readthedocs.io/en/stable/builtins.html?highlight=animate#animate
            
            