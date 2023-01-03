import tkinter as tk
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")
        self.sourceDir_btn = Button(text="Select Source", width=20)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))
        self.source_dir = Entry(width=75)
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))
##        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady(30,0))
        self.destDir_btn = Button(text="Select Destination", width=20)
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))
        self.destination_dir = Entry(width=75)
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
