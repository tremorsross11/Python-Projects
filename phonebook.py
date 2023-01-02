
from  tkinter import *
import tkinter as  tk


import phonebook_gui
import phonebook_func



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500, 300)
        self.master.maxsize(500, 300)

        phonebook_func.center_window(self, 500, 300)

        self.master.title("The TKinter Phonebook")
        self.master.configure(bg='#F0F0F0')

        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        phonebook_gui.load_gui(self)
                             


        self.varFname = StringVar()
        self.varLname = StringVar()
        self.varPhone = StringVar()
        self.varEmail = StringVar()
        self.varInfo = StringVar()

        self.lblFname = tk.Label(self.master,  text='First Name: ', font=("Helvetica", 14), fg='black', bg='darkgrey')
        self.lblFname.grid(row=0, column=0, padx=(27, 0), pady=(10, 0), sticky=N+W)

        self.lblLname = tk.Label(self.master,  text='Last Name: ', font=("Helvetica", 14), fg='black', bg='darkgrey')
        self.lblLname.grid(row=2, column=0, padx=(27, 0), pady=(10,0), sticky=N+W)

        self.lbl_Phone = tk.Label(self.master,  text='Phone Number: ', font=("Helvetica", 14), fg='black', bg='darkgrey')
        self.lbl_Phone.grid(row=4, column=0, padx=(27, 0), pady=(10, 0), sticky=N+W)

        self.lbl_Email = tk.Label(self.master,  text='Email: ', font=("Helvetica", 14), fg='black', bg='darkgrey')
        self.lbl_Email.grid(row=6, column=0, padx=(27, 0), pady=(10,0),  sticky=N+W)

        self.lbl_Info = tk.Label(self.master,  text='Information: ', font=("Helvetica", 14), fg='black', bg='darkgrey')
        self.lbl_Info.grid(row=0, column=2, padx=(0, 0), pady=(10,0),  sticky=N+W)



if __name__=="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
        
