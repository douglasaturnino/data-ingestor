import requests


class APICollector:
    def __init__(self):
        self._schema = None
        self._aws = None
        self._buffer = None
        return

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
