import xml.etree.ElementTree as ET

# Função para remover os namespaces
def remove_namespaces(tree):
    for elem in tree.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]

# Ler o arquivo XML
tree = ET.parse('NF.xml')
root = tree.getroot()

# Encontre todos os elementos CompNfse
comp_nfse_elements = root.findall(".//{http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd}CompNfse")

root[:] = comp_nfse_elements[::-1]

remove_namespaces(root)

# Salvar o novo XML em um arquivo
tree.write('novo_arquivo.xml', encoding='utf-8')