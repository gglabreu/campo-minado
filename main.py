from tupy import *
from board import Campo
from campo_minado import CampoMinado
from restart import Reiniciar
from bomb import ContadorBombas
from score import Pontuacao

if __name__ == '__main__':
    campo = Campo()
    jogo = CampoMinado(campo)
    reiniciar = Reiniciar(jogo)
    bombas = ContadorBombas(jogo)
    pontuacao = Pontuacao(jogo)
    
    run(globals())
