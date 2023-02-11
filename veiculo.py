class Veiculo:
    def __init__(self, marca, modelo, cor, tipo ):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.tipo = tipo
    

    def imprimirModelo(self):
        print(f'Este veículo é do ano de {self.modelo}')



    def imprimirCor(self):
        print(f'Este veiculo é {self.cor}')


        
        

