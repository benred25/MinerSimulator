import unittest
from datetime import datetime
from Miner.UserID import UserID

class TestUserID (unittest.TestCase):

    @classmethod
    def setUp(self):
        self.user_1 = UserID("Adrian")
        self.user_2 = UserID("Maicaella")
        self.user_3 = UserID("Hassel")

    @classmethod
    def tearDown(self):
        # This will be useful, when handling database
        pass

    def test_getName(self):
        self.assertEqual(self.user_1.getName(), "Adrian")
        self.assertEqual(self.user_2.getName(), "Maicaella")
        self.assertEqual(self.user_3.getName(), "Hassel")

    def test_setName(self):
        self.user_1.setName("Josh")
        self.user_2.setName("Alanna")
        self.user_3.setName("Aubrey")

        self.assertEqual(self.user_1.getName(), "Josh")
        self.assertEqual(self.user_2.getName(), "Alanna")
        self.assertEqual(self.user_3.getName(), "Aubrey")

    def test_getStartDate(self):
        self.assertEqual(self.user_1.getStartDate(), datetime.now().date().today())
        self.assertEqual(self.user_2.getStartDate(), datetime.now().date().today())
        self.assertEqual(self.user_3.getStartDate(), datetime.now().date().today())

if __name__ == '__main__':
    unittest.main()