import unittest
from calculadora import multiplicar

class TestCalculadora(unittest.TestCase):

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)

if __name__ == "__main__":
    unittest.main()
