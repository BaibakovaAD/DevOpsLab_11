"""Sumple HTTP server module for DevOpsLab_11"""

import http.server
import socketserver

PORT = 8000

class TestMe():
    """Test class for demonstration purposes"""

    def take_five(self):
        """Return the server port number"""
        return 5

    def port(self):
        """Return the server port number"""
        return PORT

if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()
