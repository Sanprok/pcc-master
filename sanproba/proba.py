import unittest
from test import form_name


class TestName(unittest.TestCase):
    def test_first(self):
        a = form_name('небишь', 'сергей')
        self.assertEqual(a, 'Небишь Сергей')
if __name__ == '__main__':
    unittest.main()

