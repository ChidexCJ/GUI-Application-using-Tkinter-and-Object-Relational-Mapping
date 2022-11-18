import unittest
from sales_database import *


class Testdatabase(unittest.TestCase):
    # instantiate object of database class
    data = Database()

    def test_insert(self):
        """tests for inserting value in database"""
        a = True
        self.assertTrue(a, data.insert('abc', 'fuel pump', 'john', 'lagos', 5000, 20))

    def test_fetch(self):
        """tests for select statements"""
        b = True
        self.assertTrue(b, data.fetch())

    def test_update(self):
        """tests for row update"""
        c = True
        self.assertTrue(c, data.update(2, 'abc', 'valve', 'john', 'lagos', 5000, 30))

    def test_remove(self):
        """tests for entry removal"""
        d = True
        self.assertTrue(d, data.remove('8'))



if __name__ == '__main__':
    unittest.main()
