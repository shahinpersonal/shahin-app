import streamlit as st

# --- CONFIGURAÇÃO VISUAL SHAHIN ---
st.set_page_config(page_title="Shahin Avaliação Física", layout="centered")

# CSS para cores Roxo, Vermelho e Branco
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    [data-testid="stSidebar"] { background-color: #4B0082; }
    .stSidebar * { color: white !important; }
    h1, h2, h3 { color: #4B0082; font-family: 'Arial Black'; }
    .stButton>button { 
        background-color: #E63946; color: white; 
        font-weight: bold; border-radius: 10px; height: 3.5em; width: 100%;
    }
    .footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: #4B0082; color: white;
        text-align: center; padding: 10px; font-size: 13px;
        border-top: 4px solid #E63946; z-index: 100;
    }
    .stMetric { background-color: #f8f9fa; padding: 15px; border-radius: 10px; border: 1px solid #ddd; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGAÇÃO ---
st.sidebar.title("MENU")
aba = st.sidebar.radio("Ir para:", ["Cadastro", "Anamnese", "Avaliação (Dobras)", "Bioimpedância", "Perímetros"])

st.title("🧬 SHAHIN")
st.subheader("Avaliação Física Evolution")

# --- MÓDULO 1: CADASTRO ---
if aba == "Cadastro":
    st.write("### 👤 Cadastro do Aluno")
    nome = st.text_input("Nome Completo")
    email = st.text_input("E-mail")
    data_aval = st.date_input("Data da Avaliação")
    peso = st.number_input("Peso Atual (kg)", format="%.2f")
    altura = st.number_input("Altura (m)", format="%.2f")
    if altura > 0:
        imc = peso / (altura ** 2)
        st.info(f"IMC Calculado: {imc:.2f}")

# --- MÓDULO 2: ANAMNESE ---
elif aba == "Anamnese":
    st.write("### 📝 Anamnese")
    obj = st.selectbox("Objetivo", ["Emagrecimento", "Hipertrofia", "Condicionamento", "Saúde"])
    lesao = st.text_area("Possui alguma lesão ou limitação?")
    medicamento = st.text_area("Faz uso de algum medicamento?")
    sono = st.select_slider("Qualidade do Sono", options=["Péssima", "Ruim", "Regular", "Boa", "Excelente"])

# --- MÓDULO 3: ANTROPOMETRIA ---
elif aba == "Avaliação (Dobras)":
    st.write("### 📏 Protocolo de Dobras (mm)")
    c1, c2 = st.columns(2)
    with c1:
        tri = st.number_input("Tríceps")
        sub = st.number_input("Subescapular")
        bic = st.number_input("Bíceps")
        axm = st.number_input("Axilar Média")
        peit = st.number_input("Peitoral")
    with c2:
        supra = st.number_input("Supra-ilíaca")
        abd = st.number_input("Abdominal")
        coxa = st.number_input("Coxa")
        pant = st.number_input("Panturrilha")
        idade = st.number_input("Idade do Aluno", min_value=1)
    
    sexo = st.selectbox("Sexo para Cálculo", ["Masculino", "Feminino"])
    
    if st.button("CALCULAR COMPOSIÇÃO CORPORAL"):
        # Soma 7 Dobras
        soma7 = tri + sub + axm + peit + supra + abd + coxa
        if sexo == "Masculino":
            dc = 1.097 - (0.00046971 * soma7) + (0.00000056 * (soma7**2)) - (0.00012828 * idade)
        else:
            dc = 1.097 - (0.00046971 * soma7) + (0.00000056 * (soma7**2)) - (0.00012828 * idade)
        
        gordura = ((4.95 / dc) - 4.50) * 100
        st.metric("Percentual de Gordura (%G)", f"{gordura:.2f}%")
        st.balloons()

# --- MÓDULO 4: BIOIMPEDÂNCIA ---
elif aba == "Bioimpedância":
    st.write("### ⚖️ Dados de Bioimpedância")
    col1, col2 = st.columns(2)
    g_bio = col1.number_input("% Gordura (Balança)")
    m_bio = col2.number_input("% Massa Muscular")
    visceral = col1.number_input("Gordura Visceral")
    metab = col2.number_input("Idade Metabólica")
    tmb = st.number_input("Taxa Metabólica Basal (kcal)")

# --- RODAPÉ ---
st.markdown(f"""
    <div class="footer">
        <b>Samer Abdalla Fawzi Shahin</b> | Personal Trainer | <b>CREF 033699-G/SP</b><br>
        📞 11 995462603 | Shahin Avaliação Física
    </div>
    """, unsafe_allow_html=True)
