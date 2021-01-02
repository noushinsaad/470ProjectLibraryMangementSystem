from tkinter import *
from Model import model as m
from Controller import controller as a


class StoreMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("900x900")
        self.title("Enter Member")
        self.resizable(False,False)

        #========================Frame================================

        self.top_frame = Frame(self, height=150, bg='grey')
        self.top_frame.pack(fill=X)
        heading = Label(self.top_frame, text='Add New Member',font='arial 18 bold' ,bg='grey')
        heading.place(x=300, y=60)

        self.bodyframe = Frame(self,height=650,bg='white')
        self.bodyframe.pack(fill=X)

        self.lbl_fname = Label(self.bodyframe, text='Enter First Name:', font='arial 12 bold', bg='white')
        self.lbl_fname.place(x=40, y=40)
        self.txt_fname = Entry(self.bodyframe, width=30, bd=2)
        self.txt_fname.place(x= 240,y=45)

        self.lbl_lname = Label(self.bodyframe, text='Enter Last Name', font='arial 12 bold', bg='white')
        self.lbl_lname.place(x=40, y=80)
        self.txt_lname = Entry(self.bodyframe, width=30, bd=2)
        self.txt_lname.place(x=240, y=80)

        self.lbl_uname = Label(self.bodyframe, text='Enter User Name:', font='arial 12 bold', bg='white')
        self.lbl_uname.place(x=40, y=120)
        self.txt_uname = Entry(self.bodyframe, width=30, bd=2)
        self.txt_uname.place(x=240, y=120)

        self.lbl_phone = Label(self.bodyframe, text='Enter Contact:', font='arial 12 bold', bg='white')
        self.lbl_phone.place(x=40, y=160)
        self.txt_phone = Entry(self.bodyframe, width=30, bd=2)
        self.txt_phone.place(x=240, y=160)

        self.lbl_email = Label(self.bodyframe, text='Enter Email:', font='arial 12 bold', bg='white')
        self.lbl_email.place(x=40, y=200)
        self.txt_email = Entry(self.bodyframe, width=30, bd=2)
        self.txt_email.place(x=240, y=200)

        self.lbl_dateRegistered = Label(self.bodyframe, text='Enter Registration Date:', font='arial 12 bold', bg='white')
        self.lbl_dateRegistered.place(x=40, y=240)
        self.txt_dateRegistered = Entry(self.bodyframe, width=30, bd=2)
        self.txt_dateRegistered.place(x=240, y=240)


        self.lbl_pswrd = Label(self.bodyframe, text='Enter Password:', font='arial 12 bold', bg='white')
        self.lbl_pswrd.place(x=40, y=280)
        self.txt_pswrd = Entry(self.bodyframe, width=30, bd=2)
        self.txt_pswrd.place(x= 240,y=280)



        # Save Button
        savebutton = Button(self.bodyframe, text='Add now', command=self.savemember)
        savebutton.place(x=270, y=360)


    def savemember(self):
        u=a.users()
        u.setFname(self.txt_fname.get())
        u.setLname(self.txt_lname.get())
        u.setUsername(self.txt_uname.get())
        u.setContact(self.txt_phone.get())
        u.setEmail(self.txt_email.get())
        u.setPassword(self.txt_pswrd.get())
        u.setDateRegistered(self.txt_dateRegistered.get())
        am=m.account()
        am.addMember(u)







