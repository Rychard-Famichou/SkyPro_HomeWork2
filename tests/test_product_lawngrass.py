from models.product_lawngrass import LawnGrass


def test_init(product_rus_grass: LawnGrass) -> None:
    """ Тест метода __init__ """
    assert product_rus_grass.name == "Камыш"
    assert product_rus_grass.description == "Издалека напоминает камыш"
    assert product_rus_grass.price == 100.0
    assert product_rus_grass.quantity == 10
    assert product_rus_grass.country == "Россия"
    assert product_rus_grass.germination_period == "7 дней"
    assert product_rus_grass.color == "Бурый"
