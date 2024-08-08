import streamlit as st
from validadorDados import ValidadorDados
from classes.passageiro import Passageiro

class Cad_Passageiro:
    def __init__(self):
        self.passageiros = []
    
    def cadastrar_passageiro(self):
        validador_dados = ValidadorDados()
        # ... restante do código com validação usando self.validador_dados ...
        with st.form(key='cadastro_passageiro_form'):
            nome = st.text_input("Nome completo passageiro:")
            cpf = st.text_input("CPF(XXX.XXX.XXX-XX):")
            dtNasc = st.text_input("Data de nascimento (00/00/0000):")
            contato = st.text_input("Contato:")
            senha = st.text_input("Senha:", type="password")
            endereco = st.text_input("Endereço:")

            formaPag = st.selectbox("Forma de pagamento:", ["Pix", "Cartão de Débito", "Cartão de Crédito", "Dinheiro"])

            if st.form_submit_button("Cadastrar Passgeiro!"):
                if not validador_dados.validaNomeCompleto(nome):
                        st.error("Erro no cadastro de NOME, não está corretamente informado")
                elif not validador_dados.validaCPF(cpf):
                        st.error("Erro no cadastro de CPF, não está corretamente informado")
                elif not validador_dados.validaDataNascimento(dtNasc):
                        st.error("Erro no cadastro de ANO, não está corretamente informado")
                elif not validador_dados.validaContato(contato):
                        st.error("Erro no cadastro de CONTATO, não está corretamente informado")
                else:
                    passageiro = Passageiro(nome, cpf, dtNasc, contato, senha, endereco, formaPag)
                    self.passageiros.append(passageiro)
                    st.success("Cadastro de PASSAGEIRO concluído!")
                    
if __name__ == "__main__":
    cadastro = Cad_Passageiro()
    cadastro.cadastrar_passageiro() 
