from veiculo import Veiculo
class Moto(Veiculo):
    def __init__(self, marca, modelo, cor, tipo, cilindrada):
        super().__init__(marca, modelo, cor, tipo)
        self.cilindrada = cilindrada

    
        