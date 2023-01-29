from Antonio_Lama.Segunda_pre_entrega.Class_utils import Client


cliente1 = Client()

cliente1.new_account()
print(cliente1)

card1 = cliente1.show_card()
print(card1)

pay = cliente1.pay()
print(pay)

