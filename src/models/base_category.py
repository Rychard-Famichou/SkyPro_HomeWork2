from abc import ABC, abstractmethod


class BaseCategory(ABC):
    """
    Custom abstract class
    """

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
