# Entorno sin vulnerabilidad de ataques XSS

from http.server import SimpleHTTPRequestHandler, HTTPServer
import html

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if '/search.jsp' in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # Escapar los caracteres especiales del parámetro query
            query = self.path.split('=')[1] if '=' in self.path else ''
            escaped_query = html.escape(query)  # Escapar para prevenir XSS
            
            response_content = f"<html><body><h1>Resultados</h1><p>{escaped_query}</p></body></html>"
            self.wfile.write(response_content.encode('utf-8'))
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
