import re
import datetime
from  classes.passageiro import Passageiro
from  classes.motorista import Motorista
from  classes.pessoa import Pessoa

class ValidadorDados:
    def validaCPF(self, CPF):
        padraoCPF = re.compile(r'^(\d{3}\.){2}\d{3}-\d{2}$')
        if re.match(padraoCPF, CPF):
            return True
        return False

    def validaCNPJ(self, CNPJ):
        if len(CNPJ) != 18:
                return False
        return True
    
    def validaCNH(self, CNH):
        if len(CNH) != 10:
              return False
        return True
    
    def validaNomeCompleto (self, nome):
        padraoNome = r'^[A-Za-z\s]*[A-Za-z]{3,}[A-Za-z\s]*$'

        if len(nome) < 10:
             return False        
        if re.match(padraoNome, nome):
            return True
        
    
    def validaDataNascimento(self, dtNasc):
        dataAtual = datetime.datetime.now()
        padraoData = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(19\d{2}|20\d{2})$'
    
        if not re.match(padraoData, dtNasc):
            return False  # Retorna False se a data não corresponder ao padrão
        data_nascimento = datetime.datetime.strptime(dtNasc, '%d/%m/%Y')
    
        if data_nascimento > dataAtual:
            return False  # Retorna False se a data de nascimento for maior que a data atual
        return True

    def validaContato(self, contato):
        padraoNumero = r'\(\d{2}\) \d{5}-\d{4}'
        padraoEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if re.search(padraoNumero, contato):
            return True
        elif re.search(padraoEmail, contato):
            return True
        return False   
    
    def validaPlaca(self, placa):
         padraoPlaca = r'^[A-Z]{3}\d[A-Z]\d{2}$'

         if re.match(padraoPlaca, placa):
            return True
         return False
    
    def validaCor(self, cor):
        padraoCor = ["preto", "azul", "vermelho", "amarelo", "laranja", "branco", "cinza", "verde", "violeta"]

        if cor.lower() in padraoCor:
            return True
        return False
    
    def validaAno(self,ano):
        anoAtual = datetime.datetime.now().year
        padraoAno = r'^[1-9]\d{3}$'

        if re.match(padraoAno, ano) and ano <= anoAtual:
            return True
        return False