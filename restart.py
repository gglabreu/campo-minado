from tupy import *

class Reiniciar(Image):
    def __init__(self, jogo) -> None:
        self.file = 'reiniciar.png'
        self.x = 240
        self.y = 10
        self.jogo = jogo

    def reiniciar_jogo(self) -> None: # Reinicia o jogo com os parâmetros iniciais: 100 pontos 6 bombas
        self.jogo.pontuacao = 100
        self.jogo.bombas = random.sample(range(0, 80), 6)
        self.jogo.bombas_encontradas = []
        self.jogo.bombas_restantes = self.jogo.bombas.copy()
        print("Jogo reiniciado!")