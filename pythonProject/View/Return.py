from tkinter import *
from tkinter import ttk
from Model.dbCon import Mysql
from Model import model as m
from Controller import controller as a
u = a.users()





class ReturnBook(Toplevel):
    def __init__(self):
        con = Mysql.Connect()
        cur = con.cursor()
        Toplevel.__init__(self)
        self.geometry("800x800")
        self.title("Return book")
        self.resizable(False, False)

        self.top_frame = Frame(self, height=150, bg='grey')
        self.top_frame.pack(fill=X)
        heading = Label(self.top_frame, text='Return book to Library', font='arial 18 bold', bg='grey')
        heading.place(x=300, y=60)

        self.bodyframe = Frame(self, height=650, bg='white')
        self.bodyframe.pack(fill=X)

        cur.execute("SELECT * FROM member")
        members = cur.fetchall()
        member_list = []
        for member in members:
            member_list.append(str(member[0])+'-'+member[1])

        self.lbl_name = Label(self.bodyframe, text='Enter Member name:', font='arial 12 bold', bg='white')
        self.lbl_name.place(x=40, y=40)
        self.member_name = StringVar()
        self.txt_member_combo = ttk.Combobox(self.bodyframe, textvariable=self.member_name)
        self.txt_member_combo.place(x=200, y=45)
        self.txt_member_combo['values'] = member_list


        savebutton = Button(self.bodyframe, text='Select Book', command=self.Select_book)
        savebutton.place(x=400, y=45)


    def Select_book(self):

        u.setUserid(self.txt_member_combo.get().split('-')[0])
        con = Mysql.Connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM issuedbooks where userid='"+u.getUserid()+"'")
        books = cur.fetchall()
        book_list = []
        for book in books:
            book_list.append(str(book[1]))

        self.lbl_bookname = Label(self.bodyframe, text='elect Book Id: ', font='arial 12 bold', bg='white')
        self.lbl_bookname.place(x=40, y=80)
        self.book_name = StringVar()
        self.txt_book_combo = ttk.Combobox(self.bodyframe, textvariable=self.book_name)
        self.txt_book_combo.place(x=200, y=80)

        self.txt_book_combo['values'] = book_list

        savebutton = Button(self.bodyframe, text='Return', command=self.return_book)
        savebutton.place(x=400 , y=80)

    def return_book(self):
        u.setBookid(self.txt_book_combo.get().split('-')[0])
        ib = m.account()
        ib.Returnbook(u)

