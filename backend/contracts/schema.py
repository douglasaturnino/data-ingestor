from typing import Dict, Union

GenericSchema = Dict[str, Union[str, float, int]]

compraShema: GenericSchema = {
    "ean": int,
    "price": float,
    "store": int,
    "dateTime": str,
}
