import json #Importando a biblioteca json


#Dados que serão importados
dados_pessoas_escola = {
    "alunos": [
        {   "Matricula": 123456,
            "nome": "João",
            "idade": 20,
            "curso": "Engenharia"
        },
        {
            "Matricula": 789012,
            "nome": "Maria",
            "idade": 22,
            "curso": "Medicina"
        },
        {
            "Matricula": 345678,    
            "nome": "Pedro",
            "idade": 21,
            "curso": "Direito"
        }
    ]
}

# criando um arquivo json e escrevendo os dados nele
with open('dados_alunos.json', 'w') as arquivo:
    json.dump(dados_pessoas_escola, arquivo, indent=2)
    print("Arquivo JSON criado com sucesso!")
# Lendo o arquivo JSON e exibindo os dados
with open('dados_alunos.json', 'r') as arquivo:
    dados_lidos = json.load(arquivo)
    print("Dados lidos do arquivo JSON:")

    # posso mostrar os dados assim, organizando  da minha forma
    for aluno in dados_lidos["alunos"]:
        print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']}")

# ou lendo o arquivo json e exibindo os dados  da forma de de um objeto json
    print(json.dumps(dados_lidos, indent=2, ensure_ascii=False))  # Exibe o JSON formatado