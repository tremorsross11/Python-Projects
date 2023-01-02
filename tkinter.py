
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

        self.lblFname = Label(self.master,  text='First Name: ', font=("Helvetica", 14), fg='black', bg='darkgrey')
        self.lblFname.grid(row=0, column=0, padx=(30, 0), pady=(30, 0))

        self.lblLname = Label(self.master,  text='Last Name: ', font=("Helvetica", 14), fg='black', bg='darkgrey')
        self.lblLname.grid(row=1, column=0, padx=(30, 0), pady=(30,0))

        self.lblDisplay = Label(self.master, text="", font=("Helvetica", 14), fg='black', bg='darkgrey')
        self.lblDisplay.grid(row=3, column=1, padx=(30, 0), pady=(30,0))

        self.txtFname = Entry(self.master, text=self.varFname, font=("Helvetica", 14), fg='black', bg='blue')
        self.txtFname.grid(row=0, column=1, padx=(30, 0), pady=(30,0))

        self.txtLname = Entry(self.master, text=self.varLname, font=("Helvetica", 14), fg='black', bg='blue')
        self.txtLname.grid(row=1, column=1, padx=(30, 0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(30, 0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0, 90), pady=(30,0), sticky=NE)

    def submit(self):
        fn = self.varFname.get()
        ln = self.varLname.get()
        self.lblDisplay.config(text='Hello {} {}'.format(fn, ln))

    def cancel(self):
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    App = parentwindow(root)
    root.mainloop()
