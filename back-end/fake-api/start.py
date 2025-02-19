from fastapi import FastAPI

app = FastAPI()


@app.get("/gerar_compra")
async def gerar_compra():
    return {
        "cliente": "Nome",
        "creditcard": "Tipo de cartão",
        "ean": "Código de barras do produto",
        "price": "Preço do produto",
        "store": 11,
        "dateTime": "Data da compra",
        "clientPosition": "Posição do cliente",
    }
