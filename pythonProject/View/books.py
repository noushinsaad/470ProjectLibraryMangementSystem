from tkinter import *
from Model import model as m
from Controller import controller as a


class StoreBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("800x800")
        self.title("Add book")
        self.resizable(False, False)

        self.top_frame = Frame(self, height=150, bg='grey')
        self.top_frame.pack(fill=X)
        heading = Label(self.top_frame, text='Add new book',font='arial 18 bold' ,bg='grey')
        heading.place(x=300, y=60)

        self.bodyframe = Frame(self,height=650,bg='white')
        self.bodyframe.pack(fill=X)


        self.lbl_name = Label(self.bodyframe, text='Enter Book Name:', font='arial 12 bold', bg='white')
        self.lbl_name.place(x=40, y=80)
        self.txt_book_name = Entry(self.bodyframe, width=30, bd=2)
        self.txt_book_name.place(x= 200,y=80)

        self.lbl_author = Label(self.bodyframe, text='Enter author name:', font='arial 12 bold', bg='white')
        self.lbl_author.place(x=40, y=120)
        self.txt_author = Entry(self.bodyframe, width=30, bd=2)
        self.txt_author.place(x= 200,y=120)

        self.lbl_edition = Label(self.bodyframe, text='Edition:', font='arial 12 bold', bg='white')
        self.lbl_edition.place(x=40, y=160)
        self.txt_edition = Entry(self.bodyframe, width=30, bd=2)
        self.txt_edition.place(x= 200,y=160)

        self.lbl_published = Label(self.bodyframe, text='Published:', font='arial 12 bold', bg='white')
        self.lbl_published.place(x=40, y=200)
        self.txt_published = Entry(self.bodyframe, width=30, bd=2)
        self.txt_published.place(x=200, y=200)

        self.lbl_publisher = Label(self.bodyframe, text='Publisher:', font='arial 12 bold', bg='white')
        self.lbl_publisher.place(x=40, y=240)
        self.txt_publisher = Entry(self.bodyframe, width=30, bd=2)
        self.txt_publisher.place(x=200, y=240)

        # Save Button
        savebutton = Button(self.bodyframe, text='Save now', command=self.savebook)
        savebutton.place(x=270, y=280)

    def savebook(self):
        """
            Saves the book and updates the DB
        """
        u = a.users()
        u.setBookname(self.txt_book_name.get())
        u.setAuthor(self.txt_author.get())
        u.setEdition(self.txt_edition.get())
        u.setPublished(self.txt_published.get())
        u.setPublisher(self.txt_publisher.get())
        ab=m.account()
        ab.addBook(u)
