import requests
import streamlit as st
import pandas as pd

url = 'https://viacep.com.br/ws/{cep}/json/'

st.title('Busca CEP')

cep = st.text_input('Busque seu cep')

if cep != '':

    try:
        response = requests.get(url.format(cep=cep))
        data = pd.DataFrame([response.json()])
        st.dataframe(data)
    except Exception as err:
        st.error("Entre com um CEP válido")
        



