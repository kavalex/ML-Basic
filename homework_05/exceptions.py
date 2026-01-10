"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    """Исключение при недостаточном топливе для запуска"""
    pass


class NotEnoughFuel(Exception):
    """Исключение при недостаточном топливе для движения"""
    pass


class CargoOverload(Exception):
    """Исключение при перегрузке груза"""
    pass