from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        if parsed_url.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Hello User</title>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body>
                <h1>Enter Your Name</h1>
                <input type="text" id="username" placeholder="Your Name">
                <button id="submitBtn">Submit</button>

                <script>
                document.getElementById('submitBtn').addEventListener('click', function() {
                    const username = document.getElementById('username').value;
                    window.location.href = '/hello?name=' + encodeURIComponent(username);
                });
                </script>
                <p>Repo: <a href="https://github.com/yusufmalikul/python-hello-world" _target="_blank">https://github.com/yusufmalikul/python-hello-world</p>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
        elif parsed_url.path == '/hello' and 'name' in query_params:
            name = query_params['name'][0]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Hello User</title>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body>
                <h1>Hello, {name}!</h1>
            <p>Repo: <a href="https://github.com/yusufmalikul/python-hello-world" _target="_blank">https://github.com/yusufmalikul/python-hello-world</p>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('404 Not Found'.encode('utf-8'))
        return