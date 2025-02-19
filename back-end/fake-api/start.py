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
