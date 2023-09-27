url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
#url = "   "

#SANITIZAÇÃO DA URL
url = url.strip()


#VALIDAÇÃO DA URL
if url == "":
    raise ValueError("A URL ESTÁ VAZIA")

print(url)

indiceinterrogacao = url.find('?')

url_base = url[:indiceinterrogacao] # Fatiamento de string / deixando o parametro de fatiamento tanto no inicio quanto no final diz para começar do primeiro ou ir até o final 
print(url_base)

url_parametros = url[indiceinterrogacao + 1 :] # Primeiro número é inclusivo, ou seja, ponto de partida / o último é excluisivo, ou seja, tem que botar o parametro +1
print(url_parametros)

parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)

indice_valor = indice_parametro + len(parametro_busca) + 1

indice_e_comercial = url_parametros.find('&', indice_valor)

if indice_e_comercial == -1:
    
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor : indice_e_comercial]


print(valor)