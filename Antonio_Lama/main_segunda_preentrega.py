
try:
    from Antonio_Lama.Segunda_pre_entrega.Class_utils import Client
except Exception:
    print('** Debes instalar el paquete Antonio_Lama-1.0 antes de arrancar **')
else:

    cliente1 = Client()

    cliente1.new_account()
    print(cliente1)

    card1 = cliente1.show_card()
    print(card1)

    pay = cliente1.pay()
    print(pay)

finally:
    print('Terminado')

