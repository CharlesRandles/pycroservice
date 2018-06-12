import http.server


class Route:
    def init(path, action, methods=["GET"]):
        self.path=path
        self.action=action
        self.methods=methods

class Microserver:
    def __init__(self):
        self._routes={}

    def addRoute(self, route):
        self._routes[route.path]=route

    def run(self);
        
class Handler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        print("in doGet");
        self.serve()
    def do_PUT(self):
        print("in doPut");
        self.serve()
    def do_POST(self):
        print("in doPost");
        self.serve()
    def do_DELETE(self):
        print("in doDelete");
        self.serve()

    def serve(self):
        print("Request path:".format(self.path))
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello!")
    
        
def run():
    httpd=http.server.HTTPServer(('',8000), Handler)
    httpd.serve_forever()
    
