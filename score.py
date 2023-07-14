from tupy import *

class Pontuacao(Image):
    def __init__(self, jogo) -> None:
        self.file = 'pontuacao.png'
        self.x = 520
        self.y = 240
        self.jogo = jogo

    def exibir_pontuacao(self) -> None:
        pontuacao = self.jogo.pontuacao
        print(f"Pontuação: {pontuacao}") # Botão que exibe a pontuação

