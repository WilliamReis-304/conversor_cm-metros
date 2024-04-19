from tkinter import *


#Criando a janela -----------------------------------
janela = Tk()
janela.geometry("550x170")

#Criando os widgets ---------------------------------

titulo = Label(janela, text = "CONVERSOR", font="Arial 20")
centimetrosTexto = Label(janela, text = "centímetros",font="Arial 12")
cm = Label(janela, text = "cm",font=("Arial 12"))
metrosTexto = Label(janela, text = "metros",font=("Arial 12"))
centimetros = Entry(janela, width=20 ,font=("Arial 12"))
resultado = Label(janela,text=" ",font="Arial 12")


#Organizando widgets na tela -----------------------
titulo.pack()
centimetrosTexto.pack()
centimetros.pack()
metrosTexto.pack()
resultado.pack()
cm.place(x=370,y=60)

#Definindo funções para os botões ------------------
def converter():
    calculo = float(centimetros.get())/100
    resultado.configure(text = f"{calculo} m")

def checarNumero():
    try:
        float(centimetros.get())

    except:
        resultado.configure(text = "Por favor, digite um numero válido!")

    else:
        converter()


#Criando e organizando os botões -------------------

paraMetro = Button(janela, text="converter", command = checarNumero)
paraMetro.pack()


janela.mainloop()