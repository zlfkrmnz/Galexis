class Sale:
    def __init__(self, _id: int, artwork_id: int, customer_id: int, sale_date: str, sale_price: float) -> None:
        self.__id = _id
        self.__artwork_id = artwork_id
        self.__customer_id = customer_id
        self.__sale_date = sale_date
        self.__sale_price = sale_price

    def record_sale(self) -> None:
        pass
