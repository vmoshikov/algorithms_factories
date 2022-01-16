from abc import ABC
from abc import abstractmethod


class AlgorithmExecution(ABC):
    """Базовое представление алгоритма поиска"""

    @abstractmethod
    def run(self, sorted_list: list, item: int):
        """Запуск алгорима"""
        pass


class LinearSearch(AlgorithmExecution):
    """Выполнение алгоритма линейного поиска"""

    def run(self, sorted_list: list, item: int):
        o = 0  # counter Operations
        i = 0

        while sorted_list[i] != item and i <= len(sorted_list):
            o += 1
            i += 1

        print(f"Выполнили алгоритм линейного поиска элемента __{item}__ среди {len(sorted_list)}"
              f"\nСкорость алгоритма O(n) / Выполнилось {o} операций")


class BinarySearch(AlgorithmExecution):
    """Выполнение алгоритма бинарного поиска"""

    def run(self, sorted_list: list, item: int):
        o = 0  # counter Operations
        low = 0
        high = len(sorted_list) - 1

        while low <= high:
            o += 1
            mid = int((low + high) / 2)
            guess = sorted_list[mid]

            if guess == item:
                print(f"Выполнили алгоритм бинарного поиска элемента __{item}__ среди {len(sorted_list)}"
                      f"\nСкорость алгоритма O(log n) / Выполнилось {o} операций")
                return True
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1

        print(f"Выполнили алгоритм бинарного поиска элемента __{item}__ среди {len(sorted_list)}"
              f"\nСкорость алгоритма O(log n) / Выполнилось {o} операций")


class AlgorithmFactory(ABC):
    """"""

    def get_algorithm_execution(self):
        pass


class FastAlgorithm(AlgorithmFactory):
    """Фабрика для выполненния быстрых алгоритмов"""

    def get_algorithm_execution(self) -> AlgorithmExecution:
        return BinarySearch()


class SlowAlgorithm(AlgorithmFactory):
    """Фабрика для выполнения медленных алгоритмов"""

    def get_algorithm_execution(self) -> AlgorithmExecution:
        return LinearSearch()


def read_factory() -> AlgorithmFactory:
    """Определяет factory на основе запроса пользователя"""

    factories = {
        "fast": FastAlgorithm(),
        "low": SlowAlgorithm()
    }

    while True:
        speed = input(f"С какой скоростью произвести поиск? Быстрый - fast / Медленный - low: ")

        if speed in factories:
            return factories[speed]

        print(f"Неизвестный параметр скорости: {speed}")


def main(fac: AlgorithmFactory, item: int):
    """"""

    data = list(range(0, 100000000, 1))

    algorithm_executor = fac.get_algorithm_execution()
    algorithm_executor.run(data, item)


if __name__ == "__main__":
    factory = read_factory()
    item = int(input("Укажите значение для поиска в списке от 10 до 100 000 000: "))

    main(factory, item)
