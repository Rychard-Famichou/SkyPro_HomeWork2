from typing import Any, List

from models.category import Category
from models.product import Product
from utils.converters import create_objects


def test_create_objects_success(sample_data: List[dict[str, Any]]) -> None:
    """Проверка успешного создания категорий и товаров"""
    result = create_objects(sample_data)

    # Проверяем количество категорий
    assert len(result) == 1
    assert isinstance(result[0], Category)
    assert result[0].name == "Электроника"

    # Проверяем товары внутри категории
    products = result[0].products
    assert len(products) == 2
    assert isinstance(products[0], Product)
    assert products[0].name == "Смартфон"
    assert products[1].price == 5000.0

def test_create_objects_empty_list() -> None:
    """Проверка работы с пустым списком"""
    assert create_objects([]) == []

def test_create_objects_no_products() -> None:
    """Проверка категории без товаров"""
    data = [{
        "name": "Пустая",
        "description": "Нет товаров",
        "products": []
    }]
    result = create_objects(data)
    assert len(result) == 1
    assert result[0].products == []
