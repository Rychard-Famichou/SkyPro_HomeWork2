from models.product import Product


def test_product_init(product_iphone: Product) -> None:
    """ Тест инициализации класса """
    assert product_iphone.name == "iPhone 15"
    assert product_iphone.description == "Apple"
    assert product_iphone.price == 1000.0
    assert product_iphone.quantity == 10
