import streamlit as st
from cadastros.cad_passageiro import Cad_Passageiro
from cadastros.cad_motorista import Cad_Motorista
from classes.passageiro import Passageiro
from login import Login
from views import cadastro_page
from views import main_page
from views import login_page

def main():
    page = st.experimental_get_query_params().get('page', ['main'])[0]

    cadastro_passageiro = Cad_Passageiro()
    cadastro_motorista = Cad_Motorista()
    login_usuario = Login()
    nome_passageiro = "João"
    dtNasc_passageiro = "1990-01-01"
    contato_passageiro = "123456789"
    senha_passageiro = "senha123"
    endereco_passageiro = "Rua ABC, 123"
    formaPag_passageiro = "Cartão de Crédito"
    CPF_passageiro = "123.456.789-00"

    # Crie uma instância da classe Passageiro
    passageiro = Passageiro(nome_passageiro, dtNasc_passageiro, contato_passageiro, senha_passageiro, endereco_passageiro, formaPag_passageiro, CPF_passageiro)
    cadastro_passageiro.passageiros.append(passageiro)

    
    if page == 'main':
        main_page.main_Page()
    elif page == 'cadastro':
        cadastro_page.cadastro_Page(cadastro_passageiro, cadastro_motorista)
    elif page == 'login':
        login_page.login_Page(login_usuario, cadastro_passageiro, cadastro_motorista)

if __name__ == '__main__':
    main()