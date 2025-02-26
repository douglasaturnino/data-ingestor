from aws.cliente import S3Client
from contracts.schema import compraShema
from datasource.api import APICollector
from datasource.postgre import PostgresCollector

schema = compraShema
aws = S3Client()

minha_classe = APICollector(schema, aws).start(1)


def getPostgre(aws, dbId):
    postgres = PostgresCollector(aws, dbId).start()


getPostgre(aws, dbId=1)
getPostgre(aws, dbId=2)
