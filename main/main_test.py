import main

from unittest.mock import patch
import unittest

class Test(unittest.TestCase):
    def test(self):
        user_input = ["https://en.wikipedia.org/wiki/Python_(programming_language)",0,"h1 id.*?h1\\>",1,"(h1.*?>|<\\/h1>)","",2]

        with patch('builtins.input', side_effect=user_input):
            test = main.PyParser()

if __name__ == '__main__':
    unittest.main()