import streamlit as st
import random

st.title("Desafio Babilônia")

# Inicializa as variáveis na memória do Streamlit
if 'numero_sorteado' not in st.session_state:
    st.session_state.numero_sorteado = random.randint(1, 15)
    st.session_state.tentativas = 0

# Entrada do usuário
numero_usuario = st.text_input("Digite um número de 1 a 15:")

if st.button("Tentar"):
    if numero_usuario.isdigit():
        numero_usuario = int(numero_usuario)
        
        if 1 <= numero_usuario <= 15:
            st.session_state.tentativas += 1
            
            if numero_usuario == st.session_state.numero_sorteado:
                st.success(f"Parabéns! Você acertou em {st.session_state.tentativas} tentativas!")
                st.balloons()
            elif st.session_state.tentativas >= 3:
                st.error(f"Acabaram as tentativas! O número era {st.session_state.numero_sorteado}.")
            else:
                st.warning(f"Errado! Tentativa {st.session_state.tentativas} de 3.")
        else:
            st.error("Por favor, digite um número entre 1 e 15.")
    else:
        st.error("Entrada inválida. Digite um número inteiro.")
        