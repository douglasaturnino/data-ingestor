import streamlit as st


class CSVCollector:
    def __init__(self, schema, aws):
        pass

    def getData(self, param):
        dados_excel = st.file_uploader(
            "Insira o arquivo Excel", type=("csv", "xlsx")
        )
        return dados_excel
