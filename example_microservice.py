#!/usr/bin/python3

import microservice

def serve_root(request):
    request.send_response(200)
    request.send_header('Content-type', 'text/html')
    request.end_headers()
    request.wfile.write(bytes("<html><body><h1>Hello! I am your shiny microservice!</h1></body></html>", "utf8"))

root = microservice.Route('/', serve_root, ['GET'])

microservice.add_route(root)
microservice.run()
