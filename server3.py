# Entorno vulnerable a ataques XSS

from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if '/search.jsp' in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Simulamos una respuesta con vulnerabilidad XSS
            self.wfile.write(b"<html><body><h1>Resultados</h1><p><script>alert('Cross Site Scripting')</script></p></body></html>")
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
