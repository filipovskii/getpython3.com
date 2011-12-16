import json
import unittest
from modules import rest

class TestRestConverter(unittest.TestCase):

    def setUp(self):
        self.o = rest.Converter() # testee


    def test_simple_example(self):
        mock_web_input("print 1")
        result = json.loads(self.o.GET())
        self.assertEqual("print(1)", result["py3"])

    def test_parse_error_handle(self):
        mock_web_input("print 1 !")
        result = json.loads(self.o.GET())
        self.assertEqual("", result["py3"])
        self.assertTrue(len(result["error"]) > 1)

    def test_token_error_handle(self):
        mock_web_input("print ( 1")
        result = json.loads(self.o.GET())
        self.assertEqual("", result["py3"])
        self.assertTrue(len(result["error"]) > 1)


class MockInp(object):
    """Stub for mocking result of web.input() func"""
    
    def __init__(self, code = ""):
        self.code = code


def mock_web_input(code_string):
    rest.web.input = lambda **args: MockInp(code_string)


if __name__ == '__main__':
    unittest.main()
