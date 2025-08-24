import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(
    page_title='Analise de dados',
    page_icon= '🎲',
    layout='wide'
)

# --- Ocult menus ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def title():
    titulo = st.markdown("<h1 style='text-align: center; color:  #FFD700;'>API PyGWalker & Streamlit</h1>", unsafe_allow_html=True)
    st.divider()
    return titulo


def upload():
    uploaded_file = st.sidebar.file_uploader("Escolha um arquivo", type=["csv", "xlsx", "xls"])
    st.sidebar.divider()
    st.sidebar.markdown("""
        **Desenvolvido por Leandro Souza**  
        [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/leandro-souza-dados/)
        [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lsouzadasilva)
        """)
    return uploaded_file

def main():
    uploaded_file = upload()
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        pyg_app = StreamlitRenderer(df, spec="./gw_config.json", spec_io_mode="rw")
        pyg_app.explorer()
        
if __name__ == "__main__":
    title()
    main()
    


