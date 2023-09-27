from random import randrange

class Jogo:
    def __init__(self, nome, genero, tamanho):
        self._nome = nome.title()
        self.genero = genero.title()
        self.tamanho = tamanho.title()
        self._likes = 0

    @property
    def nome(self):
        return self._nome
    
    def gera_likes(self):
        self._likes += randrange (50,100)
    
    @property
    def like(self):
        return self._likes    
    
    def __str__(self):
        return 'Titulo: {} - Gênero: {} - Tamanho: {} - {} Likes'.format(self._nome, self.genero, self.tamanho, self.like)
    
    
    
class Playstation (Jogo):
    def __init__(self, nome, genero, tamanho):
        super().__init__(nome, genero, tamanho)
        self.plataforma = 'Playstation'
    
    def __str__(self):
        return 'Titulo: {} - Gênero: {} - Tamanho: {} - Plataforma: {} - {} Likes'.format(self._nome, self.genero, self.tamanho, self.plataforma ,self.like)

class Xbox (Jogo):
    def __init__(self, nome, genero, tamanho):
        super().__init__(nome, genero, tamanho)
        self.plataforma = 'Xbox'
        
    def __str__(self):
        return 'Titulo: {} - Gênero: {} - Tamanho: {} - Plataforma: {} - {} Likes'.format(self._nome, self.genero, self.tamanho, self.plataforma ,self.like)
    
        
tlou1 = Playstation('the last of us: part 1' , 'ação', 'longo')
gow1  = Playstation('god of war 1', 'hack and slash', 'médio')
halo1 = Xbox('halo 1', 'fps / ação', 'médio')

for x in range (5):
    tlou1.gera_likes()
    gow1.gera_likes()
    halo1.gera_likes()

jogos = [tlou1,gow1,halo1]

for programa in jogos:
    print(" ")
    print(programa)
    