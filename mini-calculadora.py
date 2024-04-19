numero1  = float(input('Informe o numero 1 :'))
operacao = str(input('Operacao :'))
numero2  = float(input('Informe o numero 2 :'))
resultado = 0
   
if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 -  numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    resultado = numero1 / numero2
else:
    print("Operacao invalida")

print('Resultado : ', float(resultado))
    

    