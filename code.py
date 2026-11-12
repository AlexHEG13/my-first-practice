"""Проверка расположения букв в массивах в алфавитном порядке."""
from typing import Iterable

MAX_SIZE = 100  # максимально допустимое число элементов массива


def is_alphabetical(*elements: str) -> bool:
    """Определяет, упорядочены ли переданные элементы по алфавиту.

    Процедуре передаются ВСЕ элементы рассматриваемого массива
    (через *elements). Пустой массив и массив из одного элемента
    считаются упорядоченными тривиально.
    """
    if len(elements) > MAX_SIZE:
        raise ValueError(f"Размер массива превышает {MAX_SIZE} элементов")
    normalized = [el.lower() for el in elements]  # сравнение без учёта регистра
    return all(normalized[i] <= normalized[i + 1]
               for i in range(len(normalized) - 1))


def check_array(number: int, *elements: str) -> None:
    """Выводит результат проверки одного массива по условию задачи."""
    if is_alphabetical(*elements):
        print(f"Массив №{number}: буквы расположены в алфавитном порядке")
    else:
        print(f"Массив №{number}: -1")


if __name__ == "__main__":
    array1 = ['a', 'c', 'f', 'f', 'k']
    array2 = ['p', 'r', 't', 'b', 'w']
    for i, arr in enumerate((array1, array2), start=1):
        check_array(i, *arr)

