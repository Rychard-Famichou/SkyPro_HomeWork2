from models.category import Category


def test_category_init(category_electronics: Category) -> None:
    """ Тест инициализации класса """
    assert category_electronics.name == "Электроника"
    assert category_electronics.description == "Гаджеты и техника"
    assert category_electronics.category_count == 1
    assert category_electronics.product_count == 2
    assert category_electronics.products[1].name == "Samsung S23"
    assert category_electronics.products[1].description == "Android"
    assert category_electronics.products[1].price == 800.0
    assert category_electronics.products[1].quantity == 5
