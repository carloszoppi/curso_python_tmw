import streamlit as st
import pandas as pd

import requests

URL = "https://viacep.com.br/ws/{cep}/json/"

st.title("Busca CEP")

if cep:  # Verifica se o usuário digitou algo
    resp = requests.get(URL.format(cep=cep))
    
    if resp.status_code == 200:
        dados_json = resp.json()
        
        # Verifica se o ViaCEP retornou um CEP inexistente
        if "erro" in dados_json:
            st.error("CEP não encontrado!")
        else:
            # Passando o dicionário dentro de uma lista [] para o Pandas aceitar
            data = pd.DataFrame([dados_json]) 
            st.dataframe(data)
    else:
        st.error("Erro ao conectar com o serviço ViaCEP.")
