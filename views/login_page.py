import streamlit as st
from login import Login
from cadastros.cad_passageiro import Cad_Passageiro
from cadastros.cad_motorista import Cad_Motorista
from classes.passageiro import Passageiro

def login_Page(login_usuario, cadastro_passageiro, cadastro_motorista):
    st.set_page_config(page_title="BIDVAN.COM")

    # print(cadastro_passageiro.passageiros[0].nome)
    with open("estilo.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    login_usuario.login(cadastro_passageiro, cadastro_motorista)