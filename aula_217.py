#COMPOSIÇÃO NA ORIENTAÇÃO A OBJETOS
# COMPOSIÇÃO SIMPLESMENTE SERIA É UMA ESPECIALIZAÇÃO DA AGREGAÇÃO

class Cliente:
    def __init__(self, nome ):
        self.nome = nome
        self.enderecos = []

    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
            for endereco in self.enderecos:
                print(f'Rua: {endereco.rua}, Número: {endereco.numero}')

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero


cliente1 = Cliente('Gabriel')
cliente1.inserir_enderecos('Rua Garibaldi', 914)
cliente1.inserir_enderecos('Rua Minas Gerais', 914)

print(cliente1.enderecos[0].rua)
print(cliente1.enderecos[1].rua)
cliente1.listar_enderecos()

print('AQUI TERMINA O CÓDIGO')
    