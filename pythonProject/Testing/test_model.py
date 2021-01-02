import unittest
from Model import model as m
from Controller import controller as c
from Model.dbCon import Mysql



class TestModel(unittest.TestCase):
    __connection=None

    @classmethod
    def setUpClass(cls):
        print("Set Up Class")
    @classmethod
    def tearDownClass(cls):
        print("Tear Down Class")

    def setUp(self):
        self.__connection=Mysql.Connect()
        self.cur=self.__connection.cursor()
        self.user=c.users()
        self.model=m.account()
        self.user.setBookname("Ma")
        self.user.setAuthor("Anisul")
        self.user.setEdition("n/a")
        self.user.setPublished("n/a")
        self.user.setPublisher("n/a")
    def tearDown(self):
        print("tear Down")

    """def test_Login(self):
        self.assertEqual(self.account.Login(self.self.user), True)"""

    def test_addBook(self):
        self.assertEqual(self.model.addBook(self.user), True)




if __name__ == '__main__':
    unittest.main()
