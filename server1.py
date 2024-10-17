from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse as parse

class MyHandler(SimpleHTTPRequestHandler):
    # Simulación de un "login" vulnerable a inyección SQL
    def do_POST(self):
        if '/AltoroJ/doLogin' in self.path:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = parse.parse_qs(post_data)

            # Simulamos un comportamiento vulnerable: no se usa parametrización
            username = params.get('uid', [''])[0]
            password = params.get('passw', [''])[0]

            # Inyección SQL permitida: bypass de autenticación
            if username == "admin' or 1=1 --" or (username == 'admin' and password == 'admin'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'Login exitoso.')
            else:
                self.send_response(401)
                self.end_headers()
                self.wfile.write(b'Login fallido.')
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=MyHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
