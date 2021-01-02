# model
from Model.dbCon import Mysql
from tkinter import messagebox
from View import home as a

class account:
    __connection = None

    def __init__(self):
        self.__connection = Mysql.Connect()
        self.cur = self.__connection.cursor()
    def Login(self,users):
        if self.__isvalidLogin(users):
            if self.__isAuthentic(users):
                self.__Authorize(users)
            else:

                messagebox.showerror("Library Management System", "Incorrect User Name or Password!!!")
        else:

            messagebox.showerror("Library Management System", "Please write a user name and password")
    def __isvalidLogin(self,users):
        if users.getUsername()!="" and users.getPassword()!="":
            return True
        return False
    def __isAuthentic(self,users):

        self.cur.execute("SELECT userid FROM admin WHERE username='"+users.getUsername()+"' AND password='"+users.getPassword()+"'")
        record=self.cur.fetchone()
        if record!=None:
            return True
        return False
    def __Authorize(self,users):
        p=a.System()
        p.showsummary()
        p.showbooks()
        p.showmember()

    def addBook(self,users):
        bookname=users.getBookname()
        author=users.getAuthor()
        edition=users.getEdition()
        published=users.getPublished()
        publisher=users.getPublisher()
        if (bookname != '' and author != '' and edition != '' and published != '' and publisher != ''):
            try:
                query = "INSERT INTO books (`bookname`, `author`, `edition`, `published`, `publisher`) VALUES(%s,%s,%s,%s,%s)"
                self.cur.execute(query, (bookname, author, edition, published, publisher))
                self.__connection.commit()
                messagebox.showinfo('Success', 'Book has been saved successfully', icon='info')
                return True
            except:
                messagebox.showerror('Error', 'Transaction failed!', icon='warning')
                return False

        else:
            messagebox.showerror('Error', 'All fields are required!', icon='warning')
            return False

    def addMember(self,users):
        """
            Adds member to the library and updates DB
        """
        fname=users.getFname()
        lname=users.getLName()
        uname=users.getUsername()
        phone=users.getContact()
        em=users.getEmail()
        rg=users.getRegistered()
        ps=users.getPassword()

        if (fname != '' and lname != '' and uname != '' and phone != '' and em != '' and rg != '' and ps != ''):
            try:
                query = "INSERT INTO member(`username`, `password`, `fname`, `lname`, `email`, `contact`, `dateregistered`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                self.cur.execute(query, (uname,ps,fname,lname,em,phone,rg))
                self.__connection.commit()
                messagebox.showinfo('Success', 'Member is added!', icon='info')
            except:
                messagebox.showerror('Error', 'Transaction failed!', icon='warning')

        else:
            messagebox.showerror('Error', 'All fields are required!', icon='warning')

    def Issuebook(self,users):
        bid=users.getBookid()
        uid=users.getUserid()
        if (bid != '' and uid!= ''):
            try:
                query = "INSERT INTO issuedbooks(bookid,userid)VALUES(%s,%s)"
                self.cur.execute(query, (bid, uid))
                self.__connection.commit()
                self.cur.execute("UPDATE books SET book_status=1 WHERE bookid=%s",(bid,))
                self.__connection.commit()
                messagebox.showinfo("Success","Book has been issued successfully!",icon='info')
            except:
                messagebox.showerror('Error','Transaction not commit',icon='warning')
        else:
            messagebox.showerror('Error', 'All fields are required!', icon='warning')


    def Returnbook(self,users):
        bid = users.getBookid()
        if (bid != ''):
            try:
                self.cur.execute("DELETE from issuedbooks where bookid='"+users.getBookid()+"'")
                self.__connection.commit()
                self.cur.execute("UPDATE books SET book_status=0 WHERE bookid=%s",(users.getBookid(),))
                self.__connection.commit()
                messagebox.showinfo("Success","Book has been returned successfully!",icon='info')
            except:
                messagebox.showerror('Error','Transaction not commit',icon='warning')

    def Deletebook(self,users):
        bid = users.getBookid()
        if (bid != ''):
            try:
                self.cur.execute("DELETE from books where bookid='" + users.getBookid() + "'")
                self.__connection.commit()
                self.cur.execute("DELETE from issuedbooks where bookid='" + users.getBookid() + "'")
                self.__connection.commit()
                messagebox.showinfo("Success", "Book has been Deleted successfully!", icon='info')
            except:
                messagebox.showerror('Error', 'Transaction not commit', icon='warning')


    def Removemember(self,users):
        uid = users.getUserid()
        if (uid != ''):
            try:
                self.cur.execute("DELETE from member where userid='" + users.getUserid() + "'")
                self.__connection.commit()
                self.cur.execute("DELETE from issuebooks where userid='" + users.getUserid() + "'")
                self.__connection.commit()
                messagebox.showinfo("Success", "Member has been Removed successfully!", icon='info')
            except:
                messagebox.showerror('Error', 'Transaction not commit', icon='warning')

