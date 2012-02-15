#!/usr/bin/env python3

'''
Written by adisbladis <adis@blad.is>

Licensed under the terms of GPLv3
'''

import http.server
import sys
import argparse

class requestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        if args.f:
            self.send_header('Content-Disposition', 'attachment; filename=%s' % (args.f))
        self.send_header('Content-type', 'application/octet-stream')
        self.end_headers()

        sys.stdin = sys.stdin.detach()
        while True:
            s = sys.stdin.read(512)
            if not s:
                break
            self.wfile.write(s)

parser = argparse.ArgumentParser(description='Httpipe - Reads data from stdin and serves over http')
parser.add_argument('-p', action='store', required=False, type=int, default=8080, help='Port (default: 8080)')
parser.add_argument('-a', action='store', required=False, type=str, default='0.0.0.0', help='Address (default: 0.0.0.0)')
parser.add_argument('-f', action='store', required=False, type=str, default=False, help='Set filename header')
args=parser.parse_args()

httpd = http.server.HTTPServer((args.a,args.p),requestHandler)
httpd.handle_request()
