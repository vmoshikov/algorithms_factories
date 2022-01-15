from abc import ABC, abstractmethod


class AlgorithmExecution(ABC):
    """Базовое представление алгоритма поиска"""

    @abstractmethod
    def run(self, data: list, item: int):
        """Запуск алгорима"""
        pass


class LinearSearch(AlgorithmExecution):
    """Выполнение алгоритма линейного поиска"""

    def run(self, data: list, item: int):
        print(f"Выполняем алгоритм линейного поиска элемента __{item}__ среди {len(data)}"
              f"\nСкорость алгоритма O(n)")


class BinarySearch(AlgorithmExecution):
    """Выполнение алгоритма бинарного поиска"""

    def run(self, data: list, item: int):
        print(f"Выполняем алгоритм бинарного поиска элемента __{item}__ среди {len(data)}"
              f"\nСкорость алгоритма O(log n)")


if __name__ == "__main__":
    """"""

    item = int(input("Укажите значение для поиска в списке от 10 до 100 000 000: "))
    LinearSearch().run(list(range(0, 100000000, 1)), item)
