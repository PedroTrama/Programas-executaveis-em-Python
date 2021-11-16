# PONG
import turtle  # turtle é uma biblioteca para criar a tela do jogo

# Configurações da tela
janela = turtle.Screen()  # cria a tela
janela.title("Pong")  # titulo
janela.bgcolor("black")  # cor
janela.setup(width=800, height=600)  # tamanho
janela.tracer(0)  # impede que a janela atualize sozinha, acelera o jogo

# Barra A
barraA = turtle.Turtle()
barraA.speed(0)
barraA.shape("square")
barraA.color("white")
barraA.shapesize(stretch_wid=5, stretch_len=1)
barraA.penup()
barraA.goto(-350, 0)

# Barra B
barraB = turtle.Turtle()
barraB.speed(0)
barraB.shape("square")
barraB.color("white")
barraB.shapesize(stretch_wid=5, stretch_len=1)
barraB.penup()
barraB.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.shapesize(stretch_wid=1, stretch_len=1)
bola.penup()
bola.goto(0,0)
bola.dx = 0.5
bola.dy = -0.5

# Funções
def cimaA():
    y = barraA.ycor()
    y += 20
    barraA.sety(y)

def baixoA():
    y = barraA.ycor()
    y -= 20
    barraA.sety(y)

def cimaB():
    y = barraB.ycor()
    y += 20
    barraB.sety(y)

def baixoB():
    y = barraB.ycor()
    y -= 20
    barraB.sety(y)

# Teclado
janela.listen()
janela.onkeypress(cimaA, "w")
janela.onkeypress(baixoA, "s")
janela.onkeypress(cimaB, "Up")
janela.onkeypress(baixoB, "Down")

# Main game loop
while True:
    janela.update()

    #Movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    #Colisao
    placarA = 0
    placarB = 0
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.setx(390)
        bola.dx *= -1

    if bola.xcor() < -390:
        bola.setx(-390)
        bola.dx *= -1

    if bola.xcor() == 390:
        placarA += 1
        print(placarA)
    if bola.xcor() == -390:
        placarB += 1
        print(placarB)



