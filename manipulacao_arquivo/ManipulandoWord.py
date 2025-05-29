from docx import Document

# Add informações aos arquivo 
doc = Document() # Abrindo documento
doc.add_heading("Exemplo de Título", level=1)
doc.add_paragraph("Exemplo de paragrafo")



# Add Tabela
tabel = doc.add_table(rows=3,cols=3)
tabel.cell(0,0).text ="Matrícula"
tabel.cell(0,1).text = "Nome"
tabel.cell(0,2).text ="Data de Nascimento"
tabel.cell(1,0).text = "20250002"
tabel.cell(1,1).text = "Andresa Lídia"
tabel.cell(1,2).text = "10/05/2006"
tabel.cell(2,0).text = "20250003"
tabel.cell(2,1).text = "Faustino jr"
tabel.cell(2,2).text = "05/12/2004"

#criando documeto
doc.save('PrimeiroDocWordPython.docx')


#lendo texto em documento
for paragraph in doc.paragraphs:
    print(paragraph.text)

#lendo tabela
for tabela in doc.tables:
    for linha in tabela.rows:
        dados_linha = [celula.text.strip() for celula in linha.cells]
        print(dados_linha)

# Mostrar de forma formatada

from tabulate import tabulate #importando bibliotedca de formatação de tabela


dados = []
for tabela in doc.tables:
    for linhas in tabela.rows:
        dados_linha = [celula.text.strip() for celula in linhas.cells]
        dados.append(dados_linha)

# Separando o cabeçalo e o corpo da tabela
cabecalho = dados[0]
corpo = dados[1:]

# Mostrar formatado no terminal

print(tabulate(corpo,headers=cabecalho, tablefmt="github"))