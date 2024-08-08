import streamlit as st

def main_Page():
    st.set_page_config(page_title="BIDVAN.COM")
        
    with open("estilo.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
            
        st.title('BIDVAN')

    if st.button("Cadastro"):
        st.experimental_set_query_params(page='cadastro')
        
    if st.button("Login"):
        st.experimental_set_query_params(page='login')