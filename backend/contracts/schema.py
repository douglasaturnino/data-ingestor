from typing import Dict, Union

GenericShema = Dict[str, Union[str, float, int]]

compraShema: GenericShema = {
    "ean": int,
    "price": float,
    "store": int,
    "dateTime": str,
}
