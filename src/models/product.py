class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, data: dict, products: list | None = None):
        if products:
            for product in products:
                if product.name == data["name"]:
                    product.quantity += data["quantity"]
                    product.__price = max(product.__price, data["price"])
                    return product
        return cls(**data)


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, price: float):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif price < self.__price:
            print("Новая цена ниже старой.")
            ch = input("Подтвердите действие y/n: ")
            if ch == "y":
                self.__price = price
        else:
            self.__price = price
