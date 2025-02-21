from datetime import datetime
from io import BytesIO
from typing import List

import pandas as pd
import pyarrow.parquet as pq
import requests
from contracts.schema import GenericSchema


class APICollector:
    def __init__(self, schema, aws):
        self._schema = schema
        self._aws = aws
        self._buffer = None
        return

    def start(self, param):
        response = self.getData(param)
        response = self.extractData(response)
        response = self.transformDf(response)
        response = self.convertToParquet(response)

        if self._buffer is not None:
            file_name = self.fileName()
            print(file_name)
            self._aws.upload_file(response, file_name)
            return True

        return False

    def getData(self, param):
        response = None
        if param > 1:
            response = requests.get(
                f"http://127.0.0.01:8000/gerar_compras/{param}"
            ).json()
        else:
            response = requests.get(
                "http://127.0.0.01:8000/gerar_compra"
            ).json()
        return response

    def extractData(self, response):
        result: List[GenericSchema] = []
        for item in response:
            index = {}
            for key, value in self._schema.items():
                if type(item.get(key)) == value:
                    index[key] = item[key]
                else:
                    index[key] = None

            result.append(index)

        return result

    def transformDf(self, response):
        result = pd.DataFrame(response)
        return result

    def convertToParquet(self, response):
        self._buffer = BytesIO()
        try:
            response.to_parquet(self._buffer)
            return self._buffer
        except Exception as e:
            print(f"Error ao transformar o DF em parquet: {e}")
            self._buffer = None

    def fileName(self):
        data_atual = datetime.now().isoformat()
        match = data_atual.split(".")
        return f"api/api-reponse-compra{match[0]}.parquet"
