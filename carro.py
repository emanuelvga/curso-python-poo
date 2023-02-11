from veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, tipo, portas):
        super().__init__(marca, modelo, cor, tipo)
        self.portas = portas
        