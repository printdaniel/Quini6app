from tkinter import*
from tkinter.font import BOLD
import random

class quiniapp:
    def __init__(self,window):
        self.root=window
        self.root.title("Números para el Quini 6")
        self.root.config(bg="#f8e91a")
        
        self.imagen=PhotoImage(file="quini.png")
        self.imgquini=Label(self.root,image=self.imagen)
        self.imgquini.grid(row=0,column=0)
        
        self.frame = LabelFrame(self.root,text="Números para jugar")
        self.frame.grid(row=1, column=0)
        
        self.n1 = StringVar()
        self.n2 = StringVar()
        self.n3 = StringVar()
        self.n4 = StringVar()
        self.n5 = StringVar()
        self.n6 = StringVar()
        
        self.frame1 = LabelFrame(self.root,text="Buena suerte!!!")
        self.frame1.grid(row=3, column=0)
                
        self.num1 = Entry(self.frame,width="5",font=('arial',15),textvariable=self.n1)
        self.num2 = Entry(self.frame,width="5",font=('arial',15),textvariable=self.n2)
        self.num3 = Entry(self.frame,width="5",font=('arial',15),textvariable=self.n3)
        self.num4 = Entry(self.frame,width="5",font=('arial',15),textvariable=self.n4)
        self.num5 = Entry(self.frame,width="5",font=('arial',15),textvariable=self.n5)
        self.num6 = Entry(self.frame,width="5",font=('arial',15),textvariable=self.n6)
        
        self.num1.grid(row=2,column=0)
        self.num2.grid(row=2,column=1)
        self.num3.grid(row=2,column=2)
        self.num4.grid(row=2,column=3)
        self.num5.grid(row=2,column=4)
        self.num6.grid(row=2,column=5)
        
        com_buton=Button(self.frame1,text="¡Voy a tener suerte!",command=self.num_random,
                         font=('arial',20,BOLD),relief=GROOVE)
        com_buton.grid(row=0,column=0)
    
    def num_random(self):
        self.n1.set(random.randint(0,40))
        self.n2.set(random.randint(0,40))
        self.n3.set(random.randint(0,40))
        self.n4.set(random.randint(0,40))
        self.n5.set(random.randint(0,40))
        self.n6.set(random.randint(0,40))
            
        
        
        




if __name__=='__main__':
    window=Tk()
    app=quiniapp(window)
    window.mainloop()