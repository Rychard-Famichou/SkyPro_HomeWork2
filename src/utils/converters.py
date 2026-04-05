from typing import Any

from models.category import Category
from models.product import Product


def create_objects(data: list[dict[str, Any]]) -> list[Category]:
    """Превращает список словарей из JSON в объекты классов Category и Product"""
    categories = []

    for category_dict in data:
        products = []
        # Сначала создаем объекты товаров для этой категории
        for product_dict in category_dict.get('products', []):
            product = Product(
                name=product_dict['name'],
                description=product_dict['description'],
                price=product_dict['price'],
                quantity=product_dict['quantity']
            )
            products.append(product)

        # Затем создаем саму категорию, передавая ей список объектов товаров
        category = Category(
            name=category_dict['name'],
            description=category_dict['description'],
            products=products
        )
        categories.append(category)

    return categories
