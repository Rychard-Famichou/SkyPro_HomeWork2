from models.product import Product


class Smartphone(Product):
    """ Custom class:
    Название
    Описание
    Цена
    Количество
    Производительность
    Модель
    Объем встроенной памяти
    Цвет
    """

    def __init__(self,
                 name: str,
                 description: str,
                 price: float,
                 quantity: int,
                 efficiency: float,
                 model: str,
                 memory: int,
                 color: str) -> None:
        """ Создание объекта класса """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
