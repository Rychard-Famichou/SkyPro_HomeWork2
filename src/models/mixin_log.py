from typing import Any

from models.order import Order


class MixinLog:

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        print(repr(self))
        Order.all_products.append(self)
