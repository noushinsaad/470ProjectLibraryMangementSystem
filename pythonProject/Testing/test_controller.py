import unittest
from Controller import controller as c



class TestController(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        pass

    @classmethod
    def tearDownClass(cls) :
        pass

    def setUp(self):
        self.u=c.users()

    def tearDown(self):
        pass

    def test_getUsername(self):
        self.u.setUsername("SAAD")
        self.assertEqual(self.u.getUsername(),"SAAD")
    def test_getPassword(self):
        self.u.setPassword("12345")
        self.assertEqual(self.u.getPassword(),"12345")
    def test_getFname(self):
        self.u.setFname("Noushin")
        self.assertEqual(self.u.getFname(),"Noushin")

    def test_getLname(self):
        self.u.setLname("Islam")
        self.assertEqual(self.u.getLName(),"Islam")
    def test_getEmail(self):
        self.u.setEmail("noushin@gmail.com")
        self.assertEqual(self.u.getEmail(),"noushin@gmail.com")
    def test_getContact(self):
        self.u.setContact("01711111111")
        self.assertEqual(self.u.getContact(),"01711111111")
    def test_getRegistered(self):
        self.u.setDateRegistered("12-15-2020")
        self.assertEqual(self.u.getRegistered(),"12-15-2020")

    def test_getUserid(self):
        self.u.setUserid("1")
        self.assertEqual(self.u.getUserid(),"1")
    def test_getBookid(self):
        self.u.setBookid("1")
        self.assertEqual(self.u.getBookid(),"1")
    def test_getBookname(self):
        self.u.setBookname("Ma")
        self.assertEqual(self.u.getBookname(),"Ma")
    def test_getAuthor(self):
        self.u.setAuthor("Anisul")
        self.assertEqual(self.u.getAuthor(),"Anisul")

    def test_getEdition(self):
        self.u.setEdition("n/a")
        self.assertEqual(self.u.getEdition(),"n/a")
    def test_getPublished(self):
        self.u.setPublished("n/a")
        self.assertEqual(self.u.getPublished(),"n/a")
    def test_getPublisher(self):
        self.u.setPublisher("n/a")
        self.assertEqual(self.u.getPublisher(),"n/a")



if __name__ == '__main__':
    unittest.main()
