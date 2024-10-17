# Proyecto 4

Este proyecto contiene dos scripts de pruebas de seguridad diseñados para verificar la existencia de vulnerabilidades en un sistema de inicio de sesión, específicamente Inyección SQL y Cross-Site Scripting (XSS). Se han implementado dos versiones de entornos para cada script: uno vulnerable y uno con la vulnerabilidad mitigada, simulando un entorno real para practicar pruebas de seguridad.

## Índice
- [Descripción](#descripción)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Ejecución](#ejecución)

## Descripción

Este proyecto tiene como objetivo demostrar y practicar pruebas de seguridad en aplicaciones web. Utiliza un servidor Python que simula un entorno web vulnerable a ataques comunes como inyección SQL y Cross-Site Scripting (XSS), así como las versiones mitigadas de estas vulnerabilidades. Los scripts permiten comprobar si una vulnerabilidad está presente o ha sido mitigada correctamente.

## Requisitos

- Python 3.12 o superior.
- Biblioteca `requests` (para las pruebas).
    ```bash
    pip install requests
    ```


## Instalación

1. Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/lukibenitez/Practico4-DSS.git
    ```

2. Acceder al proyecto:
    ```bash
    cd practico-dss-seguridad
    ```

3. Hemos decidido ejecutar este proyecto en un entorno virtual para aislar las dependencias:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

## Ejecución

Para probar las vulnerabilidades, necesitarás abrir dos terminales:

- **Terminal 1**: Inicia el servidor (vulnerable o mitigado). En la primera terminal, ejecuta uno de los siguientes comandos según el entorno que desees probar:
    
    - Para iniciar el **servidor vulnerable a inyección SQL** (simulado por `server1.py`):
        ```bash
        python3 server1.py
        ```

    - Para iniciar el **servidor mitigado contra inyección SQL** (simulado por `server2.py`):
        ```bash
        python3 server2.py
        ```

    - Para iniciar el **servidor vulnerable a XSS** (simulado por `server3.py`):
        ```bash
        python3 server3.py
        ```

    - Para iniciar el **servidor mitigado contra XSS** (simulado por `server4.py`):
        ```bash
        python3 server4.py
        ```

- **Terminal 2**: Ejecuta el script de prueba. En la segunda terminal, ejecuta el script correspondiente para verificar si la vulnerabilidad está presente o mitigada:
    
    - Para probar inyección SQL:
    ```bash
    python3 script1.py localhost 8080
    ```
    - Para probar Cross-Site Scripting (XSS):
    ```bash
    python3 script2.py localhost 8080
    ```

4. **Interpretación de los resultados**:

- **Inyección SQL**:
  - Si la vulnerabilidad de inyección SQL está **presente**, el script devolverá `1`.
  - Si la vulnerabilidad está **mitigada**, el script devolverá `0`.

- **XSS**:
  - Si la vulnerabilidad de XSS está **presente**, el script devolverá `1`.
  - Si la vulnerabilidad está **mitigada**, el script devolverá `0`.

Además, hemos añadido mensajes informativos al script para que sea más amigable. Cuando ejecutes los scripts de prueba, verás un mensaje que indicará si la vulnerabilidad aún está presente o si ha sido mitigada exitosamente, lo que te ayudará a interpretar los resultados de manera más clara y rápida.

