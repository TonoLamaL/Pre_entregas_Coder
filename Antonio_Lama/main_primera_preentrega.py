''' PRE_ENTREGA N°1 -> Crear un programa para registro e inicio de sesión '''
from Primera_pre_entrega.utils import *

menu = ''' \n
Selecciona del Menú alguna de estas opciones: 

-------- Menú ---------- Letra -----

* Iniciar sesión    ->   ( L )
* Nuevo registro    ->   ( N )
* Mostrar registros ->   ( S )
* Terminar          ->   ( Q )

------------------------------------\n'''


def run():
    '''Función principal'''
    bandera = True
    print('\n', '=' * 35)
    print('\tHola, Bienvenido !!!')
    print('', '=' * 35)

    while bandera:
        print(menu)
        action = input('Escribe tu opción   ->   usar Letra: ')
        if action.upper() == 'N':
            new_user()
        elif action.upper() == 'Q':
            print('\nYa te vas? Nos vemos pronto!\n')
            bandera = False
        elif action.upper() == 'S':
            show_users()
        elif action.upper() == 'L':
            if login() == True:
                desktop()
        elif action.upper() == 'CLEAR': # no lo muestro en el menú. Si se usa se debe volver a crear el ADMIN
            base_datos_dict.clear()
        else:
            print('\n** ATENCIÓN! No existe esa opción en el menú, vuelve a escoger. **')


run()
