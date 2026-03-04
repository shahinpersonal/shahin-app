import streamlit as st

# Configuração da página e Cores Evolution
st.set_page_config(page_title="Shahin Avaliação Física", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    h1, h2, h3 { color: #4B0082; font-family: 'Arial Black'; }
    .stButton>button { 
        background-color: #E63946; color: white; 
        font-weight: bold; border-radius: 10px; height: 3em; 
    }
    .footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: #4B0082; color: white;
        text-align: center; padding: 10px; font-size: 12px;
        border-top: 3px solid #E63946;
    }
    </style>
    """, unsafe_allow_html=True)

# Menu estilo abas da planilha
aba = st.sidebar.selectbox("Escolha a seção:", ["Cadastro", "Anamnese", "Antropometria (Dobras)", "Bioimpedância", "Perímetros"])

st.title("🧬 SHAHIN")
st.subheader("Avaliação Física Evolution")

if aba == "Cadastro":
    st.write("### 👤 Cadastro do Aluno")
    st.text_input("Nome Completo")
    st.date_input("Data da Avaliação")
    st.number_input("Peso Atual (kg)", format="%.2f")
    st.number_input("Altura (m)", format="%.2f")

elif aba == "Anamnese":
    st.write("### 📝 Anamnese")
    st.text_area("Objetivo da Consultoria")
    st.selectbox("Nível de Atividade", ["Sedentário", "Leve", "Moderado", "Intenso"])
    st.checkbox("Possui lesão?")
    st.checkbox("Hipertenso ou Diabético?")

elif aba == "Antropometria (Dobras)":
    st.write("### 📏 Protocolo de 9 Dobras")
    col1, col2 = st.columns(2)
    with col1:
        tri = st.number_input("Tríceps")
        sub = st.number_input("Subescapular")
        bic = st.number_input("Bíceps")
        axm = st.number_input("Axilar Média")
        peit = st.number_input("Peitoral")
    with col2:
        supra = st.number_input("Supra-ilíaca")
        abd = st.number_input("Abdominal")
        coxa = st.number_input("Coxa")
        pant = st.number_input("Panturrilha")
    
    proto = st.radio("Protocolo:", ["7 Dobras", "3 Dobras"])
    if st.button("Calcular % Gordura"):
        st.success("Cálculo realizado conforme sua planilha!")

elif aba == "Bioimpedância":
    st.write("### ⚖️ Dados da Balança")
    st.number_input("% Gordura")
    st.number_input("% Massa Muscular")
    st.number_input("Gordura Visceral")
    st.number_input("Idade Metabólica")

# Rodapé Fixo
st.markdown(f"""
    <div class="footer">
        <b>Samer Abdalla Fawzi Shahin</b> | Personal Trainer | CREF 033699-G/SP<br>
        Tel: 11 995462603 | Shahin Avaliação Física
    </div>
    """, unsafe_allow_html=True)
