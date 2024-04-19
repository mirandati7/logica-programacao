alunos = []

# Função para adicionar um novo aluno ao array

for i in range(3):
    nome = input ("Nome: ")
    idade = input ("Idade: ")
    nota = input ("Nota: ")

    aluno = {"nome": nome, "idade": idade,   "nota": nota}
    alunos.append(aluno)
# Imprima os dados dos alunos
for aluno in alunos:
    print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}")