alunos = []
qtde = int(input("Qtde de alunos: "))
for i in range(qtde):
    nome  = input("Nome: ")
    idade = input("Idade:")
    nota  = input("Nota: ")
    aluno = {"nome": nome, "idade": idade, "nota": nota}
    alunos.append(aluno)
    print("--------------------------")

for aluno in alunos:
    print(f'Nome: {aluno["nome"]}, Idade: {aluno["idade"]}, Nota: {aluno["nota"]}')