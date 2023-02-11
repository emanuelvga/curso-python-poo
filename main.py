from pessoa import Pessoa
from veiculo import Veiculo
from moto import Moto
from carro import Carro

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('João', 32)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

p1 = Pessoa.por_ano_de_nascimento('Luiz', 1987)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()


Pessoa.dizer_oi()

v = Veiculo('volvo', '2023', 'preto', 'flex')
m = Moto('Yamaha','2023','vermelho','flex','160')
c = Carro('Vw', '1989', 'preto', 'gasolina','2' )

c.imprimirModelo()
c.imprimirCor()

