from tkinter import *
from tkinter import ttk
from Model.dbCon import Mysql
from View import members as m
from View import books as b
from View import issuebook as i
from View import Return as r
from View import delete as d
from View import removeMember as rm
con = Mysql.Connect()
cur = con.cursor()


class System(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("1300x900")
        self.title("Library Management System")
        self.resizable(True,True)

        #==========================================================

        self.main_frame = Frame(self)
        self.main_frame.pack()

        self.top_frame = Frame(self.main_frame, width=900, height=70, borderwidth=2, relief=SUNKEN, padx=20)
        self.top_frame.pack(side=TOP, fill=X)

        self.btn_add_member = Button(self.top_frame, text="Add New Member", font="arial 12 bold", padx=10,command=self.new_member)
        self.btn_add_member.pack(side=LEFT)

        self.btn_add_book = Button(self.top_frame, text="Add New Book", font="arial 12 bold", padx=10,command=self.add_book)
        self.btn_add_book.pack(side=LEFT)

        self.btn_issue_book = Button(self.top_frame, text="Issue Book", font="arial 12 bold", padx=10,command=self.issue_book)
        self.btn_issue_book.pack(side=LEFT)

        self.btn_issue_book = Button(self.top_frame, text="Return Book", font="arial 12 bold", padx=10,command=self.return_book)
        self.btn_issue_book.pack(side=LEFT)

        self.btn_issue_book = Button(self.top_frame, text="Delete Book", font="arial 12 bold", padx=10,command=self.delete_book)
        self.btn_issue_book.pack(side=LEFT)

        self.btn_issue_book = Button(self.top_frame, text="Remove Member", font="arial 12 bold", padx=10,command=self.remove_member)
        self.btn_issue_book.pack(side=LEFT)


        self.centre_frame = Frame(self.main_frame, width=900, height=800, relief=RIDGE)
        self.centre_frame.pack(side=TOP)

        self.left_frame = Frame(self.centre_frame, width=800, height=700, relief=SUNKEN, borderwidth=2)
        self.left_frame.pack(side=LEFT)

        self.leftab = ttk.Notebook(self.left_frame, width=600, height=600)
        self.leftab.pack()

        self.tab1 = ttk.Frame(self.leftab)
        self.tab2 = ttk.Frame(self.leftab)
        self.tab3 = ttk.Frame(self.leftab)
        self.leftab.add(self.tab1, text='Book Management')
        self.leftab.add(self.tab2, text='Member Management')
        self.leftab.add(self.tab3, text='Summary')


        # List Box (in left frame)
        #Book Management
        self.management_box = Listbox(self.tab1, width=40, height=30, font='times 12 bold')
        self.scroll = Scrollbar(self.tab1, orient=VERTICAL)
        self.management_box.grid(row=0, column=0, padx=(10, 0), pady=10, sticky=N)
        self.scroll.config(command=self.management_box.yview)
        self.management_box.config(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0, column=0, sticky=N + S + E)

        self.list_details = Listbox(self.tab1, width=80, height=30, font='times 12 bold')
        self.list_details.grid(row=0, column=1, padx=(10, 0), pady=10, sticky=N)

        # summary
        self.lbl_book_count = Label(self.tab3, text='', pady=20, font='verdana 14 bold')
        self.lbl_book_count.grid(row=0)
        self.lbl_member_counter = Label(self.tab3, text='', pady=20, font='verdana 14 bold')
        self.lbl_member_counter.grid(row=1, sticky=W)
        self.lbl_taken_count = Label(self.tab3, text='', pady=20, font='verdana 14 bold')
        self.lbl_taken_count.grid(row=2, sticky=W)

        # Right Frame
        self.right_frame = Frame(self.centre_frame, width=300, height=700, relief=SUNKEN, borderwidth=2)
        self.right_frame.pack()

        self.searchbar = LabelFrame(self.right_frame, width=250, height=75, text="Search")
        self.searchbar.pack()
        # '''
        # Search Bar (In Right Frame)
        self.label_search = Label(self.searchbar, text='Search Book', font='arial 12 bold')
        self.label_search.grid(row=0, column=0, padx=20, pady=10)

        self.ent_search = Entry(self.searchbar, width=30, bd=10)
        self.ent_search.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        self.btn_search = Button(self.searchbar, text='Search Now', font='arial 12',command=self.search)
        self.btn_search.grid(row=0, column=4, padx=20, pady=10)

        # List Box (In Right Frame)
        self.list_bar = LabelFrame(self.right_frame, width=280, height=200, text='Books List', bg="#fff")
        self.list_bar.pack(fill=BOTH)
        self.list_label = Label(self.list_bar, text="Sort by:", font="times 16")
        self.list_label.grid(row=0, column=2)

        self.list_choice = IntVar()

        # Radio Buttons

        self.rbtn_all_books = Radiobutton(self.list_bar, text='Sort all books', var=self.list_choice, value=1)
        self.rbtn_all_books.grid(row=1, column=0)
        self.rbtn_instock = Radiobutton(self.list_bar, text='Books available', var=self.list_choice, value=2)
        self.rbtn_instock.grid(row=1, column=1)
        self.rbtn_issued_books = Radiobutton(self.list_bar, text='Books issued', var=self.list_choice, value=3)
        self.rbtn_issued_books.grid(row=1, column=2)

        self.btn_show_books = Button(self.list_bar, text='Show books', font='arial 12 bold',command = self.searchsort)
        self.btn_show_books.grid(row=1, column=3, padx=40, pady=10)

        self.btn_refresh = Button(self.list_bar, text='Refresh', font='aria 12 bold', command=self.Refresh)
        self.btn_refresh.grid(row=1, column=4, padx=40, pady=10)

        self.welcome_image = Frame(self.right_frame, width=300, height=400)
        self.welcome_image.pack(fill=BOTH)
        self.welcome_main_image = PhotoImage(file='intro.png')
        self.image_label = Label(self.welcome_image, image=self.welcome_main_image)
        self.image_label.grid(row=1)


    def showbooks(self):
        counter = 0
        cur.execute("SELECT * FROM books")
        books = cur.fetchall()
        for book in books:
            self.management_box.insert(counter, str(book[0]) + '-' + book[1])
            counter += 1

        def bookinfo(evt):
            con = Mysql.Connect()
            cur = con.cursor()
            value = str(self.management_box.get(self.management_box.curselection()))
            id = value.split('-')[0]
            self.list_details.delete(0, 'end')

            cur.execute("SELECT * FROM books WHERE bookid='" + id + "'")
            book_info = cur.fetchall()
            self.list_details.insert(0, 'Book Name:' + book_info[0][1])
            self.list_details.insert(1, 'Author:' + book_info[0][2])
            self.list_details.insert(2, 'Edition:' + book_info[0][3])

            if book_info[0][6] == 0:
                self.list_details.insert(3, 'Status: In Stock')
            else:
                self.list_details.insert(3, 'Status: Not in stock')

        self.management_box.bind('<<ListboxSelect>>', bookinfo)

    def Refresh(self):
        self.showsummary()
        self.showmember()
        #self.showbooks()

    #====================================================================
    def showsummary(self):
        con = Mysql.Connect()
        cur = con.cursor()

        cur.execute("SELECT COUNT(bookid) FROM books WHERE book_status=0")
        book_instock_counter = cur.fetchall()
        self.lbl_book_count.config(text="IN STOCK: " + str(book_instock_counter[0][0]))
        cur.execute("SELECT COUNT(userid) FROM member")
        member_counter = cur.fetchall()
        self.lbl_member_counter.config(text="MEMBERS: " + str(member_counter[0][0]))
        cur.execute("SELECT COUNT(bookid) FROM books WHERE book_status=1")
        issued_counter = cur.fetchall()
        self.lbl_taken_count.config(text="ISSUED: " + str(issued_counter[0][0]))

    def searchsort(self):
        """
            Sorting all the books on the basis of radio button
            selected by the user
        """
        con = Mysql.Connect()
        cur = con.cursor()
        value = self.list_choice.get()
        query = ''
        if value == 1:
            query = "SELECT * FROM books ORDER BY bookname"

        elif value == 2:
            query = "SELECT * FROM books WHERE book_status = 0"

        else:
            query = "SELECT * FROM books WHERE book_status = 1"

        self.management_box.delete(0, END)
        counter = 0
        cur.execute(query)
        searchquery =  cur.fetchall()
        for book in searchquery:
            self.management_box.insert(counter, str(book[0]) + '-' + str(book[1]))
            counter += 1

    #=============================================================

    def search(self):
        """
            For searching book in the Library
        """
        con = Mysql.Connect()
        cur = con.cursor()
        value = self.ent_search.get()
        query ="SELECT * FROM books WHERE bookname LIKE %s"
        cur.execute(query,("%"+value+"%",))
        searchquery = cur.fetchall()
        self.management_box.delete(0,END)
        counter = 0
        for book in searchquery:
            self.management_box.insert(counter, str(book[0])+'-'+str(book[1]))
            counter += 1

    #=============================================================



    # ==========================================================
    def showmember(self):
        self.member_management_box = ttk.Treeview(self.tab2, height=30,columns=("uname", "fname", "lname", "email", "contact"))
        self.mscroll = Scrollbar(self.tab2, orient=VERTICAL)
        self.member_management_box.grid(row=0, column=0, padx=(10, 0), pady=10, sticky=N)
        self.mscroll.config(command=self.member_management_box.yview)
        self.member_management_box.config(yscrollcommand=self.mscroll.set)
        self.mscroll.grid(row=0, column=0, sticky=N + S + E)

        self.member_management_box.heading("uname", text="User Name")
        self.member_management_box.heading("fname", text="First Name")
        self.member_management_box.heading("lname", text="Last Name")
        self.member_management_box.heading("email", text="Email")
        self.member_management_box.heading("contact", text="Contact")

        self.member_management_box['show'] = 'headings'

        self.member_management_box.column("uname", width=70)
        self.member_management_box.column("fname", width=70)
        self.member_management_box.column("lname", width=70)
        self.member_management_box.column("email", width=50)
        self.member_management_box.column("contact", width=70)


        con = Mysql.Connect()
        cur = con.cursor()
        cur.execute("SELECT username,fname,lname,email,contact FROM member")
        members = cur.fetchall()
        for member in members:
            self.member_management_box.insert('', END, values=member)
            con.commit()


    # ===========================================================
    def new_member(self):
        m.StoreMember()
    def add_book(self):
        b.StoreBook()
    def issue_book(self):
        i.IssueBook()
    def return_book(self):
        r.ReturnBook()
    def delete_book(self):
        d.DeleteBook()
    def remove_member(self):
        rm.RemoveMember()
   #============================================================