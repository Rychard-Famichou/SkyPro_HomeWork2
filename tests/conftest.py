from typing import Any, List

import pytest

from models.category import Category
from models.product import Product


@pytest.fixture
def product_iphone() -> Product:
    """Фикстура для создания одного товара"""
    return Product("iPhone 15", "Apple", 1000.0, 10)


@pytest.fixture
def product_samsung() -> Product:
    """Фикстура для создания одного товара"""
    return Product("Samsung S23", "Android", 800.0, 5)


@pytest.fixture
def category_electronics(product_iphone: Product, product_samsung: Product) -> Category:
    """Фикстура для создания категории с двумя товарами"""
    return Category("Электроника", "Гаджеты и техника", [product_iphone, product_samsung])


@pytest.fixture
def sample_data() -> List[dict[str, Any]]:
    """Фикстура с типичными данными из JSON"""
    return [
        {
            "name": "Электроника",
            "description": "Гаджеты и устройства",
            "products": [
                {
                    "name": "Смартфон",
                    "description": "Новая модель",
                    "price": 50000.0,
                    "quantity": 10
                },
                {
                    "name": "Наушники",
                    "description": "Беспроводные",
                    "price": 5000.0,
                    "quantity": 20
                }
            ]
        }
    ]
