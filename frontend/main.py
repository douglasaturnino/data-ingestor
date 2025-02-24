import streamlit as st
from aws.cliente import S3Client
from contract.catalogo import Catalogo
from datasource.csv import CSVCollector

aws_instancia = S3Client()

st.title("Essa é uma página de portal de dados")

catalogo_de_produto = CSVCollector(Catalogo, aws_instancia, "C11:I211")
catalogo_de_produto.start()
