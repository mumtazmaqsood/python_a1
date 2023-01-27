
import unittest
from fun import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'fun.py'"""
    def test_first_last_name(self):
        """Do names like 'Mumtaz Maqasood' works?"""
        formatted_name = get_formatted_name('Mumtaz', 'Maqsood')
        self.assertEqual(formatted_name, 'Mumtaz Maqsood')

# #what is the behaviour if user given numbers values
#     def test_given_number_value(self):
#         self.assertEqual(get_formatted_name(123,456), '123 456')

if __name__ == '__main__':
    unittest.main()