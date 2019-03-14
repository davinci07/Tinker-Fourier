from tkinter import *
import numpy as np
import matplotlib as plt

class MainUI(Tk):
    def __init__(self, master):
        Tk.__init__(self, master)
        self.master = master
        self.mainwidgets()
        
    def mainwidgets(self):
        #Title
        self.label = Label(self,
                           text ="Fourier Series Maker")
        self.label.grid(padx = 30)
        
        #Coefficients Window
        self.window1 = Frame1(self)
        self.window1.grid(row = 1, column = 0,
                          padx = 10, pady = 10)
        #Image Window
        self.window2 = Frame2(self)
        self.window2.grid(row=1,column =1,padx=10, pady = 10)                          

        #Close Button                  
        self.close = Button(self, text= "Quit", command=self.destroy)
        self.close.grid(ipadx= 0)

    def square_wave(self):
       pass


class Frame1(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent,
                       bd=1, relief=SUNKEN,
                       padx = 5, pady = 5)
        self.parent = parent
        self.FrameWidgets()

    def FrameWidgets(self):
        F2 = Frame2(self)
        f1 = Frame(self)
        #N units
        f1.Ncoeff = Label(self,
                          text ="N units").grid(padx = 5,row = 0,column= 0)
        f1.Nentry = Entry(self).grid(
            padx = 5, pady = 5,
            row =0,column= 1)
        f1.Mcoeff = Label(self,
                          text ="M units").grid(
                              padx = 5, pady = 5
                              ,row = 1,column= 0)
        f1.Mentry = Entry(self).grid(row =1,column= 1)
        #Activate Button
        f1.exec = Button(
            self, text="Activate",
            ).grid(row=2, column=0)
        #Reset Button
        f1.exec = Button(
            text="Reset", command=F2.reset_image
            ).grid(row=2, column=1)
        #self.FourierButton = Button(master, text="Make the Fourier!", command=self.square_wave)
        #self.FourierButton.grid(row= 1)
        

class Frame2(Frame):
    #Frame to contain the charts and such
    def __init__(self, parent):
        Frame.__init__(self,parent,
                       bd=1, relief=SUNKEN,
                       padx = 5, pady = 5)
        self.parent = parent
        self.canvas = Canvas(bg= "white")
         
    #Reset Image
    def reset_image(self):
        self.canvas.delete("all")
        self.canvas.grid()
        self.canvas.config(bg="white")
        self.basic = PhotoImage(file="FourierSine.png")
        self.canvas.create_image(0, 0, anchor=NW, image=self.basic)














if __name__=="__main__":
    app = MainUI(None)
    app.geometry = ("500x500")
    app.title("Pyrier Machine")
    app.mainloop()


