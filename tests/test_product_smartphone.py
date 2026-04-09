from models.product_smartphone import Smartphone


def test_init(product_iphone: Smartphone) -> None:
    """ Тест метода __init__ """
    assert product_iphone.name == "iPhone 15"
    assert product_iphone.description == "Apple"
    assert product_iphone.price == 1000.0
    assert product_iphone.quantity == 10
    assert product_iphone.efficiency == 100.0
    assert product_iphone.model == "iPhone 15"
    assert product_iphone.memory == 128
    assert product_iphone.color == "Black"
