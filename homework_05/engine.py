"""
Создайте dataclass `Engine`
"""

from dataclasses import dataclass

@dataclass
class Engine:
    """
    Датакласс, представляющий двигатель

    Атрибуты:
    - volume: объем двигателя
    - pistons: количество поршней
    """
    volume: float
    pistons: int