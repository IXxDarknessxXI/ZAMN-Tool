from cryptography.fernet import Fernet, InvalidToken
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

VERDE = "\033[92m"  
AMARILLO = "\033[93m"
ROJO = "\033[91m"
MORADO = "\033[95m"
RESET = "\033[0m"

zamn =f"""
{MORADO}[Tool Creado por Kurumi Tokisaki/TempestSquad]

{MORADO}(v1.1)
{AMARILLO}

 ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░       ░▒▓████████▓▒░░▒▓██████▓▒░░▒▓██████████████▓▒░░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░           ░▒▓██▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░         ░▒▓██▓▒░  ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░        ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░       ░▒▓██▓▒░    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░        ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░        ░▒▓█▓▒░   ░▒▓██████▓▒░       ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
{AMARILLO}                                                                                                                                               
                                                                                                                                                

"""

while True:
    clear_screen()
    print(zamn)
    print(f"{MORADO}:1: {VERDE}[Encriptar o desencriptar archivos]")
    print(f"{MORADO}:2: {VERDE}[Encriptar o desencriptar mensajes]\n")

    pregunta1 = input(f"{VERDE}[¿Qué opción quieres usar?] (1/2): {MORADO}\n")
    
    if pregunta1 == "1":
        pregunta2 = input(f"\n{VERDE}[¿Deseas usar una clave ya creada por este programa para encriptar o desencriptar?] (s/n): {MORADO}\n").lower()
        if pregunta2 == "s":
            clave1 = input(f"\n{VERDE}[Introduzca la clave]: {MORADO}\n")
            try:
                obj2 = Fernet(clave1.encode())  
            except (ValueError, TypeError):
                input(f"{ROJO}Clave no válida. Asegúrate de que sea una clave Fernet correcta.\n")
                continue  

            cifdif2 = input(f"\n{VERDE}(¿Quieres encriptar o desencriptar el archivo?) [e/d]: {MORADO}\n").lower()
            carpeta = input(f"\n{VERDE}(Escribe la ruta de tu archivo): {MORADO}\n")
            try:
                with open(carpeta, "rb") as file:
                    contenido = file.read()
                    
                    if cifdif2 == "e":
                        contenido_encriptado = obj2.encrypt(contenido)
                        with open(carpeta, "wb") as file:
                            file.write(contenido_encriptado)
                            print(f"\n{ROJO}[Archivo exitosamente encriptado]\n")
                    elif cifdif2 == "d":
                        contenido_desencriptado = obj2.decrypt(contenido)
                        with open(carpeta, "wb") as file:
                            file.write(contenido_desencriptado)
                            print(f"\n{ROJO}[Archivo exitosamente desencriptado]\n")
                    else:
                        print(f"{ROJO}[Opción no valida]")
                        continue
            except FileNotFoundError:
                print(f"{ROJO}[Error] Archivo no encontrado. Verifica la ruta.")
            except InvalidToken:
                print(f"{ROJO}[Error] No se pudo desencriptar el archivo. La clave puede ser incorrecta.")
            except Exception as e:
                print(f"{ROJO}[Error] {e}")

        elif pregunta2 == "n":
            clave = Fernet.generate_key()
            obj2 = Fernet(clave)
            print(f"\n{VERDE}[Clave generada]: {MORADO}{clave.decode()}\n")
            print(f"\n{ROJO}[Guarda esta clave en un bloc de notas o algo, te servirá para encriptar y desencriptar los archivos.]\n")
            cifdif2 = input(f"\n{VERDE}¿Quieres encriptar o desencriptar? [e/d]: {MORADO}\n").lower()
            carpeta = input(f"\n{VERDE}(Escribe la ruta de tu archivo): {MORADO}\n")
            try:
                with open(carpeta, "rb") as file:
                    contenido = file.read()
                    
                    if cifdif2 == "e":
                        contenido_encriptado = obj2.encrypt(contenido)
                        with open(carpeta, "wb") as file:
                            file.write(contenido_encriptado)
                            print(f"\n{ROJO}[Archivo exitosamente encriptado]\n")
                    elif cifdif2 == "d":
                        contenido_desencriptado = obj2.decrypt(contenido)
                        with open(carpeta, "wb") as file:
                            file.write(contenido_desencriptado)
                            print(f"\n{ROJO}[Archivo exitosamente desencriptado]\n")
                    else:
                        input(f"{ROJO}[Opción no valida]\n")
            except FileNotFoundError:
                print(f"{ROJO}[Error] Archivo no encontrado. Verifica la ruta.\n")
            except InvalidToken:
                print(f"{ROJO}[Error] No se pudo desencriptar el archivo. La clave puede ser incorrecta.\n")
            except Exception as e:
                print(f"{ROJO}[Error] {e}\n")

    elif pregunta1 == "2":
        pregunta = input(f"\n{VERDE}[¿Deseas usar una contraseña ya creada por este programa para encriptar o desencriptar?] (s/n): {MORADO}\n").lower()
        
        if pregunta == "s":
            clave = input(f"\n{VERDE}[Introduzca la clave]: {MORADO}\n")
            try:
                obj1 = Fernet(clave.encode())
            except (ValueError, TypeError):
                print(f"{ROJO}[Clave no válida. Asegúrate de que sea una clave Fernet correcta.]\n")
                continue

            cifdif1 = input(f"\n{VERDE}[¿Quieres encriptar o desencriptar? (e/d)]: {MORADO}\n").lower()
            if cifdif1 == "e":
                mensaje1 = input(f"\n{VERDE}[Escribe el mensaje a encriptar]: {MORADO}\n")
                mensaje_cifrado1 = obj1.encrypt(mensaje1.encode())
                print(f"\n{VERDE}[Mensaje encriptado]: {MORADO}{mensaje_cifrado1.decode()}{RESET}")
            elif cifdif1 == "d":
                mensaje2 = input(f"\n{VERDE}[Escribe el mensaje a desencriptar]: {MORADO}\n")
                try:
                    mensaje_desencriptado = obj1.decrypt(mensaje2.encode())
                    print(f"\n{VERDE}[Mensaje desencriptado]:{MORADO}{mensaje_desencriptado.decode()}{RESET}")
                except InvalidToken:
                    print(f"{ROJO}[Error] No se pudo desencriptar el mensaje. La clave puede ser incorrecta.\n")
            else:
                input(f"{ROJO}[Opción no valida]\n")

        elif pregunta == "n":
            key = Fernet.generate_key()
            obj = Fernet(key)
            print(f"\n{VERDE}[Clave generada]: {MORADO}{key.decode()}")
            print(f"\n{ROJO}[Guarda esta clave en un bloc de notas o algo, te servirá para encriptar y desencriptar los mensajes.]\n")
            cifdif = input(f"{VERDE}[¿Quieres encriptar o desencriptar?] (e/d): {MORADO}\n").lower()
            if cifdif == "e":
                mensaje = input(f"\n{VERDE}[Escribe el mensaje a encriptar]: {MORADO}\n")
                mensaje_cifrado = obj.encrypt(mensaje.encode())
                print(f"\n{VERDE}[Mensaje encriptado]: {MORADO}{mensaje_cifrado.decode()}{RESET}\n")
            elif cifdif == "d":
                mensaje3 = input(f"\n{VERDE}[Escribe el mensaje a desencriptar]: {MORADO}\n")
                try:
                    mensaje_desencriptado2 = obj.decrypt(mensaje3.encode())
                    mensaje = input(f"\n{VERDE}[Escribe el mensaje a encriptar]: {MORADO}{RESET}\n")
                except InvalidToken:
                    print(f"{ROJO}[Error] No se pudo desencriptar el mensaje. La clave puede ser incorrecta.")
            else:
                print(f"{ROJO}[Opción no valida]")
                continue
        else:
            print(f"{ROJO}[Opción no valida]")
            continue
    else:
        print(f"{ROJO}[Opción no valida]")
        continue

    continuar = input(f"{ROJO}[¿Quieres continuar?] (s/n): ")
    if continuar.lower() != 's':
        break