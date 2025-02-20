from contracts.schema import compraShema
from datasource.api import APICollector

schema = compraShema
minha_classe = APICollector(schema).start(1)

print(minha_classe)
