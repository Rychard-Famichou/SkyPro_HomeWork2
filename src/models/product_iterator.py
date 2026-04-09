from typing import Self

from models.category import Category
from models.product import Product


class ProductIterator:
    """ Класс-итератор позволяет перебрать объекты класса Product в классе Category """

    def __init__(self, category: Category) -> None:
        """ Создание объекта класса """
        self.category = category

    def __iter__(self) -> Self:
        """ Возвращает итератор """
        self.current_value  = -1
        return self

    def __next__(self) -> Product:
        """ Возвращает каждый объект класса Product из списка продуктов в классе Category """
        if self.current_value  +1 < len(self.category.products_list):
            self.current_value  += 1
            return self.category.products_list[self.current_value ]
        else:
            raise StopIteration
