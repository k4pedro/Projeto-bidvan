from classes.pessoa import Pessoa
class Motorista(Pessoa):
    def __init__(self, nome, dtNasc, contato, senha, endereco, CNH, CNPJ, areaDeAtuacao):
        super().__init__(nome, dtNasc, contato, senha, endereco)
        self.CNPJ = CNPJ
        self.CNH = CNH
        self.areaDeAtuacao = areaDeAtuacao

        