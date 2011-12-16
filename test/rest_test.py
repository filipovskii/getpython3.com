import json
import unittest
from modules import rest

class TestRestConverter(unittest.TestCase):

    def setUp(self):
        self.o = rest.Converter() # testee

    def blank_code(self):
        mock_web_input("")
        result = json.loads(self.o.GET())
        self.assertEquals("", result["py3"])

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

    def test_jsonp_request(self):
        cb = "callback-name"
        mock_web_input("print 1", "callback-name")
        result = self.o.GET()
        self.assertTrue(result.startswith(cb + "("))
        self.assertTrue(result.endswith(")"))


class MockInp(object):
    """Stub for mocking result of web.input() func"""
    
    def __init__(self, code = "", callback = ""):
        self.code = code
        self.callback = callback


def mock_web_input(code_string, callback = ""):
    rest.web.input = lambda **args: MockInp(code_string, callback)


if __name__ == '__main__':
    unittest.main()
