contador = 0

numero = int(input("Informe ate que numero contar ..: "))
elevado = int(input("Informe o numero elevado ..: "))
while contador < numero:
    contador = contador + elevado
    print("Contador", int(contador))