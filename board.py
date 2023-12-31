from tupy import *

class Campo(Image):
    def __init__(self) -> None:
        self.file = 'campo.png'
        self.x = 240
        self.y = 240
        self.casas = {
            '0': {'x': 48, 'y': 48}, 
            '1': {'x': 96, 'y': 48}, 
            '2': {'x': 144, 'y': 48}, 
            '3': {'x': 192, 'y': 48}, 
            '4': {'x': 240, 'y': 48}, 
            '5': {'x': 288, 'y': 48}, 
            '6': {'x': 336, 'y': 48}, 
            '7': {'x': 384, 'y': 48}, 
            '8': {'x': 432, 'y': 48},
            '9': {'x': 48, 'y': 96}, 
            '10': {'x': 96, 'y': 96}, 
            '11': {'x': 144, 'y': 96}, 
            '12': {'x': 192, 'y': 96}, 
            '13': {'x': 240, 'y': 96}, 
            '14': {'x': 288, 'y': 96}, 
            '15': {'x': 336, 'y': 96}, 
            '16': {'x': 384, 'y': 96}, 
            '17': {'x': 432, 'y': 96},
            '18': {'x': 48, 'y': 144}, 
            '19': {'x': 96, 'y': 144}, 
            '20': {'x': 144, 'y': 144}, 
            '21': {'x': 192, 'y': 144}, 
            '22': {'x': 240, 'y': 144}, 
            '23': {'x': 288, 'y': 144}, 
            '24': {'x': 336, 'y': 144}, 
            '25': {'x': 384, 'y': 144}, 
            '26': {'x': 432, 'y': 144},
            '27': {'x': 48, 'y': 192}, 
            '28': {'x': 96, 'y': 192}, 
            '29': {'x': 144, 'y': 192}, 
            '30': {'x': 192, 'y': 192}, 
            '31': {'x': 240, 'y': 192}, 
            '32': {'x': 288, 'y': 192}, 
            '33': {'x': 336, 'y': 192}, 
            '34': {'x': 384, 'y': 192}, 
            '35': {'x': 432, 'y': 192},
            '36': {'x': 48, 'y': 240}, 
            '37': {'x': 96, 'y': 240}, 
            '38': {'x': 144, 'y': 240}, 
            '39': {'x': 192, 'y': 240}, 
            '40': {'x': 240, 'y': 240}, 
            '41': {'x': 288, 'y': 240}, 
            '42': {'x': 336, 'y': 240}, 
            '43': {'x': 384, 'y': 240}, 
            '44': {'x': 432, 'y': 240},
            '45': {'x': 48, 'y': 288}, 
            '46': {'x': 96, 'y': 288}, 
            '47': {'x': 144, 'y': 288}, 
            '48': {'x': 192, 'y': 288}, 
            '49': {'x': 240, 'y': 288}, 
            '50': {'x': 288, 'y': 288}, 
            '51': {'x': 336, 'y': 288}, 
            '52': {'x': 384, 'y': 288}, 
            '53': {'x': 432, 'y': 288},
            '54': {'x': 48, 'y': 336}, 
            '55': {'x': 96, 'y': 336}, 
            '56': {'x': 144, 'y': 336}, 
            '57': {'x': 192, 'y': 336}, 
            '58': {'x': 240, 'y': 336}, 
            '59': {'x': 288, 'y': 336}, 
            '60': {'x': 336, 'y': 336}, 
            '61': {'x': 384, 'y': 336}, 
            '62': {'x': 432, 'y': 336},
            '63': {'x': 48, 'y': 384}, 
            '64': {'x': 96, 'y': 384}, 
            '65': {'x': 144, 'y': 384}, 
            '66': {'x': 192, 'y': 384}, 
            '67': {'x': 240, 'y': 384}, 
            '68': {'x': 288, 'y': 384}, 
            '69': {'x': 336, 'y': 384}, 
            '70': {'x': 384, 'y': 384}, 
            '71': {'x': 432, 'y': 384},
            '72': {'x': 48, 'y': 432}, 
            '73': {'x': 96, 'y': 432}, 
            '74': {'x': 144, 'y': 432}, 
            '75': {'x': 192, 'y': 432}, 
            '76': {'x': 240, 'y': 432}, 
            '77': {'x': 288, 'y': 432}, 
            '78': {'x': 336, 'y': 432}, 
            '79': {'x': 384, 'y': 432}, 
            '80': {'x': 432, 'y': 432},
        } # Elenca as 80 casas do campo minado


        self.bombas_encontradas = []

    def remover_bomba(self, casa: str) -> None:
        del self.casas[casa]
