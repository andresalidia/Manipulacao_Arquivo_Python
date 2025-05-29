
# Sistema de Gestão Escolar
# Importando bibliotecas necessárias
import json 
import os 

# funções para manipulação de arquivos JSON

#Adicionando Alunos no sistema
def adicionar_aluno(nome, matricula, data_nascimento):
    aluno = {
        "nome": nome,
        "matricula": matricula,
        "data_nascimento": data_nascimento,
        "notas": {},
        "faltas": 0
    }
    # Lendo os dados que já existem no arquivo JSON
    with open('dados_Sistema_escola.json', 'r', encoding='utf-8') as arquivo:
        dados_Escola = json.load(arquivo)
    # Adicionando o novo aluno à lista de alunos
    dados_Escola["alunos"].append(aluno)
    # Salvando os dados no arquivo JSON
    with open('dados_Sistema_escola.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados_Escola, arquivo, indent=2, ensure_ascii=False)
        print(f"Aluno {nome} adicionado com sucesso!")

# Listar Alunos
def listar_alunos():
    with open('dados_Sistema_escola.json', 'r', encoding='utf-8') as arquivo:
        dados_Escola = json.load(arquivo)
    for aluno in dados_Escola["alunos"]:
        print(f"Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}, nota: {aluno['notas']}, Faltas: {aluno['faltas']}, ")

# remover aluno com base na matrícula
def remover_aluno(matricula):
    with open('dados_Sistema_escola.json', 'r', encoding='utf-8') as arquivo:
        dados_Escola = json.load(arquivo)
    
    # Filtrando os alunos para remover o aluno com a matrícula especificada
    dados_Escola["alunos"] = [aluno for aluno in dados_Escola["alunos"] if aluno["matricula"] != matricula]
    
    # Salvando os dados atualizados no arquivo JSON
    with open('dados_Sistema_escola.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados_Escola, arquivo, indent=2, ensure_ascii=False)
        for aluno in dados_Escola["alunos"]:
            if aluno["matricula"] == matricula:
                print(f"Aluno {aluno['nome']} com matrícula {aluno['matricula']} foi removido com sucesso!")


                
# Sistema de Gestão Escolar

print("Seja bem-vindo ao Sistema de Gestão Escolar!")
print("Informe o que deseja fazer:")
print("1. Listar Alunos")
print("2. Adicionar Aluno")
print("3. Remover Aluno")
escolha = input("Digite o número da opção desejada: ")
if escolha == "1":
    listar_alunos()
elif escolha == "2":
  print("Vamos adicionar um novo aluno!")

  # Pedindo dados do aluno ao usuário
  nome= input("Digite o nome do aluno: ")
  matricula = input("Digite a matrícula do aluno: ")
  data_nascimento = input("Digite a data de nascimento do aluno (DD/MM/AAAA): ")
  adicionar_aluno(nome, matricula, data_nascimento)
elif escolha == "3":
    print("Vamos remover um aluno!")  
    # pedindo informações para  remover aluno
    matricula = input("Digite a matrícula do aluno que deseja remover: ")
    remover_aluno(matricula)