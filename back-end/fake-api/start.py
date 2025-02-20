import os
import random

import pandas as pd
from faker import Faker
from fastapi import FastAPI

app = FastAPI()
fake = Faker()

file_name = os.path.join(os.path.dirname(__file__), "produto.csv")
df = pd.read_csv(file_name)
df["index"] = range(1, len(df) + 1)
df.set_index("index", inplace=True)


@app.get("/gerar_compra")
async def gerar_compra():
    index = random.randint(1, len(df) - 1)
    tuple = df.iloc[index]
    return {
        "cliente": fake.name(),
        "creditcard": fake.credit_card_provider(),
        "product": tuple["produto"],
        "ean": int(tuple["ean"]),
        "price": round(float(tuple["price"]) * 1.2, 2),
        "store": 11,
        "dateTime": fake.iso8601(),
        "clientPosition": fake.location_on_land(),
    }


@app.get("/gerar_compras/{numero_registro}")
async def gerar_compras(numero_registro: int):
    if numero_registro < 1:
        return {"error": "O número deve ser maior que 1"}

    respostas = []

    for _ in range(numero_registro):
        index = random.randint(1, len(df) - 1)
        tuple = df.iloc[index]
        compra = {
            "cliente": fake.name(),
            "creditcard": fake.credit_card_provider(),
            "product": tuple["produto"],
            "ean": int(tuple["ean"]),
            "price": round(float(tuple["price"]) * 1.2, 2),
            "clientPosition": fake.location_on_land(),
            "store": 11,
            "dateTime": fake.iso8601(),
        }
        respostas.append(compra)

    return respostas
