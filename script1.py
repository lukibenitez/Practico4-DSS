import requests
import sys

def check_sql_injection(host, port):
    url = f'http://{host}:{port}/AltoroJ/doLogin'
    session = requests.Session()

    # Inyección SQL típica
    username = "admin' or 1=1 --"
    password = "cualquierpassword"

    # Datos enviados como formulario, no JSON
    payload = {
        "uid": username,
        "passw": password
    }

    try:
        # Cambiar a data=payload para enviar como application/x-www-form-urlencoded
        response = session.post(url, data=payload)

        # Verificar si la petición fue exitosa (es decir, si la respuesta no es 401)
        if response.status_code == 401:
            print(f"Error: {response.status_code} - No se pudo conectar al servidor.")
            return 0

        # Verificar la respuesta si la inyección SQL fue exitosa
        if 'Login fallido' in response.text:
            print("Inyección SQL no exitosa (vulnerabilidad mitigada).")
            return 0
        else:
            print("Inyección SQL exitosa (vulnerabilidad presente).")
            return 1

    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión: {e}")
        sys.exit(1)

# Verifica si se proporcionan los argumentos correctos
if len(sys.argv) != 3:
    print("Uso: python3 script1.py <host> <port>")
    sys.exit(1)

host = sys.argv[1]
port = sys.argv[2]

# Ejecutar la prueba
exit_code = check_sql_injection(host, port)
sys.exit(exit_code)
