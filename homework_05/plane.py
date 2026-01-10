"""
Создайте класс `Plane`, наследник `Vehicle`
"""

from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload


class Plane(Vehicle):
    """
    Класс самолета, наследник Vehicle

    Дополнительные атрибуты:
    - cargo: текущий груз
    - max_cargo: максимальная грузоподъемность
    """

    def __init__(self, weight: float = 0, fuel: float = 0, fuel_consumption: float = 0, max_cargo: float = 0):
        """
        Инициализация самолета с учетом максимальной грузоподъемности

        Аргументы:
        - weight: вес самолета
        - fuel: количество топлива
        - fuel_consumption: расход топлива на единицу расстояния
        - max_cargo: максимальная грузоподъемность
        """
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, weight: float) -> None:
        """
        Загрузка груза на самолет

        Проверяет, что в сумме с текущим cargo не будет перегруза,
        и обновляет значение cargo, в ином случае выкидывает исключение CargoOverload

        Аргументы:
        - weight: вес груза для загрузки
        """
        new_cargo = self.cargo + weight

        if new_cargo <= self.max_cargo:
            self.cargo = new_cargo
        else:
            raise CargoOverload(
                f"Перегруз! Максимум: {self.max_cargo}, попытка загрузить: {new_cargo}"
            )

    def remove_all_cargo(self) -> float:
        """
        Выгрузка всего груза из самолета

        Обнуляет значение cargo и возвращает значение cargo, которое было до обнуления

        Возвращает:
        - вес выгруженного груза
        """
        removed_cargo = self.cargo
        self.cargo = 0
        return removed_cargo