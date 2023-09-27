class Conta:
    def __init__(self , login, numero, saldo, limite):
        self._login  = login
        self._numero = numero
        self.saldo   = saldo
        self._limite = limite
        
    @property
    def user_login(self):
        return self._login
    
    @property
    def numero_conta(self):
        return self._numero
    
    def user_saldo(self):
        print('Seu saldo {}'.format(self.saldo))
        
    @property
    def user_limite(self):
        return self._limite
    
    @user_limite.setter
    def mudar_limite(self, novo_limite):
        self.user_limite = novo_limite
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        self.saldo -= valor
    
    def transferencia(self,valor , destino):
        self.saldo -= valor
        destino.saldo += valor
        
        
conta1 = Conta ("jpedrob", 123, 300.0, 1000.0)
conta2 = Conta ("paulab", 321, 200.0, 1000.0)

valor = float(0)

print('Oque deseja fazer?')
acao = print(str(input("Sacar, Depositar, Transferir: ").upper()))

if(acao == "Sacar"):
    print("Qual valor desejas sacar?: ")
    valor = float(input())