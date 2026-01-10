"""
Базовый класс `Vehicle`
"""

from abc import ABC
from homework_05.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    """
    Базовый класс для транспортных средств

    Атрибуты:
    - weight: вес транспортного средства (по умолчанию 0)
    - started: состояние двигателя (по умолчанию False)
    - fuel: количество топлива (по умолчанию 0)
    - fuel_consumption: расход топлива на единицу расстояния (по умолчанию 0)
    """

    def __init__(self, weight: float = 0, fuel: float = 0, fuel_consumption: float = 0):
        """
        Инициализация транспортного средства

        Аргументы:
        - weight: вес транспортного средства
        - fuel: количество топлива
        - fuel_consumption: расход топлива на единицу расстояния
        """
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self) -> None:
        """
        Запуск двигателя транспортного средства

        Проверяет состояние started. Если не started, то проверяет, что топлива больше нуля,
        и обновляет состояние started, иначе выкидывает исключение LowFuelError
        """
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Недостаточно топлива для запуска")

    def move(self, distance: float) -> None:
        """
        Движение транспортного средства на указанное расстояние

        Проверяет, что топлива достаточно для преодоления переданной дистанции,
        и изменяет количество оставшегося топлива, иначе выкидывает исключение NotEnoughFuel

        Аргументы:
        - distance: расстояние для преодоления
        """
        required_fuel = distance * self.fuel_consumption

        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
        else:
            raise NotEnoughFuel(
                f"Недостаточно топлива. Нужно: {required_fuel:.2f}, осталось: {self.fuel:.2f}"
            )