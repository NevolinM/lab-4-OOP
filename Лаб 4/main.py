from typing import Any


class Appliance:
    """
    Базовый класс для бытовой техники
    """

    def __init__(self, brand: str, power: int) -> None:
        """
        Инициализация базового класса бытовой техники
        :param brand: Бренд устройства
        :param power: Потребляемая мощность (Вт)
        """
        self._brand = brand  # Бренд не должен изменяться
        self.power = power

    def __str__(self) -> str:
        return f"{self._brand} (Мощность: {self.power} Вт)"

    def __repr__(self) -> str:
        return f"Appliance('{self._brand}', {self.power})"

    def turn_on(self) -> str:
        """
        Метод для включения устройства
        """
        return "Устройство включено"


class WashingMachine(Appliance):
    """
    Дочерний класс, представляющий стиральную машину
    """

    def __init__(self, brand: str, power: int, load_capacity: int) -> None:
        """
        Инициализация класса WashingMachine
        :param brand: Бренд стиральной машины
        :param power: Потребляемая мощность (Вт)
        :param load_capacity: Максимальная загрузка (кг)
        """
        super().__init__(brand, power)
        self.load_capacity = load_capacity

    def __str__(self) -> str:
        return f"{self._brand} (Мощность: {self.power} Вт, Загрузка: {self.load_capacity} кг)"

    def __repr__(self) -> str:
        return f"WashingMachine('{self._brand}', {self.power}, {self.load_capacity})"

    def turn_on(self) -> str:
        """
        Перегруженный метод включения устройства
        В отличие от базового класса, стиральная машина запускает программу стирки
        """
        return "Стиральная машина включена, программа стирки запущена"

if __name__ == "__main__":
    washer = WashingMachine("LG", 2000, 7)
    print(washer)
    print(washer.turn_on())
    pass
