print("Lampada - Fluxograma")
lampada = input("Lampada (S)Plugada (N)Nao Plugada: ")

if lampada == "S":
    print("Lampada Plugada")
    bulbo = input("Bulbo Queimou  (S)Sim (N)Nao : ")
    if bulbo == "S":
        print("Trocar o bulbo")
    else:
        print("Compra nova lampada") 
else:
    print("Plugar a lampada")




