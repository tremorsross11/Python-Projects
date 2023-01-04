import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web page generator")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command= self.defaultHTML)
        self.btn.grid(row=2, column=1, padx=(10,10) , pady=(10,10))
        self.butn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.addHTML)
        self.butn.grid(row=2, column=0, padx=(20,20), pady=(20,20))
        self.entry = Entry(self.master, width=50)
        self.entry.grid(row=1, column=0, sticky=W+E, columnspan=2, padx=(30,15), pady=(20,20))
        

    def defaultHTML(self): #function that enters header into html document
        htmlText = "Stay tuned for our summer sale"
        htmlFile = open("index.html",  "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def addHTML(self): #function that enters text into html document
        self.butntxt = open("index.html", "w")
        textb=self.entry.get()
        print(textb)
        HTMLtxt = "<html>\n<body>" + textb + "</body>\n</html>"
        self.butntxt.write(HTMLtxt)
        self.butntxt.close()
        webbrowser.open_new_tab("index.html")
        

    




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
