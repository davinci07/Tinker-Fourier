from tkinter import *
import numpy 

class MainUI:
    def __init__(self, master):
        self.master = master
        master.title("Pyrier Machine ")
        master.geometry("500x500")
        self.label = Label(master,
                           text ="Please enter the details for your Fourier Series"
                           )
        self.label.grid()
        self.entry = Entry(master)
        self.entry.grid(row= 1, column=0, sticky="w")
        self.FourierButton = Button(master, text="Make the Fourier!", command=self.Fourier)
        self.FourierButton.grid(row= 1)
        self.close = Button(master, text= "Quit", command=master.destroy)
        self.close.grid(row= 1,column= 0, sticky="e")

    def Fourier(self):
       print(self.entry.get())
        



root = Tk()
main = MainUI(root)
root.mainloop()
