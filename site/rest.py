import web
import json
from lib2to3 import refactor
        
FIXES_MODULE = "lib2to3.fixes"

urls = (
    '/convert', 'Converter'
)

app = web.application(urls, globals())

class Converter(object):        
    
    def GET(self):
        """Converts `code` passed in http request 
        from python2 to python3"""

        code = web.input(code = '').code
        res = {'py2' : code}
        res['py3'] = unicode(convert(code + '\n'))[:-1]
        return json.dumps(res)

def convert(code):
    """Converts `code` string from python2 to python3"""

    fixes = [FIXES_MODULE + "." + f for f in 
        refactor.get_all_fix_names(FIXES_MODULE, False)]
    tool = refactor.RefactoringTool(fixes)
    return tool.refactor_string(code, "some description")

if __name__ == "__main__":
    app.run()
