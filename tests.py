import unittest
from bank import Person, Client, Account
from datetime import *

class TestPersonFullName(unittest.TestCase):

  def setUp(self):
    self.person = Person(1, "Olivier", "LON")

  def testFullName(self):
    self.assertEqual("Olivier LON", self.person.getFullName())

class TestClientDateJoint(unittest.TestCase):

  def setUp(self):
    self.client = Client(1, "2017/09/21", 1, "Olivier", "LON")

  def testIsJoint(self):
    #print(self.client.date_joint)
    dateClient = datetime.strptime(self.client.getDateJoint(), "%Y/%m/%d")
    before = datetime.strptime("2016/12/21", "%Y/%m/%d") - dateClient
    after = dateClient - datetime.now()
    self.assertEqual((bool(before.days), bool(after.days)), (True, True))

class TestAccountOverdraft(unittest.TestCase):

  def setUp(self):
    self.client = Client(1, "2017-09-21", 1, "Olivier", "LON")
    self.account = Account(1, self.client)

  def testIsOverdraft(self):
    plus = self.account.overdraft is False
    self.account.withdraw(200)
    minus = self.account.overdraft is False
    self.assertEqual((plus, minus), (True, True))

if __name__ == '__main__':
    unittest.main()
