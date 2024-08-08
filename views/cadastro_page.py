import streamlit as st
from cadastros.cad_motorista import Cad_Motorista
from cadastros.cad_passageiro import Cad_Passageiro

def cadastro_Page(cadastro_passageiro, cadastro_motorista):
    with open("estilo.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        st.title('Cadastro')
        menu_opcoes = ['Cadastro Passageiro', 'Cadastro Motorista']
        escolha = st.selectbox('Escolha a opção:', menu_opcoes)

        if escolha == 'Cadastro Passageiro':
            cadastro_passageiro.cadastrar_passageiro()

        elif escolha == 'Cadastro Motorista':
            cadastro_motorista.cadastrar_motorista()