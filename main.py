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
    
    [M8.L3] - Actividad # 2 - "Compra de skins"
    Objetivo: Poder comprar y cambiar las skins del personaje

    Paso 1º) En tienda y en Coleccion queremos poder acceder a click_mult,
             así que lo marcamos como global en on_mouse_down()

    Paso 2º) Crear las listas "coleccion_completa" y "coleccion_skins"
    
    Paso 3º) Implementar compra de skins
            > Verificar que tenga suficientes créditos
            > Verificar que no la haya desbloqueado todavía
            > Agregar la skin comprada a mi colección
            > Actualizar la skin y el multiplicador tras la compra
            
    Paso 4º) Modificar draw para que se ajuste a cualquier cantidad de skins

    EXTRA: Agregar un método que ajuste el tamaño de la puntuación en pantalla
"""

WIDTH = 600  # Ancho de la ventana
HEIGHT = 400 # Altura de la ventana

TITLE = "Animal Clicker" # Título de la ventana de juego
FPS = 60 # Fotogramas por segundo

# VARIABLES
puntuacion = 0 # puntos actuales
click_mult = 1 # multiplicador del valor por click
token = "⛏️" # ₽ ¢ ℂ
modo_actual = "menu" # Estados: "menu" / "juego" / "tienda" y "coleccion"
tam_fuente_punt = 96 # Altura en píxeles del indicador de puntuacion

# OBJETOS / ACTORES:
fondo = Actor("background", size=(WIDTH, HEIGHT))
animal = Actor("giraffe", (150, 250))

# SKINS
cocodrilo = Actor("crocodile", (120, 200))
cocodrilo.precio = 500        # El costo en puntos para desbloquearlo
cocodrilo.mult = 2            # La cant. de puntos que nos otorga por cada click

hipopotamo = Actor("hippo", (300, 200))
hipopotamo.precio = 2500       # El costo en puntos para desbloquearlo
hipopotamo.mult = 3            # La cant. de puntos que nos otorga por cada click

# TAREA 4: Agregar otro animal (morsa)

bonus_1 = Actor("bonus", (450, 100))
bonus_1.precio = 15           # El costo en puntos para activarlo/mejorarlo
bonus_1.potenciador = 1       # La cant. de puntos extra que agrega cada 2 segundos
bonus_1.ya_activado = False   # atributo que registra si el bonus se ecnuentra activo

bonus_2 = Actor("bonus", (450, 200))
bonus_2.precio = 200          # El costo en puntos para activarlo/mejorarlo
bonus_2.potenciador = 15      # La cant. de puntos extra que agrega cada 2 segundos
bonus_2.ya_activado = False   # atributo que registra si el bonus se ecnuentra activo

bonus_3 = Actor("bonus", (450, 300))
bonus_3.precio = 600          # El costo en puntos para activarlo/mejorarlo
bonus_3.potenciador = 50      # La cant. de puntos extra que agrega cada 2 segundos
bonus_3.ya_activado = False   # atributo que registra si el bonus se ecnuentra activo

boton_jugar = Actor("play", (300, 100))
boton_tienda = Actor("tienda", (300, 200))
boton_coleccion = Actor("coleccion", (300, 300))

boton_cerrar = Actor("cross", (WIDTH - 30, 30))

# Listas skins
coleccion_skins = []          # lista de skins desbloqueadas/compradas

coleccion_completa = []       # lista que contiene todas las skins desbloqueables por el jugador
coleccion_completa.append(cocodrilo)
coleccion_completa.append(hipopotamo)
# TAREA 4: Agregar otro animal (morsa)

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

def el_bonus_3():
    global puntuacion
    puntuacion += bonus_3.potenciador

def actualizar_tam_fuente_punt():
  global tam_fuente_punt

  # Ajustar el tamaño de la fuente según el tamaño de la puntuación
  if puntuacion < 1000:
    tam_fuente_punt = 96
      
  elif puntuacion < 10000:
    tam_fuente_punt = 72

  elif puntuacion < 100000:
      tam_fuente_punt = 48

  else:
    tam_fuente_punt = 32

""" ####################
   # FUNCIONES PGZERO #
  #################### """

def draw():

    if (modo_actual == "menu"):
        fondo.draw()
        boton_jugar.draw()
        boton_tienda.draw()
        boton_coleccion.draw()

    elif (modo_actual == "tienda"):
        fondo.draw()

        # Si ya desbloqueamos TODAS las skins:
        if (set(coleccion_skins) == set(coleccion_completa)):
            screen.draw.text("¡FELICIDADES!", center=(WIDTH/2, HEIGHT/3), color = "white", background = "black" , fontsize = 42)
            screen.draw.text("Has adquirido todas las skins", center=(WIDTH/2, HEIGHT/3*2), color = "white", background = "black" , fontsize = 32)

        else:
            for skin in coleccion_completa:
                if skin not in coleccion_skins: # Si todavía NO la hemos adquirido
                    skin.draw()
                    screen.draw.text((str(skin.precio) + token), center=(skin.x, 300), color = "white" , fontsize = 36)

        # NOTA: Ponemos acá la puntuación porque no la queremos mostrar cuando el jugador ya haya desbloqueado todo
        screen.draw.text((str(puntuacion) + token), center=(150, 70), color="white", fontsize = tam_fuente_punt)
        
        boton_cerrar.draw()
    
    elif (modo_actual == "juego"):
        fondo.draw()
        animal.draw()
    
        screen.draw.text(str(puntuacion) + token, center = (150, 70), color = "white", fontsize = tam_fuente_punt)
    
        # Dibujamos botones bonus:
        bonus_1.draw()
        screen.draw.text(("+" + str(bonus_1.potenciador) + " " + token + " cada 2 seg"), center = (bonus_1.x, bonus_1.y - 20), color = "black", fontsize = 20)
        screen.draw.text(("PRECIO: " + str(bonus_1.precio) + " " + token), center = (bonus_1.x, bonus_1.y + 10), color = "black", fontsize = 20)
    
        bonus_2.draw()
        screen.draw.text(("+" + str(bonus_2.potenciador) + " " + token + " cada 2 seg"), center = (bonus_2.x, bonus_2.y - 20), color = "black", fontsize = 20)
        screen.draw.text(("PRECIO: " + str(bonus_2.precio) + " " + token), center = (bonus_2.x, bonus_2.y + 10), color = "black", fontsize = 20)
    
        bonus_3.draw()
        screen.draw.text(("+" + str(bonus_3.potenciador) + " " + token + " cada 2 seg"), center = (bonus_3.x, bonus_3.y - 20), color = "black", fontsize = 20)
        screen.draw.text(("PRECIO: " + str(bonus_3.precio) + " " + token), center = (bonus_3.x, bonus_3.y + 10), color = "black", fontsize = 20)

        boton_cerrar.draw()

def on_mouse_down(button, pos):
    global puntuacion, modo_actual, click_mult

    if (button == mouse.LEFT):
        actualizar_tam_fuente_punt()

        if (modo_actual == "menu"):
            if (boton_jugar.collidepoint(pos)): # Si el click fue sobre el boton "Jugar"
                modo_actual = "juego"

            elif (boton_tienda.collidepoint(pos)): # Si el click fue sobre el boton "Tienda"
                modo_actual = "tienda"

            # Tarea 3: Agregar lógica de modo "coleccion"

        elif (modo_actual == "tienda"):
            if (boton_cerrar.collidepoint(pos)):
                modo_actual = "menu"

            for skin in coleccion_completa:
                if ( ( skin.collidepoint(pos) )    and    # Si le doy click a una skin 
                     (skin not in coleccion_skins) and    # Y esa skin NO la tengo desbloqueada
                     ( puntuacion >= skin.precio)     ):  # Y tengo suficientes créditos/tokens

                    puntuacion -= skin.precio             # Restamos los créditos para comprar
                    animal.image = skin.image             # Cambiamos la skin de nuestro PJ
                    click_mult = skin.mult                # Actualizamos el mult de click
                    coleccion_skins.append(skin)          # Agrego la skin comprada a mi lista

                else: # Si NO lo puedo comprar:
                    temp_x = skin.x
                    skin.x = temp_x - 10
                    animate(skin, tween="bounce_start", duration = 0.25, x = temp_x)
                    skin.x = temp_x + 10
                    animate(skin, tween="bounce_end", duration = 0.25, x = temp_x)
                    skin.x = temp_x

                    # NOTA: Este método funcionará para otros animales SIEMPRE y cuando los incluya en coleccion_completa

        elif (modo_actual == "juego"):
            if (boton_cerrar.collidepoint(pos)):
                modo_actual = "menu"
            
            elif (animal.collidepoint(pos)):
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
    
                    # Animación de "compra exitosa"
                    bonus_1.y = 95
                    animate(bonus_1, tween='bounce_end', duration=0.25, y=100)
                    bonus_1.y = 105
                    animate(bonus_1, tween='bounce_end', duration=0.25, y=100)
                    
                    if (bonus_1.ya_activado == False):    # Chequeamos que NO se haya activado antes
                        schedule_interval(el_bonus_1, 2)  # Programamos las llamadas reiteradas
                        bonus_1.ya_activado = True        # Lo marcamos como "activado"
    
                    else: # SI YA ESTABA ACTIVO
                        bonus_1.potenciador += 1           # Aumentamos los puntos que dá este bonus
                    #######################################################################################
                else:   # Si NO tiene suficientes puntos para comprarlo
                        
                        # Animación de "compra rechazada"
                        bonus_1.x = 445
                        animate(bonus_1, tween='bounce_end', duration=0.25, x=450)
                        bonus_1.x = 455
                        animate(bonus_1, tween='bounce_end', duration=0.25, x=450)
            ##############################################################################################
    
            elif (bonus_2.collidepoint(pos)): # Si el click fue sobre el botón de bonus # 2:
    
                if (puntuacion >= bonus_2.precio): # Chequeamos si tiene suficientes puntos para comprarlo:
    
                    puntuacion -= bonus_2.precio   # Restamos los puntos gastados para comprar el bonus
                    # TAREA 9: Cuando pidan aumentar el precio -> bonus_2.precio *= 2
    
                    # Animación de "compra exitosa"
                    bonus_2.y = 195
                    animate(bonus_2, tween='bounce_end', duration=0.25, y=200)
                    bonus_2.y = 205
                    animate(bonus_2, tween='bounce_end', duration=0.25, y=200)
                    
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
    
            elif (bonus_3.collidepoint(pos)): # Si el click fue sobre el botón de bonus # 3:
    
                if (puntuacion >= bonus_3.precio): # Chequeamos si tiene suficientes puntos para comprarlo:
    
                    puntuacion -= bonus_3.precio   # Restamos los puntos gastados para comprar el bonus
                    # TAREA 9: Cuando pidan aumentar el precio -> bonus_3.precio *= 2
    
                    # Animación de "compra exitosa"
                    bonus_3.y = 295
                    animate(bonus_3, tween='bounce_end', duration=0.25, y=300)
                    bonus_3.y = 305
                    animate(bonus_3, tween='bounce_end', duration=0.25, y=300)
                    
                    if (bonus_3.ya_activado == False):    # Chequeamos que NO se haya activado antes
                        schedule_interval(el_bonus_3, 2)  # Programamos las llamadas reiteradas
                        bonus_3.ya_activado = True        # Lo marcamos como "activado"
    
                    else: # SI YA ESTABA ACTIVO
                        bonus_3.potenciador += 50         # Aumentamos los puntos que dá este bonus
                    #######################################################################################
                else:   # Si NO tiene suficientes puntos para comprarlo
                        
                        # EJEMPLO TAREA 8: Animación de "compra rechazada"
                        bonus_3.x = 445
                        animate(bonus_3, tween='bounce_end', duration=0.25, x=450)
                        bonus_3.x = 455
                        animate(bonus_3, tween='bounce_end', duration=0.25, x=450)
            ##############################################################################################
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