class Client:
    '''Atributos del cliente '''
    def __init__(self):
        self.name = str
        self.lastname = str
        self.mail = str
        self.number = int

        self.num_card = int
        self.date = str
        self.cvv = []

    '''Comportamientos del cliente / métodos '''
    
    def __str__(self):
        '''Mostrar datos del cliente sin considerar la tarjeta que es privada'''
        return f'\nDATOS DEL CLIENTE\nCliente {self.name} {self.lastname}\nCorreo: {self.mail}\nNúmero telefono: {self.number}'


    def new_account(self):
        ''' Completar datos del nuevo cliente '''
        print('\nTe solicitaremos tus datos para crear tu cuenta -->')
        self.name = input('Agrega tu nombre: ')
        self.lastname = input('Agrega tu apellido: ')
        self.mail = input('Agrega tu correo: ')
        while True:
            try:
                self.number = int(input('Agrega tu número de telefono: '))
                self.num_card = int(input('Agrega el número de tu tarjeta: '))
                self.date = input('Agrega la fecha de expiración de tu tarjeta: ')
                self.cvv = int(input('Agrega el número de seguridad de la tarjeta: '))
                break
            except ValueError:
                print(' --> Debe ser un número, vuelve a intentarlo <--')


    def show_card(self):
        '''Método para revisar los datos de la tarjeta'''
        return f'\nDATOS DE LA TARJETA\nNúmero Tarjeta: {self.num_card}\nFecha Exp.: {self.date}\nCVV: {self.cvv}\n'


    def pay(self):
        ''' Pagar asegurando que el CVV es correcto'''
        print('\nEstas a un paso de pagar tu carro de compras!!')
        confirm = input('Confirmas la compra? Y/N: ')
        if confirm.upper() == 'Y':
            cvv = int(input('Escribe el numero de seguridad de la tarjeta: '))
            if cvv == self.cvv:
                return '\nCompra exitosa!'
            else:
                return '\nNo es el numero correcto'
        else:
            return 'Te arrepentiste? Hasta la próxima'
