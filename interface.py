from tkinter import *
from leitura import texto
class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.msg = Label(self.widget1, text=texto)
        self.msg["font"] = ("Verdana", "25", "italic", "bold")

        self.msg.pack ()

        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["height"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack ()

root = Tk()
root.title("MONITVPP")
root.config(padx=125, pady=100)
Application(root)
root.mainloop()