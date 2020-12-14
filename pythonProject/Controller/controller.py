
class users:

    def __init__(self):
        pass
    __userid=0
    __username=""
    __password=""
    __fname=""
    __lname=""
    __email=""
    __contact=""
    __date=""
    __address=""
    __message=""
    __bookid=0
    __bookname=""
    __author=""
    __edition=""
    __published=""
    __publisher=""
    __dateRegistered=""




    #Settters
    def setUsername(self,param):
        self.__username=param
    def setPassword(self,param):
        self.__password=param
    def setFname(self,param):
        self.__fname=param
    def setLname(self,param):
        self.__lname=param
    def setEmail(self,param):
        self.__email=param
    def setContact(self,param):
        self.__contact=param
    def setDate(self,param):
        self.__date=param
    def setAddress(self,param):
        self.__address=param
    def setUserid(self,param):
        self.__userid=param
    def setDateRegistered(self,param):
        self.__dateRegistered=param
    def setMessage(self,param):
        self.__message=param
    def setBookid(self,param):
        self.__bookid=param
    def setBookname(self,param):
        self.__bookname=param
    def setAuthor(self,param):
        self.__author=param
    def setEdition(self,param):
        self.__edition=param
    def setPublished(self,param):
        self.__published=param
    def setPublisher(self,param):
        self.__publisher=param



    #Getters
    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password
    def getFname(self):
        return self.__fname
    def getLName(self):
        return self.__lname
    def getEmail(self):
        return self.__email
    def getContact(self):
        return self.__contact
    def getDate(self):
        return self.__date
    def getAddress(self):
        return self.__address
    def getUserid(self):
        return self.__userid
    def getMessage(self):
        return self.__message
    def getRegistered(self):
        return self.__dateRegistered
    def getBookid(self):
        return self.__bookid
    def getBookname(self):
        return self.__bookname
    def getAuthor(self):
        return self.__author
    def getEdition(self):
        return self.__edition
    def getPublished(self):
        return self.__published
    def getPublisher(self):
        return self.__publisher



