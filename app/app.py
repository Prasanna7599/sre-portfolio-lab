import os
from http.server import BaseHTTPRequestHandler, HTTPServer
VERSION = os.environ.get("APP_VERSION", "dev")[:7]
 
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            status = 200
            body = b"ok"
        else:
            status = 200
            body = ("SRE portfolio V2, version " + VERSION).encode()
 
        self.send_response(status)
        self.end_headers()
        self.wfile.write(body)
 
HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
