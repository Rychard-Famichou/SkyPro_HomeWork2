from typing import Any, List

import pytest

from models.category import Category
from models.order import Order
from models.product import Product
from models.product_lawngrass import LawnGrass
from models.product_smartphone import Smartphone


@pytest.fixture
def setup_order() -> type[Order]:
    """Фикстура для очистки списка продуктов перед каждым тестом"""
    Order.all_products.clear()
    return Order


@pytest.fixture
def sample_products(setup_order: Order, product_iphone: Product, product_samsung: Product) -> tuple[Product, Product]:
    """Фикстура для наполнения склада тестовыми данными"""
    p1 = product_iphone
    p2 = product_samsung
    return p1, p2


@pytest.fixture
def product_iphone() -> Smartphone:
    """Фикстура для создания одного объекта класса"""
    return Smartphone("iPhone 15", "Apple", 1000.0, 10, 100.0, "iPhone 15", 128, "Black")


@pytest.fixture
def product_samsung() -> Smartphone:
    """Фикстура для создания одного объекта класса"""
    return Smartphone("Samsung S23", "Android", 800.0, 5, 100.0, "Samsung S23", 64, "White")


@pytest.fixture
def product_xiaomi() -> Product:
    """Фикстура для создания одного объекта класса"""
    return Product("Xiaomi Mi 13", "Android", 600.0, 15)


@pytest.fixture
def product_nokia() -> Product:
    """Фикстура для создания одного объекта класса"""
    return Product("Nokia 3310", "Legendary phone", 50.0, 100)


@pytest.fixture
def product_rus_grass() -> LawnGrass:
    """Фикстура для создания одного объекта класса"""
    return LawnGrass("Камыш", "Издалека напоминает камыш", 100.0, 10, "Россия", "7 дней", "Бурый")


@pytest.fixture
def product_nokia_dict() -> dict[str, Any]:
    """Фикстура для создания словаря"""
    return {"name": "Nokia 3310", "description": "Legendary phone", "price": 50.0, "quantity": 100}


@pytest.fixture(autouse=True)
def reset_category_counts() -> None:
    """Автоматически сбрасывает счетчики классов перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def category_electronics(product_iphone: Product, product_samsung: Product) -> Category:
    """Фикстура для создания категории с двумя товарами"""
    return Category("Электроника", "Гаджеты и техника", [product_iphone, product_samsung])


@pytest.fixture
def products_list(category_electronics: Category) -> List[Product]:
    """Фикстура для создания категории с двумя товарами в форме списка"""
    return category_electronics.products_list


@pytest.fixture
def sample_data() -> List[dict[str, Any]]:
    """Фикстура с типичными данными из JSON"""
    return [
        {
            "name": "Электроника",
            "description": "Гаджеты и устройства",
            "products": [
                {"name": "Смартфон", "description": "Новая модель", "price": 50000.0, "quantity": 10},
                {"name": "Наушники", "description": "Беспроводные", "price": 5000.0, "quantity": 20},
            ],
        }
    ]
