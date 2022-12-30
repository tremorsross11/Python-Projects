
import tkinter
from tkinter import *

class parentwindow(Frame):
    def __init__ (self,  master):
        Frame.__init__ (self)

        self.master = master
        
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('learning tkinter')
        self.master.config(bg='darkgrey')
    
        self.varFname = StringVar()
        self.varLname = StringVar()
       

        self.txtFname = Entry(self.master, text=self.varFname, font=("Helvetica", 14), fg='black', bg='blue')
        self.txtFname.pack()

        self.txtLname = Entry(self.master, text=self.varLname, font=("Helvetica", 14), fg='black', bg='blue')
        self.txtLname.pack()



if __name__ == "__main__":
    root = Tk()
    App = parentwindow(root)
    root.mainloop()
