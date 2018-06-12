#!/usr/bin/python3

"""
A Page Counting microservice
"""

import microservice as ms
import json

COUNT=0

def serve_count(request):
    global COUNT
    COUNT += 1
    request.send_response(200)
    request.send_header('Content-type', 'application/json')
    request.end_headers()
    request.send(json.dumps({'count': COUNT}))

ms.set_port(8080)
ms.add_route('/', serve_count)
ms.run()
