import xml.etree.ElementTree as ET


# Ler o arquivo XML
tree = ET.parse('NF.xml')
root = tree.getroot()

# Encontrar todos os elementos CompNfse
comp_nfse_elements = root.findall(".//{http://www.abrasf.org.br/ABRASF/arquivos/nfse.xsd}CompNfse")

# Inverter a ordem das tags dentro de cada CompNfse
for comp_nfse in reversed(comp_nfse_elements):
    # Remover o prefixo ns0 de cada elemento
    for elem in comp_nfse.iter():
        if 'ns0:' in elem.tag:
            elem.tag = elem.tag.replace('ns0:', '')


# Salvar o novo XML em um arquivo
tree.write('novo_arquivo.xml', encoding='utf-8')