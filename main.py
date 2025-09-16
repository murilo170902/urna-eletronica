from tkinter import*
janela = Tk()
janela.title("urna eletronica")


candidato1 = ["lucas"]
candidato2 = ["marcos"]
nulos = ["nulo"]
votoc1 = 0
votoc2 = 0
nulo = 0

def votar_c1():
	global votoc1
	votoc1 += 1

def votar_c2():
	global votoc2
	votoc2 += 1

def votar_nulo():
	global nulo
	nulo += 1

def janela2():
	janela2 = Toplevel(janela)
	janela2.title("votar")
	votarbtn2 = Button(janela2, text="candidato1", command=votar_c1)
	votarbtn2.pack()

	votarbtn2 = Button(janela2, text="candidato2", command=votar_c2)
	votarbtn2.pack()
	
	votarbtn2 = Button(janela2, text="nulo", command=votar_nulo)
	votarbtn2.pack()

def janela3():
	janela3 = Toplevel(janela)
	janela3.title("numero de votos")

	candidat1 = Label(janela3, text="")
	candidat1.config(text=candidato1)
	candidat1.pack()
	votoc13 = Label(janela3, text="")
	votoc13.config(text=votoc1)
	votoc13.pack()

	candidat2 = Label(janela3, text="")
	candidat2.config(text=candidato2)
	candidat2.pack()
	votoc21 = Label(janela3, text="")
	votoc21.config(text=votoc2)
	votoc21.pack()

	nulov = Label(janela3, text="")
	nulov.config(text=nulos)
	nulov.pack()
	votoc41 = Label(janela3, text="")
	votoc41.config(text=nulo)
	votoc41.pack()

votarbtn = Button(janela,  text="votar",command=janela2)
votarbtn.pack()
votarbtn = Button(janela,  text="numero de votos",command=janela3)
votarbtn.pack()

Label(janela, text="menu").pack()

janela.mainloop()
