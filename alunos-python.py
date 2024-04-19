alunos = []

# Função para adicionar um novo aluno ao array
def adicionar_aluno(nome, idade, nota):
    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }
    alunos.append(aluno)

# Exemplo: Adicione três alunos
adicionar_aluno("João", 20, 8.5)
adicionar_aluno("Maria", 22, 9.0)
adicionar_aluno("Pedro", 19, 7.8)

# Imprima os dados dos alunos
for aluno in alunos:
    print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}")