# Como criar um arquivo XML
import xml.etree.ElementTree as XML  # importando a biblioteca XML

raiz = XML.Element("loja")  # Criando o elemento raiz do XML

#Primeiro produto
produto1 = XML.SubElement(raiz, "produto")  # Adiciona <produto> dentro de <loja>
XML.SubElement(produto1,"nome").text= "Notebook"  # Adiciona <nome> dentro de <produto>
XML.SubElement(produto1,"preco").text= "2500.00"  # Adiciona <preco> dentro de <produto>
#Segundo produto
produto2 = XML.SubElement(raiz, "produto")  # Adiciona <produto> dentro de <loja>
XML.SubElement(produto2,"nome").text= "Smartphone"  # Adiciona <nome> dentro de <produto>
XML.SubElement(produto2,"preco").text= "1500"  # Adiciona <preco> dentro de <produto>

#Salvar esse conteúdo em um arquivo XML

tree = XML.ElementTree(raiz)  # Cria uma árvore XML a partir do elemento raiz
tree.write("loja_eletronicos.xml", encoding="utf-8", xml_declaration=True)  # Salva a árvore em um arquivo XML


# Lendo o arquivo XML e exibindo os dados
tree = XML.parse("loja_eletronicos.xml")  # Abre e "perseia" (lê) o arquivo XML
root = tree.getroot()  # Obtém o elemento raiz da árvore XML, nesse caso <loja>

# Agora, vamos percorrer os elementos <produtos> que estão dentro de <loja>
print("Produtos disponíveis na loja:")  # Exibe uma mensagem inicial
for produto in root.findall("produto"):  # Encontra todos os elementos <produto> dentro de <loja>
    nome = produto.find("nome").text  # Obtém o texto do elemento <nome>
    preco = produto.find("preco").text  # Obtém o texto do elemento <preco>
    print(f"Produto: {nome} - Preço: {preco}")  # Exibe o nome e o preço do produto