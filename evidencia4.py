from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Responde al click en pantalla lanzando la pelota"
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    "Regresa True si el punto está dentro de la pantalla."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Dibuja la pelota y los blancos."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Mueve la pelota y los blancos."
    # Crear nuevos blancos aleatorios
    if randrange(30) == 0:  # más frecuente (antes 40)
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Hacemos que los targets se muevan más rápido
    for target in targets:
        target.x -= 0.5

    # Gravedad al proyectil
    if inside(ball):
        speed.y -= 0.5   #Aquí se hace el cambio de velocidad (antes 0.35)
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        # Aqui vemos si la colisión golpea el blanco, desaparece
        if abs(target - ball) > 13:
            targets.append(target)

    # Redibujamos todo
    draw()

   
    for target in targets:
        if not inside(target):
            return

    ontimer(move, 30)  # más rápido (antes 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

