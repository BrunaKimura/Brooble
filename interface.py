from tkinter import *
# import ImageTk
from PIL import Image
import brooble
  
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 50
        self.primeiroContainer.configure(background='white')
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 10
        self.segundoContainer.configure(background='white')
        self.segundoContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.configure(background='white')
        self.quartoContainer.pack()

        self.image = PhotoImage(file='logo.png')
        self.img = self.image.subsample(2, 2)
        self.titulo = Label(self.primeiroContainer, bg="white", image=self.img)
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Pesquisa ", font=self.fontePadrao, bg="white")
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.buscar = Button(self.quartoContainer)
        self.buscar["text"] = "Buscar"
        self.buscar["font"] = ("Calibri", "8")
        self.buscar["width"] = 12
        self.buscar["command"] = self.buscaimg
        self.buscar.pack()

    
    def buscaimg(self):
        pesquisa = self.nome.get()
        brooble.encontra(pesquisa)

  
  
root = Tk()
root.geometry("700x700")
root.configure(background='white')
Application(root)
root.mainloop()