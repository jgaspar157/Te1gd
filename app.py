import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = int(os.getenv("PORT", 3000))

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Custom response handling can be added here if necessary
        if self.path == "/":
            self.path = "templates/index.html"  # Serve index.html for root path
        return super().do_GET()

if __name__ == "__main__":
    with TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
