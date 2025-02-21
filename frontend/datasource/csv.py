import streamlit as st


class CSVCollector:
    def __init__(self, schema, aws):
        pass

    def getData(self, param):
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
