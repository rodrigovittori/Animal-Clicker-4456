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
    
    [M8.L2] - Actividad Nº 5 - "Menú de inicio"
    Objetivo:  Crear condiciones para un menú: Actores, lógica y comprobación de clicks

    Paso 1º) Crear una variable global que contenga el estado actual del juego (modo_actual) 
    Paso 2º) Crear actores para los botones del menú (botón Jugar)
    Paso 3º) Modificar nuestro draw() para que muestre los botones de nuestro menú
    Paso 4º) Implementar la lógica (en on_mouse_down) para que al clickear el botón "Jugar", pasemos al modo "juego"
    
    Extra: agregar "cheat" para volver a la pantalla del menu ppal
"""

WIDTH = 600  # Ancho de la ventana
HEIGHT = 400 # Altura de la ventana

TITLE = "Animal Clicker" # Título de la ventana de juego
FPS = 60 # Fotogramas por segundo

# VARIABLES
puntuacion = 0 # puntos actuales
click_mult = 1 # multiplicador del valor por click
token = "⛏️" # ₽ ¢ ℂ
modo_actual = "menu" # Estados: "menu" / "juego" (prox. "tienda" y "coleccion")

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

boton_jugar = Actor("play", (300, 100))

# TAREA 11 (HOMEWORK 2/2): Agregar los botones de la tienda y nuestra colección de skins

##########################################################

""" #####################
   # FUNCIONES PROPIAS #
  ##################### """

def el_bonus_1():
    global puntuacion
    puntuacion += bonus_1.potenciador

def el_bonus_2():
    global puntuacion
    puntuacion += bonus_2.potenciador

# TAREA 7: Agregar función "el_bonus_3()"

""" ####################
   # FUNCIONES PGZERO #
  #################### """

def draw():

    if (modo_actual == "menu"):
        fondo.draw()
        boton_jugar.draw()
        
        # TAREA 11 (HOMEWORK 2/2): Agregar los botones de la tienda y nuestra colección de skins
    
    elif (modo_actual == "juego"):
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
        # TAREA 10 (HOMEWORK 1/2): Agregar el botón de "cerrar" / "volver al menú"


def on_mouse_down(button, pos):
    global puntuacion, modo_actual

    if (button == mouse.LEFT):

        if (modo_actual == "menu"):
            if (boton_jugar.collidepoint(pos)): # Si el click fue sobre el boton "Jugar"
                modo_actual = "juego"

        elif (modo_actual == "juego"):
            if (animal.collidepoint(pos)):
                # Si el click fue sobre el PJ:
                puntuacion += click_mult
                # Animación
                animal.y = 200
                animate(animal, tween = "bounce_end", duration = 0.5, y = 250)
                # https://pygame-zero.readthedocs.io/en/stable/builtins.html?highlight=animate#animate
                
            elif (bonus_1.collidepoint(pos)): # Si el click fue sobre el botón de bonus # 1:
    
                if (puntuacion >= bonus_1.precio): # Chequeamos si tiene suficientes puntos para comprarlo:
    
                    puntuacion -= bonus_1.precio   # Restamos los puntos gastados para comprar el bonus
                    # TAREA 9: Cuando pidan aumentar el precio -> bonus_1.precio *= 2
    
                    # TAREA 8: Agregar animación al comprar el bonus
                    
                    if (bonus_1.ya_activado == False):    # Chequeamos que NO se haya activado antes
                        schedule_interval(el_bonus_1, 2)  # Programamos las llamadas reiteradas
                        bonus_1.ya_activado = True        # Lo marcamos como "activado"
    
                    else: # SI YA ESTABA ACTIVO
                        bonus_1.potenciador += 1           # Aumentamos los puntos que dá este bonus
                    #######################################################################################
                else:   # Si NO tiene suficientes puntos para comprarlo
                        
                        # EJEMPLO TAREA 8: Animación de "compra rechazada"
                        bonus_1.x = 445
                        animate(bonus_1, tween='bounce_end', duration=0.25, x=450)
                        bonus_1.x = 455
                        animate(bonus_1, tween='bounce_end', duration=0.25, x=450)
            ##############################################################################################
    
            elif (bonus_2.collidepoint(pos)): # Si el click fue sobre el botón de bonus # 2:
    
                if (puntuacion >= bonus_2.precio): # Chequeamos si tiene suficientes puntos para comprarlo:
    
                    puntuacion -= bonus_2.precio   # Restamos los puntos gastados para comprar el bonus
                    # TAREA 9: Cuando pidan aumentar el precio -> bonus_2.precio *= 2
    
                    # TAREA 8: Agregar animación al comprar el bonus
                    
                    if (bonus_2.ya_activado == False):    # Chequeamos que NO se haya activado antes
                        schedule_interval(el_bonus_2, 2)  # Programamos las llamadas reiteradas
                        bonus_2.ya_activado = True        # Lo marcamos como "activado"
    
                    else: # SI YA ESTABA ACTIVO
                        bonus_2.potenciador += 15         # Aumentamos los puntos que dá este bonus
                    #######################################################################################
                else:   # Si NO tiene suficientes puntos para comprarlo
                        
                        # EJEMPLO TAREA 8: Animación de "compra rechazada"
                        bonus_2.x = 445
                        animate(bonus_2, tween='bounce_end', duration=0.25, x=450)
                        bonus_2.x = 455
                        animate(bonus_2, tween='bounce_end', duration=0.25, x=450)      
            ##############################################################################################
    
            # TAREA 7: Agregar lógica del bonus_3
            # TAREA 10 (HOMEWORK 1/2): Agregar lógica para el botón de "cerrar" / "volver al menú"

# CHEATS:

def on_key_down(key):
    global puntuacion, modo_actual

    if keyboard.d:
        puntuacion += 500

    if keyboard.a:
        puntuacion -= 500

    if keyboard.q:
        modo_actual = "menu"