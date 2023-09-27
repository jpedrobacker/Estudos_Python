
class Conta:
    def __init__(self, codigo, titular):
        self.titular = titular
        self._codigo = codigo
        self._saldo = 0
        
    def deposita(self, valor):
        self._saldo += valor
        
    def __eq__(self, outro):
        if type(outro) !=Conta:
            return False
        
    def __str__(self):
        return 'A conta de código: {} possui um saldo de R${}'.format(self._codigo , self._saldo)
        
class ContaCorrente (Conta):
    
    def desconto_passa_mes(self):
        self._saldo -= 2
    
class ContaPoupanca (Conta):
    
    def desconto_passa_mes(self):
        self._saldo *=1.01
        self._saldo -= 3
    
    
from functools import total_ordering

@total_ordering
class ContaSalario (Conta):
    
    def __init__(self, codigo, titular, salario):
        super().__init__(codigo, titular)
        self.salario = salario

    def __eq__(self, outro):
        
        if type(outro) != ContaSalario: # uso do Type para saber se o "outro" é da mesma classe
            return False
        return  self._saldo == outro._saldo and self._saldo == outro._saldo

    def __lt__(self, outro): # ordenação de elementos de uma classe por medidas especificas como por exemplo o "saldo" como utilizado abaixo
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._saldo < outro._saldo
 
    def imposto_salario(self):
        if 0 <= self.salario <= 1903.98:
            return self.salario
        
        elif 1903.99 <= self.salario <= 2826.65:
            return self.salario - (self.salario * 0.075)

        elif 2826.66 <= self.salario <= 3751.05:
            return self.salario - (self.salario * 0.150)
        
        elif 3751.06 <= self.salario <= 4664.68:
            return self.salario - ((self.salario * 22.5)/100)
        
        elif 4664.69 <= self.salario:
            return self.salario - ((self.salario * 27.5)/100)
        
    def __str__ (self):
        return 'A conta de código: {} possui um saldo de R${} com um salario médio de {:.2f}'.format(self._codigo , self._saldo,self.imposto_salario())


conta2 = ContaSalario(123 , "Joao", 2142.54)
conta3 = ContaSalario(321, "Bia", 4532.78)
conta1 = ContaSalario(312, "Paula", 4664.69)

contas = [conta1, conta2, conta3]

for conta in contas:
    print(conta)