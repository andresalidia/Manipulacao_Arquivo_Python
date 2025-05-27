# Manipulação de Arquivos:

# Metodo open():
# O método open() é usado para abrir um arquivo, ler, escrever ou adicionar conteúdo a ele.
# A sintaxe básica é a seguinte:
#arquivo = open("nome_do_arquivo.txt ou caminho/para/o/arquivo.txt", "modo")
# onde "modo" pode ser: 
# "r" para leitura (read), 
# "w" para escrita (write),
# "a" para adicionar (append)
# 'x' para criar um novo arquivo (erro se já existir),)
#  "b" para binário (usado com 'rb' e 'wb').
# "t" para texto (usado com 'rt' e 'wt').
# "r+" para leitura e escrita (read and write).
# "w+" para escrita e leitura (write and read).
# "a+" para adicionar e leitura (append and read).
# "x+" para criar e leitura (create and read).
# 'rb' leitura em modo binário (tipo pra imagens)
# 'wb' escrita em modo binário (tipo pra imagens)
# O método open() retorna um objeto de arquivo que pode ser manipulado. ex: read(), write(), close().

with open("PrimeiroArquivo.txt", "r") as arq:
     conteudo = arq.read()
     print(conteudo)

with open("PrimeiroArquivo2.txt", "w") as escrever:
    escrever.write("Essa é uma mensagem com o método write()\n")
    mensagem = "Isso é para mostrar que também posso colocar mensagens em uma variavel e depois escrever ela no arquivo\n"
    escrever.write(mensagem)
    escrever.write("Nota importante, esse comando vai subescrever tudo que ja estiver no arquivo,\n ou seja apaga tudo que já estava escrito antes e escreve essa nova mensagem.\n")

#     #Nota importante sobre esse método!
#     # Ele não cria um novo arquivo, apaga o que está com o mesmo nome que ele e escreve a mensagem do write()

# como acrencentar algo?
with open("PrimeiroArquivo2.txt", "a") as escrever:
     escrever.write("Esse é um exemplo de como adicionar algo a um arquivo já existente.\n")
     escrever.write("Ele não apaga nada, apenas adiciona o que você colocar depois do 'a' no open()\n")
     escrever.write("E o 'w' apaga tudo que já estava escrito antes.\n")
     escrever.write("Então cuidado com o que você vai usar!\n")
# o "a"  cria um novo arquivo se não existir, mas não apaga nada do arquivo já existente.



# Exercícios:

Materias = ["Matemática", "Português", "História", "Geografia", "Ciências", "Educação Física", "Artes", "Inglês", "Física", "Química"]
notas = [7.5, 8.0, 6.5, 7.0, 9.0, 8.5, 7.0, 8.0, 9.5, 10.0]

# criando um arquivo chamado Boletim.txt e escrevendo as notas e matérias
with open("Boletim.txt", "w") as arq:
    for materia, nota in zip(Materias, notas):
        arq.write(f"{materia}: {nota}\n")
# essa é uma forma de fazer isso, porém quando se entende como a maquina funciona, você percebe que essa 
#forma é ineficiente, pois ele vai escrever linha por linha, e não de uma vez só.
# então vamos fazer de uma forma mais eficiente, escrevendo tudo de uma vez só.
# criando um arquivo chamado Boletim.txt e escrevendo as notas e matérias
conteudo = {}
for materia, nota in zip(Materias, notas):
        conteudo.update({materia: nota})

with open("Boletim.txt", "w") as arq:
   for materia, nota in conteudo.items():
        arq.write(f"{materia}: {nota}\n")

# exercicios cyber edux:

 #1.
with open("meu_arquivo.txt", "w+", encoding="utf-8") as arquivo:
        arquivo.write("Olá, mundo!\n")
        arquivo.write("Aprendendo Python!\n")
        arquivo.write("O mundo é um lugar incrível!\n")
        arquivo.write("o mundo é lindo")
       
        arquivo.seek(0)# joga o cursor para o começo do arquivo
        mensagem = arquivo.read()
        print(mensagem)
        
        palavras = mensagem.split()# separa as palavras
        print(f"O Arquivo tem {len(palavras)} palavras")# mostra as palavras separadas
        
        arquivo.seek(0)
        linhas = arquivo.readlines()
        print(f"O total de linhas é {len(linhas)}")

with open("Copia.txt", "w", encoding="utf-8") as destino:
    destino.write(mensagem)
    print("Arquivo Copiado com sucesso!")


palavras = "mundo"
with open("Copia.txt", "r", encoding="utf-8") as arquivo:
    for numero_linha, linha in enumerate(arquivo, start=1):# o enumerate serve para contar as linhas
        # e o start=1 serve para começar a contagem do 1, se não ele começa do 0
        if palavras in linha:
           print(f"linha{numero_linha}: {linha.strip()}")# strip() necessário, pois a cada 
           #print uma nova linha é criada e o arquivo já tem um \n, então vai ficar com \n duplo
    # outra forma de fazer isso é:
    for linha in arquivo:
        if palavras in linha:
            print(linha.strip())

with open("ListadeCompras.txt", "r", encoding="utf-8") as compras:
    lista_compras=[lista.strip() for lista in compras]# o strip() serve para remover os espaços em branco
    print(lista_compras)
    lista_compras.sort()# ordena a lista
    print(lista_compras)# mostra a lista ordenada


with open("ListadeCompras_Copias.txt", "w", encoding="utf-8") as compras:
    for item in lista_compras:
        compras.write(f"{item}\n")
print("Lista de compras copiada com sucesso!")

with open("PrimeiroArquivo.txt", "r", encoding="utf-8") as arquivo:
    # lê quantidade de linhas do arquivo
    linhas = arquivo.readlines()
    # print(linhas)
    print(f"O arquivo tem {len(linhas)} linhas.")


    #lê quantidade de palavras do arquivo
    arquivo.seek(0)  # Volta para o início do arquivo
    conteudo= arquivo.read()
    palavras = conteudo.split()# separa as palavras em uma lista
    # print(palavras)
    print(f"O arquivo tem {len(palavras)} palavras.")


    #lê quantidade de caracteres do arquivo
    arquivo.seek(0)  # Volta para o início do arquivo
    conteudo = arquivo.read()
    caracteres = len(conteudo)
    print(f"O arquivo tem {caracteres} caracteres.")
    

