import unittest
from tests.homework.d_repetition import tests_repetition 

suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)

if __name__ == "__main__":
    unittest.TextTestRunner().run(suite) 