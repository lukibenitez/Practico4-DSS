import requests
import sys

def check_xss(host, port):
    url = f'http://{host}:{port}/AltoroJ/search.jsp'
    payload = "<script>alert('Cross Site Scripting')</script>"

    try:
        response = requests.get(url, params={'query': payload})

        # Verificar si la petición fue exitosa
        if response.status_code != 200:
            print(f"Error: {response.status_code} - No se pudo conectar al servidor.")
            sys.exit(1)

        # Verificar si el payload se encuentra en la respuesta
        if payload in response.text:
            print("Vulnerabilidad XSS presente.")
            return 1
        else:
            print("Vulnerabilidad XSS mitigada.")
            return 0

    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión: {e}")
        sys.exit(1)

# Verifica si se proporcionan los argumentos correctos
if len(sys.argv) != 3:
    print("Uso: python3 script.py <host> <port>")
    sys.exit(1)

host = sys.argv[1]
port = sys.argv[2]

# Ejecutar la prueba
exit_code = check_xss(host, port)
sys.exit(exit_code)
