import http.server

#module global routing table
routes={}

class Route:
    def __init__(self, path, action, methods=["GET"]):
        self.path=path
        self.action=action
        self.methods=methods

class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.serve("GET")
    def do_PUT(self):
        print("in doPut");
        self.serve("PUT")
    def do_POST(self):
        print("in doPost");
        self.serve("POST")
    def do_DELETE(self):
        print("in doDelete");
        self.serve("DELETE")

    def serve(self, method):
        print("Request path:".format(self.path))
        try:
            global routes
            routing = routes[self.path]
            if method in routing.methods:
                routing.action(self)
            else:
                self.method_not_supported(method)
        except (KeyError):
            self.not_found()

    ###################
    # Error responses #
    ###################
    def method_not_supported(self, method):             
        self.send_response(501)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body>")
        self.wfile.write(b"<h2>501 Method not Supported</h2>")
        message = "<p>Resource {} does not support method {}</p></body></html>".format(self.path, method)
        self.wfile.write(bytes(message, "utf8"))
        
    def not_found(self):             
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body>")
        self.wfile.write(b"<h2>404 Not Found</h2>")
        message = "<p>Resource {} not found</p></body></html>".format(self.path)
        self.wfile.write(bytes(message, "utf8"))

def add_route(route):
    global routes
    routes[route.path]=route
        
def run():
    httpd=http.server.HTTPServer(('',8000), Handler)
    httpd.serve_forever()
    
