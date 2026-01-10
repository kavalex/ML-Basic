"""
Создайте класс `Car`, наследник `Vehicle`
"""

from homework_05.base import Vehicle
from homework_05.engine import Engine


class Car(Vehicle):
    """
    Класс автомобиля, наследник Vehicle

    Дополнительные атрибуты:
    - engine: двигатель автомобиля (экземпляр класса Engine)
    """

    def __init__(self, weight: float = 0, fuel: float = 0, fuel_consumption: float = 0):
        """
        Инициализация автомобиля

        Аргументы:
        - weight: вес автомобиля
        - fuel: количество топлива
        - fuel_consumption: расход топлива на единицу расстояния
        """
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine: Engine) -> None:
        """
        Установка двигателя на автомобиль

        Аргументы:
        - engine: экземпляр объекта Engine для установки
        """
        self.engine = engine