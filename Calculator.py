from tkinter import Tk, Button, StringVar

class Caculator():
    def __init__(self,master):
        master.title("Calculator")
        master.geometry("357×420+0+0")
        master.config(bg="gray")
        master.resizable(False,False)

        self.equation = StringVar()
        self.entry_value=''
        Entry(width=17,bg='#fff', font=('Arial bold',28),textvariable=self.equation).place(x=0,y=0)


root = Tk()
root.mainloop()