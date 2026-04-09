from typing import Any, Optional, Self, cast


class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


    def __add__(self, other: "Product") -> float:
        all_price_self = self.price + self.quantity
        all_price_other = other.price + self.quantity
        return all_price_self + all_price_other


    @classmethod
    def new_product(cls, data: dict[str, Any], products: Optional[list["Product"]] = None) -> Self:
        if products:
            for product in products:
                if product.name == data["name"]:
                    product.quantity += data["quantity"]
                    product.__price = max(product.__price, data["price"])
                    return cast(Self, product)

        if products == []:
            print("Объект класса создан, но список пуст")

        return cls(**data)


    @property
    def price(self) -> float:
        return self.__price


    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif price < self.__price:
            print("Новая цена ниже старой.")
            ch = input("Подтвердите действие y/n: ")
            if ch.lower() == "y":
                self.__price = price
        else:
            self.__price = price
