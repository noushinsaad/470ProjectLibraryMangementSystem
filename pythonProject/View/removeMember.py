from tkinter import *
from tkinter import ttk
from Model.dbCon import Mysql
from Model import model as m
from Controller import controller as a
u = a.users()





class RemoveMember(Toplevel):
    def __init__(self):
        con = Mysql.Connect()
        cur = con.cursor()
        Toplevel.__init__(self)
        self.geometry("800x800")
        self.title("Return book")
        self.resizable(False, False)

        self.top_frame = Frame(self, height=150, bg='grey')
        self.top_frame.pack(fill=X)
        heading = Label(self.top_frame, text='Remove Member from Library', font='arial 18 bold', bg='grey')
        heading.place(x=300, y=60)

        self.bodyframe = Frame(self, height=650, bg='white')
        self.bodyframe.pack(fill=X)

        cur.execute("SELECT * FROM member")
        books = cur.fetchall()
        book_list = []
        for book in books:
            book_list.append(str(book[0]) + '-' + book[1])

        self.lbl_name = Label(self.bodyframe, text='Enter member name:', font='arial 12 bold', bg='white')
        self.lbl_name.place(x=40, y=40)
        self.book_name = StringVar()
        self.txt_book_combo = ttk.Combobox(self.bodyframe, textvariable=self.book_name)
        self.txt_book_combo.place(x=200, y=45)
        self.txt_book_combo['values'] = book_list



        savebutton = Button(self.bodyframe, text='Remove', command=self.remove_member)
        savebutton.place(x=400 , y=45)

    def remove_member(self):
        u.setUserid(self.txt_book_combo.get().split('-')[0])
        ib = m.account()
        ib.Removemember(u)

