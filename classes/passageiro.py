from classes.pessoa import Pessoa
class Passageiro(Pessoa):
    def __init__(self, nome, dtNasc, contato, senha, endereco, formaPag, CPF):
        super().__init__(nome, dtNasc, contato, senha, endereco)
        self.formaPag = formaPag
        self.CPF = CPF