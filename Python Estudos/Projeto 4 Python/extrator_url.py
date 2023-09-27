import re #ReGex ou Regular Expressions, usado para validar coisas como CPF, CEP, URLS e entre outras

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
        self.indiceinterrogacao = url.find('?')
        
        
    def get_url(self):
        return self.url
        
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    
    
    def valida_url(self):
        if not self.url:
            raise ValueError("A URL ESTÁ VAZIA")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')#Metodos do ReGex para validação
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida.")
    
    def get_url_base(self):
        url_base = self.url[:self.indiceinterrogacao]
        return url_base
    
    @property
    def url_parametro(self):
        url_parametro = self.url[self.indiceinterrogacao + 1 :]
        return url_parametro
    
    def get_valor_parametro(self, parametro_busca):
        
        indice_parametro = self.url_parametro.find(parametro_busca)

        indice_valor = indice_parametro + len(parametro_busca) + 1

        indice_e_comercial = self.url_parametro.find('&', indice_valor)

        if indice_e_comercial == -1:
    
            valor = self.url_parametro[indice_valor:]
        else:
            valor = self.url_parametro[indice_valor : indice_e_comercial]

        return valor
    
    def __len__ (self): #Metodo especial para saber o tamanho de um str
        return len(self.url)
    
    def __str__(self): #Metodo especial para padronizar a str da classe
        return self.url
    
    def __eq__(self, other): #Metodo especial para comparar strs entre classes
        return self.url == other.url
    
extrator_url = ExtratorURL("bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real")
extrator_url2 = ExtratorURL("bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real")


print("A Url tem : {} caracteres".format(len(extrator_url)))
print(extrator_url)

print (extrator_url == extrator_url2)

valor_quatidade = extrator_url.get_valor_parametro('quantidade')

print(valor_quatidade)