import openpyxl
import pandas as pd
import streamlit as st


class CSVCollector:
    def __init__(self, schema, aws, cell_range):
        self._schema = schema
        self._aws = aws
        self.cell_range = cell_range
        return

    def start(self):
        getData = self.getData()

        if getData is not None:
            extractData = self.extractData(getData)
        if extractData is not None:
            validateData = self.validateData(extractData)
            return validateData

    def getData(self):
        dados_excel = st.file_uploader(
            "Insira o arquivo Excel", type=("csv", "xlsx")
        )
        return dados_excel

    def extractData(self, dados_excel):
        workbook = openpyxl.load_workbook(dados_excel)
        sheet = workbook.active
        range_cell = sheet[self.cell_range]

        headers = [cell.value for cell in range_cell[0]]

        data = []
        for row in range_cell[1:]:
            data.append([cell.value for cell in row])

        dataframe = pd.DataFrame(data, columns=headers)
        return dataframe
