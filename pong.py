#PONG
import turtle  #turtle é uma biblioteca para criar a tela do jogo

#Configurações da tela
janela = turtle.Screen()                #cria a tela
janela.title("Pong")                    #titulo
janela.bgcolor("black")                 #cor
janela.setup(width=800, height=600)     #tamanho
janela.tracer(0)                        #impede que a janela atualize sozinha, acelera o jogo

#Barra A
barraA = turtle.Turtle()                        #coloca a barra na tela
barraA.speed(0)                                 #função de velocidade da animação (aqui está no máximo pras coisas nao ficarem lentas)
barraA.shape("square")                          #formato
barraA.color("white")                           #cor
barraA.shapesize(stretch_wid=5, stretch_len=1)  #dimensões
barraA.penup()                                  #tira a linha que aparece de default
barraA.goto(-350, 0)                            #posição inicial

#Barra B
barraB = turtle.Turtle()
barraB.speed(0)
barraB.shape("square")
barraB.color("white")
barraB.shapesize(stretch_wid=5, stretch_len=1)
barraB.penup()
barraB.goto(350, 0)

#Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.shapesize(stretch_wid=1, stretch_len=1)
bola.penup()
bola.goto(0, 0)
bola.velocidadex = 0.50
bola.velocidadey = -0.50

#Placar
placarA = 0
placarB = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

#Funções
def cimaA():            #movimento vertical de A
    y = barraA.ycor()   #aplica o valor da coordenada y na variável y
    y += 20             #a placa anda +20 pixels em A
    barraA.sety(y)      #coloca a barra na nova posição y

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

#Controles
janela.listen()                     #recebe inputs de teclado
janela.onkeypress(cimaA, "w")       #cada função tem uma tecla
janela.onkeypress(cimaA, "W")
janela.onkeypress(baixoA, "s")
janela.onkeypress(baixoA, "S")
janela.onkeypress(cimaB, "Up")
janela.onkeypress(baixoB, "Down")

#Main game loop, faz tudo funcionar
while True:
    janela.update()                     #a janela sempre atualiza

    #Movimento da bola
    bola.setx(bola.xcor() + bola.velocidadex)    #como está em loop, sempre que passa por aqui a posição da pola atualiza de acordo com a velocidade setada e sua coordenada anterior
    bola.sety(bola.ycor() + bola.velocidadey)

    #Colisao com a parede
    #Quando a bola chegar em uma parede ela precisa inverter sua velocidade em ambos sentidos
    if bola.ycor() > 290:   #Parte superior da tela
        bola.sety(290)      #Coloca a bola nessa coordenada (impede que ela saia da tela)
        bola.velocidadey *= -1       #Inverte a velocidade para ela ir no outro sentido

    if bola.ycor() < -290:  #Parte inferior da tela
        bola.sety(-290)
        bola.velocidadey *= -1

    if bola.xcor() > 390:   #Lado direito da tela
        bola.goto(0, 0)
        bola.velocidadex *= -1
        placarA += 1
        pen.clear()
        pen.write("Jogador A: " + str(placarA) + "    Jogador B: " + str(placarB), align="center", font=("Courier", 24, "normal"))

    if bola.xcor() < -390:  #Lado esquerdo da tela
        bola.goto(0, 0)
        bola.velocidadex *= -1
        placarB += 1
        pen.clear()
        pen.write("Jogador A: " + str(placarA) + "    Jogador B: " + str(placarB), align="center", font=("Courier", 24, "normal"))


    #Colisão com as barras
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < barraB.ycor() + 50 and bola.ycor() > barraB.ycor() - 50):   #Essa condicao limita a colisao ao espaco da barra
        bola.setx(340)
        bola.velocidadex *= -1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < barraA.ycor() + 50 and bola.ycor() > barraA.ycor() - 50):
        bola.setx(-340)
        bola.velocidadex *= -1