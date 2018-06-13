import http.server
import threading
from socketserver import ThreadingMixIn
#module global routing table
routes={}

#Useful 'constants' for caller
GET=['GET']
PUT=['PUT']
POST=['POST']
DELETE=['DELETE']

#Default server settings
HOST='localhost'
PORT=8080

class Action:
    def __init__(self, action, methods):
        self.action, self.methods=action, methods

class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
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

    def send(self, content):
        self.wfile.write(bytes(content, "utf8"))
        
    def serve(self):
        try:
            global routes
            routing = routes[self.path]
            if self.command in routing.methods:
               routing.action(self)
            else:
                self.method_not_supported(method)
        except (KeyError):
            self.not_found()

    ###################
    # Error responses #
    ###################
    def method_not_supported(self):             
        self.send_response(501)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.send("<html><body>")
        self.send("<h2>501 Method not Supported</h2>")
        message = "<p>Resource {} does not support method {}</p></body></html>".format(self.path, self.command)
        self.send(message)
        
    def not_found(self):             
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.send("<html><body>")
        self.send("<h2>404 Not Found</h2>")
        message = "<p>Resource {} not found</p></body></html>".format(self.path)
        self.send(message)

def log(message):
    print(message)

def set_host(host):
    global HOST
    HOST=host

def set_port(port):
    global PORT
    PORT=port
        
def add_route(path, action, methods=GET):
    global routes
    routes[path]=Action(action, methods)

class ThreadedHTTPServer(ThreadingMixIn, http.server.HTTPServer):
    #Passes requests to a new thread
    pass
    
def run():
    log("starting microserver at {} on port {}".format(HOST, PORT))
    httpd=ThreadedHTTPServer((HOST, PORT), Handler)
    httpd.serve_forever()
