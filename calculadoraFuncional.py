from tkinter import *
raiz = Tk()
raiz.title("Calculadora")

#função para digitar os botoes clicados
def clicar(numero):
    atual = input.get()
    input.delete(0, END)
    input.insert(0, str(atual) + str(numero))   #adiciona um numero a direita dele

def somar():
    primeiro_numero = input.get()
    global p_num
    global conta
    conta = "somar"
    p_num = int(primeiro_numero)
    input.delete(0, END)

def subtrair():
    primeiro_numero = input.get()
    global p_num
    global conta
    conta = "subtrair"
    p_num = int(primeiro_numero)
    input.delete(0, END)

def dividir():
    primeiro_numero = input.get()
    global p_num
    global conta
    conta = "dividir"
    p_num = int(primeiro_numero)
    input.delete(0, END)

def multiplicar():
    primeiro_numero = input.get()
    global p_num
    global conta
    conta = "multiplicar"
    p_num = int(primeiro_numero)
    input.delete(0, END)

def igualar():
    segundo_numero = input.get()
    input.delete(0, END)

    if conta == "somar":
        input.insert(0, p_num + int(segundo_numero))
    if conta == "subtrair":
        input.insert(0, p_num - int(segundo_numero))
    if conta == "dividir":
        input.insert(0, p_num / int(segundo_numero))
    if conta == "multiplicar":
        input.insert(0, p_num * int(segundo_numero))

def apagar():
    input.delete(0, END)


#tela de input
input = Entry(raiz, width=20, borderwidth=5, bg="#33383e", fg="#d7d8da")
input.grid(row=0, column=0,  columnspan=4, padx=10, pady=10)

#botões
num1 = Button(raiz, text="1", padx=10, pady=5, font="Calibri", bg="#292a2e", fg="#d7d8da", command=lambda: clicar(1)).grid(row=1, column=0)
num2 = Button(raiz, text="2", padx=10, pady=5, font="Calibri", bg="#292a2e", fg="#d7d8da", command=lambda: clicar(2)).grid(row=1, column=1)
num3 = Button(raiz, text="3", padx=10, pady=5, font="Calibri", bg="#292a2e", fg="#d7d8da", command=lambda: clicar(3)).grid(row=1, column=2)
num4 = Button(raiz, text="4", padx=10, pady=5, font="Calibri", bg="#292a2e", fg="#d7d8da", command=lambda: clicar(4)).grid(row=2, column=0)
num5 = Button(raiz, text="5", padx=10, pady=5, font="Calibri", bg="#292a2e", fg="#d7d8da", command=lambda: clicar(5)).grid(row=2, column=1)
num6 = Button(raiz, text="6", padx=10, pady=5, font="Calibri", bg="#292a2e", fg="#d7d8da", command=lambda: clicar(6)).grid(row=2, column=2)
num7 = Button(raiz, text="7", padx=10, pady=5, font="Calibri", bg="#292a2e", fg="#d7d8da", command=lambda: clicar(7)).grid(row=3, column=0)
num8 = Button(raiz, text="8", padx=10, pady=5, font="Calibri", bg="#292a2e", fg="#d7d8da", command=lambda: clicar(8)).grid(row=3, column=1)
num9 = Button(raiz, text="9", padx=10, pady=5, font="Calibri", bg="#292a2e", fg="#d7d8da", command=lambda: clicar(9)).grid(row=3, column=2)
num0 = Button(raiz, text="0", padx=10, pady=5, font="Calibri", bg="#292a2e", fg="#d7d8da", command=lambda: clicar(0)).grid(row=4, column=0)
somar = Button(raiz, text="+", padx=10, pady=5, font="Calibri", bg="#5ab2f1", fg="#021d32", command=somar).grid(row=1, column=3)
subtrair = Button(raiz, text="-", padx=11, pady=5, font="Calibri", bg="#5ab2f1", fg="#021d32", command=subtrair).grid(row=2, column=3)
dividir = Button(raiz, text="÷", padx=10, pady=5, font="Calibri", bg="#5ab2f1", fg="#021d32", command=dividir).grid(row=4, column=3)
multiplicar = Button(raiz, text="x", padx=10, pady=5, font="Calibri", bg="#5ab2f1", fg="#021d32", command=multiplicar).grid(row=3, column=3)
igual = Button(raiz, text="=", padx=10, pady=5, font="Calibri", bg="#d3e3fd", fg="#021d32", command=igualar).grid(row=4, column=2)
deletar = Button(raiz, text="del", padx=4, pady=5, font="Calibri", bg="#c3eed0", fg="#021d32", command=apagar).grid(row=4, column=1)

#mainloop
raiz.mainloop()