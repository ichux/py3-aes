import Crypto.Random.random as randomize
import json
import logging
import unittest
import inspect

import aes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BodyTest(unittest.TestCase):
    def setUp(self):
        self.key = str(randomize.getrandbits(256))
        self.nbits = 256

    def test_encrypt(self):
        data = json.dumps({'a': 1})
        response = aes.encrypt(data, self.key, self.nbits)

        logger.info(f"key, {self.key}, generated for function; {inspect.currentframe().f_code.co_name}")
        self.assertIsNotNone(response)

    def test_decrypt(self):
        data = json.dumps({'a': 1})

        response = aes.encrypt(data, self.key, self.nbits)
        response = aes.decrypt(response, self.key, self.nbits)

        logger.info(f"key, {self.key}, generated for function; {inspect.currentframe().f_code.co_name}")
        self.assertEqual(response, data)


if __name__ == '__main__':
    unittest.main()
