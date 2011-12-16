import web
import json
from lib2to3 import refactor
from lib2to3.pgen2.parse import ParseError
from lib2to3.pgen2.tokenize import TokenError
        
FIXES_MODULE = "lib2to3.fixes"

urls = (
    "/convert", "Converter"
)

app = web.application(urls, globals())

class Converter(object):        
    
    def GET(self):
        """Convert `code` passed in http request 
        from python2 to python3
        """
        code = web.input(code = "").code
        res = {"py2" : code}
        try:
            res["py3"] = unicode(convert(code + "\n"))[:-1]
        except (TokenError, ParseError) as e:
            res["py3"] = ""
            res["error"] = unicode(e)
        js = json.dumps(res)

        callback = web.input(callback = "").callback
        if callback:
            return callback + "(" + js + ")"

        return js


def convert(code):
    """Convert `code` string from python2 to python3"""
    fixes = [FIXES_MODULE + "." + f for f in 
        refactor.get_all_fix_names(FIXES_MODULE, False)]
    tool = refactor.RefactoringTool(fixes)
    return tool.refactor_string(code, "some description")

if __name__ == "__main__":
    app.run()
