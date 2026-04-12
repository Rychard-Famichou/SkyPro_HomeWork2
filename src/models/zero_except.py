class ZeroQuantityError(Exception):
    """Custom class, Ошибка:
    Если попытаться добавить продукт с 0 количеством товара
    """

    def __init__(self, *args: str) -> None:
        self.message: str = args[0] if args else "Товар с нулевым количеством не может быть добавлен"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
