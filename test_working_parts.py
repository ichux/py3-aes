import json
import unittest

import aes


class BodyTest(unittest.TestCase):
    def setUp(self):
        self.key = '7O86CFBE1563322983CB3515BF62B2652B5495BED15B4D450908B6B223FEE409D512CCB0DC2FB1C891E6329D2143418E'
        self.nbits = 256

    def test_encrypt(self):
        data = json.dumps({'a': 1})
        response = aes.encrypt(data, self.key, self.nbits)
        
        self.assertIsNotNone(response)

    def test_decrypt(self):
        data = json.dumps({'a': 1})

        response = aes.encrypt(data, self.key, self.nbits)
        response = aes.decrypt(response, self.key, self.nbits)
        self.assertEqual(response, data)


if __name__ == '__main__':
    unittest.main()
