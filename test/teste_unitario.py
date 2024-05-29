
import unittest
from src.conversao import celsius_para_fahrenheit

class TestConversao(unittest.TestCase):
    def test_celsius_para_fahrenheit(self):
        self.assertEqual(celsius_para_fahrenheit(0), 32)
        self.assertEqual(celsius_para_fahrenheit(100), 212)
        self.assertEqual(celsius_para_fahrenheit(-40), -40)

if __name__ == '__main__':
    unittest.main()
