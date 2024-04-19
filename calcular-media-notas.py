nome_aluno = str(input("Digite o nome do Aluno:"))
nome_disciplina = str(input("Digite o nome da disciplina:"))
quantidade_notas = int(input("Digite a quantidade de notas:"))
soma_notas = 0

for i in range(1, quantidade_notas + 1):
    nota = float(input(f"Digite a nota {i}:"))
    soma_notas = soma_notas + nota

media = soma_notas / quantidade_notas
print(f"Nome do Aluno :  {nome_aluno} Disciplina - {nome_disciplina} " )
print(f"A média das notas é {media:.2f}.")

if media >= 7:
    print("Aluno Aprovado")
else:
    print("Aluno reprovado")