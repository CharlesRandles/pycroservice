#!/usr/bin/python3

import microservice as ms

def serve_root(request):
    request.send_response(200)
    request.send_header('Content-type', 'text/html')
    request.end_headers()
    request.send("<html><body><h1>Hello! I am your shiny microservice!</h1></body></html>")

ms.set_host('0.0.0.0')
ms.set_port(80)
ms.add_route('/', serve_root)
ms.run()
