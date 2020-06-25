#!/usr/bin/env python
"""

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

Author: Bhaskar Tallamraju
Description: Very simple HTTP server in python 3 or greater. 
             Receives JSON and writes it to a file
 
Usage::
    ./pywebserv.py [<port>]

SAMPLE commands to POST using curl
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
from datetime import datetime
import json
import sys

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(B"<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
	# Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        try:
            parsed = json.loads(post_data)
            print(json.dumps(parsed, indent=4, sort_keys=True))
        except:
            print("EXCEPTION: Invalid JSON! ")

        fileName = "Received" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".txt"
        with open(fileName, "w") as text_file:
            text_file.write("%s" % post_data)
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write(B"<html><body><h1>POST!</h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

def signal_handler(sig, frame):
    print('Exiting ... ')
    sys.exit(0)

if __name__ == "__main__":
    from sys import argv
    import signal
    import sys
    signal.signal(signal.SIGINT, signal_handler)
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
