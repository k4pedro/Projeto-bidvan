import streamlit as st
from validadorDados import ValidadorDados
from classes.motorista import Motorista
from classes.veiculo import Veiculo
from classes.contrato import Contrato

class Cad_Motorista:
    def __init__(self):
        self.motoristas = []
    
    def cadastrar_motorista(self):
        validador_dados = ValidadorDados()

        with st.form(key='cadastro_motorista_form'):
            # Seu código para a interface de entrada de dados
            nome = st.text_input("Nome:")
            cnh = st.text_input("CNH (10 digitos):")
            cnpj = st.text_input("CNPJ (XX.XXX.XXX/0001-XX):")
            dtNasc = st.text_input("Data de nascimento (00/00/0000):", value=None)
            contato = st.text_input("Contato:")
            senha = st.text_input("Senha:")
            endereco = st.text_input("Endereço:")
            areaDeAtuacao = st.selectbox("Area de atuação:", ["Escolar", "Evento", "Empresarial", "Faculdade", "Outros"]).lower()

            if st.form_submit_button("Cadastrar Motorista!"):
                if validador_dados.validaCadastroMotorista(nome, cnh, cnpj, dtNasc, contato):
                    motorista = Motorista(nome, cnpj, cnh, dtNasc, contato, senha, endereco, areaDeAtuacao)
                    self.motoristas.append(motorista)
                    st.success("Cadastro de MOTORISTA concluído!")
                else:
                    st.error("Erro no cadastro. Verifique os dados informados.")
    
if __name__ == "__main__":
    cadastro_motorista = Cad_Motorista()
    cadastro_motorista.cadastrar_motorista()
