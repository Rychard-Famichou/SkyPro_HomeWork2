from typing import Any

import pytest

from models.category import Category
from models.product import Product


def test_category_init(category_electronics: Category) -> None:
    """ Тест инициализации класса """
    assert category_electronics.name == "Электроника"
    assert category_electronics.description == "Гаджеты и техника"
    assert category_electronics.category_count == 1
    assert category_electronics.product_count == 2
    assert category_electronics.products_list[1].name == "Samsung S23"
    assert category_electronics.products_list[1].description == "Android"
    assert category_electronics.products_list[1].price == 800.0
    assert category_electronics.products_list[1].quantity == 5


def test_str(category_electronics: Category) -> None:
    assert str(category_electronics) == "Электроника, количество продуктов: 15 шт."


def test_category_products_property(category_electronics: Category) -> None:
    """ Тест строкового представления списка товаров в категории """
    expected_output = (
        "iPhone 15, 1000.0 руб. Остаток: 10 шт.\n"
        "Samsung S23, 800.0 руб. Остаток: 5 шт."
    )
    assert category_electronics.products == expected_output


def test_add_product(category_electronics: Category, product_xiaomi: Product) -> None:
    """ Тест метода add_product: успех """
    category_electronics.add_product(product_xiaomi)

    assert category_electronics.product_count == 3
    assert category_electronics.products_list[2].name == "Xiaomi Mi 13"


def test_add_product_error(category_electronics: Category,  product_nokia_dict: dict[str, Any]) -> None:
    """ Тест метода add_product: ошибка """
    with pytest.raises(TypeError) as excinfo:
        category_electronics.add_product(product_nokia_dict) # type: ignore[arg-type]

    assert str(excinfo.value) == "Добавлять можно только объекты классов Product или его наследников"
