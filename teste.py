import xml.etree.ElementTree as ET

# Função para remover os namespaces
def remove_namespaces(tree):
    for elem in tree.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]

# Ler o arquivo XML
tree = ET.parse('NF.xml')
root = tree.getroot()

# Encontrar todos os elementos CompNfse
comp_nfse_elements = root.findall(".//{http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd}CompNfse")

# Inverter a ordem das tags dentro de cada CompNfse
for comp_nfse in reversed(comp_nfse_elements):
    for elem in comp_nfse.iter():
        if 'ns0:' in elem.tag:
            elem.tag = elem.tag.replace('ns0:', '')

# Remover namespaces
remove_namespaces(root)

# Salvar o novo XML em um arquivo
tree.write('novo_arquivo.xml', encoding='utf-8')
