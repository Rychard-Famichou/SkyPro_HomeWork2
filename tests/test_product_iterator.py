import pytest

from models.category import Category
from models.product import Product
from models.product_iterator import ProductIterator


def test_product_iterator_full_cycle(category_electronics: Category,
                                     product_iphone: Product,
                                     product_samsung: Product) -> None:
    """ Проверка полного цикла работы итератора """
    iterator = ProductIterator(category_electronics)

    # 1. Инициализируем итератор
    it = iter(iterator)

    # 2. Проверяем последовательность
    assert next(it) == product_iphone
    assert next(it) == product_samsung

    # 3. Проверяем, что элементы закончились
    with pytest.raises(StopIteration):
        next(it)


def test_product_iterator_reusable(category_electronics: Category,) -> None:
    """ Проверка, что итератор можно перезапустить """
    iterator = ProductIterator(category_electronics)

    # Первый проход
    first_run = list(iterator)
    # Второй проход (благодаря self.current_value = -1 в __iter__)
    second_run = list(iterator)

    assert len(first_run) == 2
    assert first_run == second_run
