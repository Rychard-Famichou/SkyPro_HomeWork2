from typing import Any

from models.base_category import BaseCategory
from models.zero_except import ZeroExcept


class Order(BaseCategory):
    """Custom class:
    целевой продукт
    целевое количество
    итоговая цена
    """

    all_products: list[Any] = []

    def __init__(self, product_name: str, quantity: int) -> None:
        self.product_name = product_name
        self.quantity = self.check_quantity(quantity)
        self.total_price = self.add_product()

    def __str__(self) -> str:
        """Возвращает строку класса"""
        return f"Заказ на {self.product_name} в количестве {self.quantity} шт."

    @staticmethod
    def check_quantity(quantity: int) -> int:
        """Возвращает количество, если оно больше нуля. Иначе возбуждает ошибку"""
        if quantity <= 0:
            raise ZeroExcept
        return quantity

    def add_product(self) -> float | Any:
        for product in Order.all_products:
            if product.name == self.product_name:
                if product.quantity >= self.quantity:
                    product.quantity -= self.quantity
                    return self.quantity * product.price
                else:
                    print(f"Недостаточно товара {self.product_name} на складе")
                    return 0.0

        print(f"Товара {self.product_name} нет на складе")
        return 0.0

    @property
    def products(self) -> str:
        """Возвращает строку каждого добавленного продукта"""
        return "\n".join(map(str, self.all_products))
