from typing import Any, Optional, Self, cast

from models.base_product import BaseProduct
from models.mixin_log import MixinLog


class Product(MixinLog, BaseProduct):
    """Custom class:
    Название
    Описание
    Цена
    Количество
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Создание объекта класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __repr__(self) -> str:
        """Возвращает строку класса для отладки"""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"

    def __str__(self) -> str:
        """Возвращает строку класса"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Возвращает цену * количество двух продуктов"""
        if type(self) is type(other):
            all_price_self = self.price * self.quantity
            all_price_other = other.price * other.quantity
            return all_price_self + all_price_other
        else:
            raise TypeError("Можно складывать только продукты одного класса")

    @classmethod
    def new_product(cls, data: dict[str, Any], products: Optional[list["Product"]] = None) -> Self:
        """Возвращает объект класса:
        принимает словарь,
        складывает количество,
        цена наивысшая
        """
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
        """Возвращает приватный атрибут: Цена"""
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        """Условное изменение атрибута: Цена"""
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif price < self.__price:
            print("Новая цена ниже старой.")
            ch = input("Подтвердите действие y/n: ")
            if ch.lower() == "y":
                self.__price = price
        else:
            self.__price = price
