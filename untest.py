import unittest
import validate



class TestStringMethods(unittest.TestCase):
    def test_checksum_function(self):
        self.assertEqual(validate.hashlib_md5('fakefile.txt'), 'e7df7cd2ca07f4f1ab415d457a6e1c13')


if __name__ == '__main__':
    unittest.main(verbosity=2)

   

