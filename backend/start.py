from aws.cliente import S3Client
from contracts.schema import compraShema
from datasource.api import APICollector

schema = compraShema
aws = S3Client()

minha_classe = APICollector(schema, aws).start(1)

print(minha_classe)
