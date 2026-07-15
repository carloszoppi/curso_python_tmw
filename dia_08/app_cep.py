import streamlit as st
import requests
import pandas as pd


URL = "https://viacep.com.br/ws/{cep}/json/"

st.title("Busca CEP")

cep = st.text_input("Busque seu CEP: ")

if cep != "":
   
   try: # para o caso de CEP inválido
       resp = requests.get(URL.format(cep=cep))
       data = pd.DataFrame([resp.json()])
       st.dataframe(data) # é o que mostra o resultado e formato de tabela.

   except Exception as err:
       st.error("Entre com CEP válido")



    
