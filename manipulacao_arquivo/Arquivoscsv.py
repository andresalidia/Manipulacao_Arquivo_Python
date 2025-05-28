import csv
with open("dados.csv", "w", newline='', encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)  # Cria um objeto escritor para escrever no arquivo CSV
    # Escreve o cabeçalho e algumas linhas de dados
    escritor.writerow(["Nome", "Idade", "Cidade"])
    escritor.writerow(["João", 25, "São Paulo"])
    escritor.writerow(["Maria", 30, "Rio de Janeiro"])
    escritor.writerow(["Pedro", 22, "Belo Horizonte"])

with open("dados.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)  # Cria um objeto leitor para ler o arquivo CSV
    for linha in leitor:
        print(linha)  # Imprime cada linha do arquivo CSV como uma lista    