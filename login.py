import streamlit as st
from validadorDados import ValidadorDados
from classes.passageiro import Passageiro
from classes.motorista import Motorista
from cadastros.cad_passageiro import Cad_Passageiro
from cadastros.cad_motorista import Cad_Motorista

class Login:
    def login(self, cadastro_passageiro, cadastro_motorista):
        validador_dados = ValidadorDados()
        print(cadastro_passageiro.passageiros[0].nome)
        with st.form(key='login_form'):
            cpf_cnpj = st.text_input("CPF/CNPJ:")
            senha = st.text_input("Senha:", type="password")

            if st.form_submit_button("Login"):
                passageiro_encontrado = next((p for p in cadastro_passageiro.passageiros if isinstance(p, Passageiro) and p.CPF == cpf_cnpj and p.senha == senha), None)
                motorista_encontrado = next((m for m in cadastro_motorista.motoristas if isinstance(m, Motorista) and m.CNPF == cpf_cnpj and m.senha == senha), None)
                
                if passageiro_encontrado:
                    st.success("Login de Passageiro bem-sucedido!")
                    # Lógica adicional após o login bem-sucedido do passageiro
                elif motorista_encontrado:
                    st.success("Login de Motorista bem-sucedido!")
                    # Lógica adicional após o login bem-sucedido do motorista
                else:
                    st.error("CPF/CNPJ ou senha incorretos. Tente novamente.")
