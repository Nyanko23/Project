import unittest

#class TestMyProgram(unittest.TestCase):

#    def test_upper(self):
#        self.assertEqual('foo'.upper(), 'FOO')
#
#    def test_isupper(self):
#        self.assertTrue('FOO'.isupper())
#        self.assertFalse('Foo'.isupper())

#if __name__ == '_main_':
#   unittest.main()

# Write a simple Unit Testing myProgram and executing the test script
import myProgram as prog

class TestMyProgram(unittest.TestCase):

    def test_EngineType(self):
        vios = prog.vehicle('4', 'petrol', 5, 180)
        self.assertEqual(vios.types_of_tanks, 'petrol')

if __name__ == '_main_':
    unittest.main()
