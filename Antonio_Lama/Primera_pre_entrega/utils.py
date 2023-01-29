import json
path = '/base_datos.json' # agregar el path que te quede mejor

try:
    with open(path) as f:
        base_datos_dict = json.load(f)
except Exception:
    base_datos_dict = {'ADMIN' : 'coderbeca'}


    
def new_user():
    '''Crear un nuevo usuario y almacenar'''
    print('\nVas a crear un nuevo usuario.')

    while True:
        username = input('\t--> Escribe tu USUARIO a registrar (mas de 3 caracteres): ')

        if username in base_datos_dict:
            print('* Ese usuario ya existe, intenta con otro nombre *\n')
            continue
        elif len(username) < 4:
            print('* Debe ser mayor a 3 caracteres *')
            continue
        else:
            password = input('\t--> Escribe tu CONTRASEÑA (mayor a 3 caracteres): ')
            if len(password) < 4:
                print('* Debe ser mayor a 3 caracteres *')
                continue
            else:
                pass
            base_datos_dict[username] = password
            print('\nHaz creado tus credenciales, muy bien!')

            with open (path,'w') as f:
                json.dump(base_datos_dict,f, indent=4)
            break


def login():
    '''Acceso a tu cuenta'''
    login_ok = False
    intento = 1
    print('\nVas a hacer un inicio de sesion. Tienes tres intentos.')
    while intento < 4:
        username = input('\t--> Ingresa tu USUARIO: ')
        password = input('\t--> Ingresa tu CONTRASEÑA: ')

        if username in base_datos_dict and base_datos_dict[username] == password:
            print('\n¡Haz ingresado correctamente!')
            login_ok = True
            break

        else:
            if username not in base_datos_dict or base_datos_dict[username] != password:
                print('Credenciales incorrectas, ingresa denuevo tus credenciales!\n')
                intento += 1

    return login_ok


def new_password():
    '''Cambiar contraseña '''
    intento = 1
    print('\nVas a cambiar tu CONTRASEÑA. Tienes tres intentos.\n')
    while intento < 4:
        username = input('\t--> Cual es el nombre del USUARIO: ')
        old_password = input('\t--> Cual es tu CONTRASEÑA ACTUAL: ')

        if username in base_datos_dict and base_datos_dict[username] == old_password:
            new_password = input('\t--> Cual es la NUEVA CONTRASEÑA: ')
            base_datos_dict[username] = new_password
            print('\nContraseña cambiada exitosamente! Debes volver a ingresar.')
            with open (path,'w') as f:
                json.dump(base_datos_dict,f, indent=4)
            break

        else:
            if username not in base_datos_dict or base_datos_dict[username] != old_password:
                print('Credenciales incorrectas, ingresa de nuevo tus credenciales!\n')
                intento += 1


def desktop():
    '''Mostrar el escritorio'''
    print(f'\n\t_________ Este es tu escritorio! _________\n')
    action = input('Quieres cambiar tu CONTRASEÑA (C) o Cerrar sesión (Q)\n--> ')

    if action.upper() == 'C':
        new_password()

    elif action.upper() == 'Q':
        pass



def show_users():
    '''Mostrar el detalle de usuarios siempre que conozca la contraseña de ADMIN'''
    contraseña_admin = input('\t--> Ingresa la contraseña de ADMIN: ')
    if base_datos_dict['ADMIN'] == contraseña_admin: # contraseña es codebeca
        print('\n-------------------- Registros -----------------------\n')
        for registros, (username, password) in enumerate(base_datos_dict.items()):
            print(
                f'Registro n°{registros + 1}: Username: {username} -> Password: {password}')
        if base_datos_dict == {}:
            print('\t\tNo hay registros')
        print('\n------------------------------------------------------')
    else:
        print('No conoces la contraseña? No te puedo mostrar el contenido')