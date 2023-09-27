from random import randrange

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0
    
    def dar_likes(self):
        self._likes += randrange(1, 10)

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def like(self):
        return self._likes

    def __str__(self):
        return '{} - {} - {} Likes'.format(self._nome, self._ano, self.like)

class Filme (Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao
        
    def __str__(self):
        return '{} - {} - {} min - {} Likes'.format(self._nome, self._ano, self._duracao, self.like)

class Serie (Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas
    
    def __str__(self):
        return '{} - {} - {} temporadas - {} Likes'.format(self._nome, self._ano, self._temporadas, self.like)

class Playlist:
    def __init__(self, nomes, programas):
        self.nomes = nomes
        self._programas = programas
        
    def __getitem__(self, item):
        return self._programas[item]
    
    def __len__(self):
        return len(self._programas)
    
    @property
    def listagem(self):
        return self._programas


vingadores = Filme('vingadores Ultimato', 2019, 200)
babd = Serie('breaking bad', 2013, 5)
tdmp = Filme('Todo mundo em pânico', 2001, 100)
theboys = Serie('The boys', 2019, 3)


vingadores.dar_likes()
babd.dar_likes()
tdmp.dar_likes()
theboys.dar_likes()


filme_e_series = [vingadores, babd, tdmp, theboys]
playlist_fds = Playlist('fim de semana', filme_e_series)


for programa in playlist_fds:
    print(programa)

print('Tamanho da Playlist: {}'.format(len(playlist_fds)))
