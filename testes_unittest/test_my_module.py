# verbosity=2 (verbose)
# verbosity=1 (default)
# verbosity=0 (quiet)

import my_module
import unittest

class teste(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(my_module.soma(1,1), 2)
    
    def test_divide(self):
        self.assertEqual(my_module.divide(2, 1), 2)

    def test_divide(self):
        with self.assertRaises(ValueError):
            my_module.divide(2, 0)

# sintax para quando 
if __name__ == '__main__':
    unittest.main(verbosity=2)
