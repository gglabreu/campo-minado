from tupy import *
from board import Campo
import random

class CampoMinado(Image):
    def __init__(self, campo: Campo) -> None:
        self.file = 'seta.png'
        self.x = 240
        self.y = 240
        self.campo = campo
        self.bombas = random.sample(range(0, 80), 6)
        self.pontuacao = 100
        self.bombas_encontradas = []
        self.bombas_restantes = self.bombas.copy()

    def mover_seta(self, casa: int) -> None: # Move a seta para a casa desejada, se existir
        casa_str = str(casa)
        destino = self.campo.casas.get(casa_str)
        if destino is None:
            print("Casa inválida.")
            return

        self.x = destino['x']
        self.y = destino['y']

        if casa_str in self.bombas_encontradas:
            print("Você já achou essa bomba! Perdeu 20 pontos.") # Se vai na casa onde já foi achada a bomba, perde 20 pontos
            self.pontuacao -= 20
        elif casa in self.bombas_restantes:
            print("Bomba! Ganhou 20 pontos.") # Se acha a bomba, 20 pontos e remove a bomba
            self.pontuacao += 20
            self.bombas_encontradas.append(casa_str)
            self.bombas_restantes.remove(casa)
        else:
            print("Campo sem bomba. Perdeu 10 pontos.") # Se não acha a bomba, perde 10 pontos
            self.pontuacao -= 10

        if self.pontuacao <= 0: 
            print("Game Over.") # Se a pontuação cai para 0, perde o jogo

        if len(self.bombas_encontradas) == 6 and self.pontuacao > 0:
            print("Parabéns, você ganhou o jogo!") # Se acha todas as bombas sem perder, ganha o jogo