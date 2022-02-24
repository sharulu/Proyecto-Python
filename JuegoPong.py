#!/usr/bin/python3
#                    Universidad de Costa Rica
#                 Escuela de Ingenieria Electrica
#            IE0117 Programacion Bajo Plataformas Abiertas

#                        Proyecto de Python
#                            JUEGO PONG
# Elaborado por: Yennifer Espinoza Fuentes  <yennifer.espinoza@ucr.ac.cr>
#                Sharlotte Orozco Rojas    <sharlotte.orozco@ucr.ac.cr>
# Fecha: 02/2022

# Descripcion: Juego Pong.


import turtle
# -------------------------------VENTANA----------------------------------
'''Primero se crea la ventana, con turtle.Screen
 .setup() se define las dimensiones de ancho y alto
 .bgcolor() es el color de fondo
 .tracer() es para que la animacion se vea corrida'''
ventana = turtle.Screen()
ventana.setup(width=600, height=400)
ventana.title('Juego Pong')
ventana.bgcolor('black')
ventana.tracer(0)

# -------------------------------BOLA---------------------------------
''' Segundo se crea la bola con turtle.Turtle
 .goto(x,y) es para establecer las coordenadas de la bola, el centro es (0,0)
 .shape() es para determinar la forma de la bola
 .color() es el color de la bola
 .penup() es para eliminar el rastro de la bola'''
Bola = turtle.Turtle()
Bola.goto(0, 0)
Bola.shape('circle')
Bola.color('white')
Bola.penup()

'''Para que se mueva la bola se tiene que agregar un cambio de direccion
en las coordenadas (x,y) con .dx y se le asigna 0.09 que significa que la
bola se va a mover cada 0.09 pixeles'''
Bola.dx = 0.09
Bola.dy = 0.09
# ------------------------------BARRAS---------------------------------
# DERECHA
'''Segundo se crea la barra derecha con turtle.Turtle
 .goto(x,y) es para establecer las coordenadas de la bola, en este caso
 se ocupa la barra a la derecha, por lo tanto se pone en (280,0) no se coloca
 en (300,0) porque querdaría muy pegada al borde de la ventana.
 .shape() es determinar la forma de la barra
 .shapesize() es para cambiar de forma el cuadrado, hacerlo un rectangulo
 .color() es el color de la barra
 .speed() es para que aparezca en la pantalla cuando se abra la ventana
 .penup() es para eliminar el rastro de la linea'''
Barra_Derecha = turtle.Turtle()
Barra_Derecha.goto(280, 0)
Barra_Derecha.shape('square')
Barra_Derecha.shapesize(stretch_len=0.75, stretch_wid=4)
Barra_Derecha.color('white')
Barra_Derecha.speed(0)
Barra_Derecha.penup()

# IZQUIERDA
Barra_Izquierda = turtle.Turtle()
Barra_Izquierda.goto(-280, 0)
Barra_Izquierda.shape('square')
Barra_Izquierda.shapesize(stretch_len=0.75, stretch_wid=4)
Barra_Izquierda.color('white')
Barra_Izquierda.speed(0)
Barra_Izquierda.penup()

# ------------------------Mensaje INICIO--------------------------------------
# Pide al usuario presionar ENTER para iniciar
inicio = turtle.Turtle()
inicio.goto(0, 150)
inicio.color('white')
inicio.speed(0)
inicio.penup()
inicio.hideturtle()
# -----------------------MARCADOR------------------------------------------
# Variables del marcador
marcador1 = 0
marcador2 = 0
marcadorganador = 7
marcador = turtle.Turtle()
marcador.goto(0, 150)
marcador.color('white')
marcador.speed(0)
marcador.penup()
marcador.hideturtle()
marcador.write('Jugador 1: 0                       Jugador 2: 0', align = 'center',font=(12))

# ------------------------REINICIO------------------------------------------
reinicio = turtle.Turtle()
reinicio.goto(0, 50)
reinicio.color('white')
reinicio.speed(0)
reinicio.penup()
reinicio.hideturtle()

# -------------------------------DESPLAZAMIENTO DE BARRAS----------------------
'''Se usa una funcion para que la Barra_Derecha se mueva hacia arriba, por lo
tanto se emplea el eje 'y' usando Barra_Derecha.ycor que es la coordenada 'y'
el movimiento funciona por pixeles entonces a la variable 'y' se le suma
10 pixeles lo que hace que mueva hacia arriba.
sety() se utiliza para establecer la orientacion del angulo'''


def Barra_Derecha_Arriba():
    y = Barra_Derecha.ycor()
    y += 10
    Barra_Derecha.sety(y)


'''Se hace la misma funcion solo que esta vez se le resta -10 pixeles
#porque va en direccion contraria'''


def Barra_Derecha_Abajo():
    y = Barra_Derecha.ycor()
    y -= 10
    Barra_Derecha.sety(y)


'''Ahora para que la tecla direccional 'Up' o 'Down', pueda realizar la
instruccion de la funcion 'Barra_Derecha_Arriba', se debe llamar con
el comando .listen() y con .onkeypress() se le coloca cual tecla se usara.'''
ventana.listen()
ventana.onkeypress(Barra_Derecha_Arriba, 'Up')
ventana.onkeypress(Barra_Derecha_Abajo, 'Down')

'''Se repite el mismo procedimiento para la Barra_Izquierda'''


def Barra_Izquierda_Arriba():
    y = Barra_Izquierda.ycor()
    y += 10
    Barra_Izquierda.sety(y)


'''Se hace la misma funcion solo que esta vez se le resta -10 pixeles
#porque va en direccion contraria'''


def Barra_Izquierda_Abajo():
    y = Barra_Izquierda.ycor()
    y -= 10
    Barra_Izquierda.sety(y)


ventana.listen()
ventana.onkeypress(Barra_Izquierda_Arriba, 'w')
ventana.onkeypress(Barra_Izquierda_Abajo, 's')

# ---------------------------PAUSA--------------------------------------
''' Se crea una funcion para que el juego se pause cuando se termina'''


def pausa():
    global GameOn
    global ganar
    global reinicio
    global marcador
    marcador.clear()
    reinicio.clear()
    marcador.write('Jugador {} es el ganador'.format(ganar),
                   align='center', font=(12))
    reinicio.write('presione r para reiniciar', align='center', font=(24))
    while not GameOn:
        ventana.update()
        ventana.listen()
        ventana.onkeypress(Inicio_Juego, 'r')


# Se inicializan variables para cuando el juego no se esta jugando
GameOn = False
quieta = True
ganar = 0

'''Funcion que le permite a la bola comenzar a moverse, cuando la bola
no esta quieta, inicia el juego'''


def start_game():
    global quieta
    quieta = False
    inicio.clear()
    marcador.write('Jugador 1: {}                       Jugador 2: {}'.format(marcador1, marcador2), align='center', font=(12))


'''Funcion que detiene la bola'''


def stop_ball():
    global quieta
    quieta = True


'''Funcion del inicio del juego'''


def Inicio_Juego():
    global GameOn
    global ganar
    global reinicio
    global marcador
    global quieta
    # Bola inicia sin moverse
    quieta = True
    marcador.clear()
    # Si el jugador presiona enter, empieza el juego
    inicio.write('Presione ENTER para iniciar', align='center', font=("Fixedsys", 24))
    ventana.update()
    ventana.listen()
    ventana.onkeypress(start_game, 'Return')
    GameOn = True
    marcador1 = 0
    marcador2 = 0
    reinicio.clear()
    marcador.clear()
    ganar = 0
    while GameOn:
        ventana.update()

        # ----------------DESPLAZAMIENTO DE BOLA-----------------------------
        '''Para que la bola se mueva se llama al parametro 'Bola'
         y con .set se establece la orientacion del angulo sumando
        las coordenadas (x,y) con el cambio de direccion .dx y .dy'''
        if quieta is False:
            Bola.setx(Bola.xcor() + Bola.dx)
            Bola.sety(Bola.ycor() + Bola.dy)

        # -----------------LOGICA PARA QUE LA BOLA NO SE SALGA ----------------
        # ------------------DE LOS BORDES SUPERIOR-INFERIOR------------------
        '''Si la bola con la coordenada 'y' es menor a 190
        entonces la Bola.dy (recordar que es el cambio de direccion)
        se multiplica por -1 para que cambie a la direccion opuesta.
        Lo mismo si la coordenada 'y' es mayor a 190
        Es 190 porque la altura de la ventana es 400, o sea la mitad es
        200 pero se le resta 10 entonces 190'''
        if Bola.ycor() < -190:
            Bola.dy *= -1
        if Bola.ycor() > 190:
            Bola.dy *= -1
        # -----------------LOGICA PARA QUE LA BOLA NO SE SALGA ----------------
        # ------------------DE LOS BORDES IZQUIERDA-DERECHA------------------
        '''Es la misma logica que la anterior, pero con 290, ya que el ancho
        es 600.
        En este caso cada que la bola choque con un borde, se ocupa que salga
        del centro para esto se uso .goto(0,0) y se multiplica por -1 para
        que cambie de direccion.'''

        # Izquierda
        if Bola.xcor() < -290:
            Bola.goto(0, 0)
            Bola.dx *= -1
            # incremento del marcador2
            marcador2 += 1
            # Borra el marcador para que los numeros no se sobreescriban
            marcador.clear()
            # imprimir los valores en el marcador
            marcador.write('Jugador 1: {}                       Jugador 2: {}'.format(marcador1, marcador2), align='center', font=(12))
        # Derecha
        if Bola.xcor() > 290:
            Bola.goto(0, 0)
            Bola.dx *= -1
            # incremento del marcador1
            marcador1 += 1
            # Borra el marcador para que los numeros no se sobreescriban
            marcador.clear()
            # imprimir los valores en el marcador
            marcador.write('Jugador 1: {}                       Jugador 2: {}'.format(marcador1, marcador2), align='center', font=(12))

        if marcador1 >= marcadorganador:
            ganar = 1

        if marcador2 >= marcadorganador:
            ganar = 2

        # Si algien gana, el juego para y se reinicia
        if ganar != 0:
            GameOn = False
            marcador.clear()
            reinicio.clear()
            pausa()
            stop_ball()

        # ------------------------BORDES DE LAS BARRAS-------------------------
        ''' Para los bordes de las Barras se toma en cuenta los pixeles, de
        de la barra, entonces recordar que el ancho de la ventana es de 600, y
        la mitad es 300, pero para que la barra no quede pegada al borde se le
        resto 10 por lo cual es 290. El borde de la barra interior que
        choca con la bola esta a una distancia de 20 pixeles respecto al borde
        de la ventana por tanto, los limites estan dentro de 260 y 270.
        Para la parte vertical a la barra se le sumo 30 pixeles ya que, fue lo
        suficiente que se necesito para la bola rebotara.'''
        # Borde Barra Derecha
        if ((Bola.xcor() > 260 and Bola.xcor() < 270)
            and (Bola.ycor() < Barra_Derecha.ycor() + 30
            and Bola.ycor() > Barra_Derecha.ycor()-30)):
            Bola.dx *= -1
        # Borde Barra Izquierda
        if ((Bola.xcor() < -260 and Bola.xcor() > -270)
            and (Bola.ycor() > Barra_Izquierda.ycor()-30
            and Bola.ycor() < Barra_Izquierda.ycor()+30)):
            Bola.dx *= -1


Inicio_Juego()
