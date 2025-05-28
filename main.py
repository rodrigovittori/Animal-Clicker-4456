#pgzero

""" PACK DE ASSETS: https://kenney.nl/assets/animal-pack-redux

    CARPETA FONDOS KODLAND: https://drive.google.com/drive/folders/1lXNvCF8q-IJ886xrCZmNt0ap1ElwGEU7
    
    Packs fondos Kenney: 
    > https://kenney.nl/assets/background-elements
    > https://kenney.nl/assets/background-elements-redux
    
    PACK BOTONES COMPLETO: https://kenney.nl/assets/ui-pack
    > COLLECIÓN UI COMPLETA:  https://kenney.nl/assets/series:UI%20Pack
    
    Link a este archivo (en GitHub):  https://github.com/rodrigovittori/Animal-Clicker-4456/blob/main/main.py
    Link al historial (en GitHub):    https://github.com/rodrigovittori/Animal-Clicker-4456/commits/main/
    
    --------------------------------------------------------------------------
    
    [M8.L2] - Actividad Nº 3 - "Añadiendo bonificaciones"
    Objetivo: Agregar botones de bonus, (sólo dibujarlos)

    Paso 1º) Crear Actores bonus_1 y bonus_2 así como sus valores :
             > {precio (int), potenciador (int), ya_activado (bool)} 

    Paso 2º) Modificar nuestro draw() para que los muestre por pantalla, así como el texto que explica su función
    
    NOTA: La lógica de activar los botones la programaremos en el próximo ejercicio (no hay que agregar collidepoint todavía)
    Extra: Crear un token personalizado para nuestro juego
"""

WIDTH = 600  # Ancho de la ventana
HEIGHT = 400 # Altura de la ventana

TITLE = "Animal Clicker" # Título de la ventana de juego
FPS = 60 # Fotogramas por segundo

# VARIABLES
puntuacion = 0 # puntos actuales
click_mult = 1 # multiplicador del valor por click
token = "⛏️" # ₽ ¢ ℂ


# OBJETOS / ACTORES:
fondo = Actor("background", size=(WIDTH, HEIGHT))
animal = Actor("giraffe", (150, 250))

bonus_1 = Actor("bonus", (450, 100))
bonus_1.precio = 15           # El costo en puntos para activarlo/mejorarlo
bonus_1.potenciador = 1       # La cant. de puntos extra que agrega cada 2 segundos
bonus_1.ya_activado = False   # atributo que registra si el bonus se ecnuentra activo

bonus_2 = Actor("bonus", (450, 200))
bonus_2.precio = 200          # El costo en puntos para activarlo/mejorarlo
bonus_2.potenciador = 15      # La cant. de puntos extra que agrega cada 2 segundos
bonus_2.ya_activado = False   # atributo que registra si el bonus se ecnuentra activo

# TAREA 7: Agregar bonus_3

##########################################################

def draw():
    fondo.draw()
    animal.draw()

    # To-do: Agregar control que chequee que el texto no se salga de la pantalla (ajusta vble fontsize) 
    screen.draw.text(str(puntuacion) + token, center = (150, 70), color = "white", fontsize = 96)

    # Dibujamos botones bonus:
    bonus_1.draw()
    screen.draw.text(("+" + str(bonus_1.potenciador) + " " + token + " cada 2 seg"), center = (bonus_1.x, bonus_1.y - 20), color = "black", fontsize = 20)
    screen.draw.text(("PRECIO: " + str(bonus_1.precio) + " " + token), center = (bonus_1.x, bonus_1.y + 10), color = "black", fontsize = 20)

    bonus_2.draw()
    screen.draw.text(("+" + str(bonus_2.potenciador) + " " + token + " cada 2 seg"), center = (bonus_2.x, bonus_2.y - 20), color = "black", fontsize = 20)
    screen.draw.text(("PRECIO: " + str(bonus_2.precio) + " " + token), center = (bonus_2.x, bonus_2.y + 10), color = "black", fontsize = 20)

    # TAREA 7: Agregar bonus_3


def on_mouse_down(button, pos):
    global puntuacion

    if (button == mouse.LEFT):
        puntuacion += 1