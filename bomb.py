from tupy import *

class ContadorBombas(Image):
    def __init__(self, jogo) -> None:
        self.file = 'bomba.png'
        self.x = 240
        self.y = 472
        self.jogo = jogo

    def mostrar_bombas_restantes(self) -> None:
        quantidade_bombas = len(self.jogo.bombas_restantes)
        print(f"Quantidade de bombas restantes: {quantidade_bombas}") # Botão que exibe quantidade de bombas restantes
