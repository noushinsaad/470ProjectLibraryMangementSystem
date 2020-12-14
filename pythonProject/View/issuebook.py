from tkinter import *
from tkinter import ttk
from Model.dbCon import Mysql
from Model import model as m
from Controller import controller as a

#con=Mysql.Connect()
#cur=con.cursor()
#u = a.users()


class IssueBook(Toplevel):
    def __init__(self):
        con = Mysql.Connect()
        cur = con.cursor()
        Toplevel.__init__(self)
        self.geometry("800x800")
        self.title("Issue book")
        self.resizable(False,False)


        self.top_frame = Frame(self, height=150, bg='grey')
        self.top_frame.pack(fill=X)
        heading = Label(self.top_frame, text='Issue book to member',font='arial 18 bold' ,bg='grey')
        heading.place(x=300, y=60)

        self.bodyframe = Frame(self,height=650,bg='white')
        self.bodyframe.pack(fill=X)

        cur.execute("SELECT * FROM books WHERE book_status=0")
        books=cur.fetchall()
        book_list = []
        for book in books:
            book_list.append(str(book[0])+'-'+book[1])

        

        self.lbl_name = Label(self.bodyframe, text='Enter book name:', font='arial 12 bold', bg='white')
        self.lbl_name.place(x=40, y=40)
        self.book_name = StringVar()
        self.txt_book_combo = ttk.Combobox(self.bodyframe, textvariable=self.book_name)
        self.txt_book_combo.place(x= 200,y=45)
        self.txt_book_combo['values'] = book_list

        cur.execute("SELECT * FROM member")
        members = cur.fetchall()
        member_list = []
        for member in members:
            member_list.append(str(member[0])+'-'+member[1])

        self.lbl_author = Label(self.bodyframe, text='Select member:', font='arial 12 bold', bg='white')
        self.lbl_author.place(x=40, y=80)
        self.member_name = StringVar()
        self.txt_member_combo = ttk.Combobox(self.bodyframe,textvariable=self.member_name)
        self.txt_member_combo.place(x= 200,y=80)

        self.txt_member_combo['values'] = member_list

        # Save Button
        savebutton = Button(self.bodyframe, text='Issue now',command=self.issue_book)
        savebutton.place(x=270, y=200)

    def issue_book(self):
        """
            Issues book to the given member and updates DB
        """
        u = a.users()
        u.setBookid(self.txt_book_combo.get().split('-')[0])
        u.setUserid(self.txt_member_combo.get().split('-')[0])
        ib = m.account()
        ib.Issuebook(u)

