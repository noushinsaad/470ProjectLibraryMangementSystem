from Controller import controller as c
from Model import model as m
from tkinter import *


class Library:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("900x500")
        self.root.resizable(False, False)
        self.root.configure(bg='cadetblue')


        # ==================MFrames=================================
        MainFrame = Frame(self.root, bg='cadetblue')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=10, width=850, padx=60, relief=RIDGE,)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, width=25, font=('arial', 40, 'bold'), text="Admin Log in")
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame, bd=10, width=1300, height=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=10, width=1300, height=400, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)



        DataFrameLEFT = Frame(DataFrame, bd=10, width=800, height=300, padx=13, pady=2, relief=RIDGE)
        DataFrameLEFT.pack(side=TOP)


        #=========================================================

        self.lblFirstname = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="User Name :", padx=2, pady=2)
        self.lblFirstname.grid(row=3, column=0, sticky=W)
        self.txtFirstname = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  width=36)
        self.txtFirstname.grid(row=3, column=1)

        self.lblLastName = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Password :", padx=2, pady=2)
        self.lblLastName.grid(row=4, column=0, sticky=W)
        self.txtLastName = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width=36,show="*")
        self.txtLastName.grid(row=4, column=1)

        #=====================================================================
        def gotologin():
            u=c.users()
            u.setUsername(self.txtFirstname.get())
            u.setPassword(self.txtLastName.get())
            a=m.account()
            a.Login(u)


        #=======================Buttons==============================
        self.btnDisplayData = Button(ButtonFrame, text="Log In", font=('arial', 15, 'bold'), padx=2, width=8,
                                     bd=2, bg='cadetblue',command=gotologin)
        self.btnDisplayData.grid(row=0, column=1, padx=3)

        #====================================================

if __name__ == '__main__':
       root=Tk()
       app=Library(root)
       root.mainloop()