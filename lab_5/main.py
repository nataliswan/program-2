import timeit
import matplotlib.pyplot as plt
from functools import lru_cache


# Реализации факториала
def fact_recursive(n: int) -> int:
    """Рекурсивный факториал"""
    if n == 0:
        return 1
    return n * fact_recursive(n - 1)


def fact_iterative(n: int) -> int:
    """Итеративный факториал"""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


@lru_cache(maxsize=None)
def fact_recursive_memo(n: int) -> int:
    """Рекурсивный факториал с мемоизацией"""
    if n == 0:
        return 1
    return n * fact_recursive_memo(n - 1)


@lru_cache(maxsize=None)
def fact_iterative_memo(n: int) -> int:
    """Итеративный факториал с мемоизацией"""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


# Бенчмарк
def benchmark(func, n, number=1000, repeat=5):
    """
    Замеряет время выполнения func(n).
    Выполняет `repeat` серий по `number` вызовов.
    Возвращает минимальное среднее время одного вызова (в секундах).
    """
    times = timeit.repeat(lambda: func(n), number=number, repeat=repeat)
    return min(times) / number


# Основная функция
def main():
    # Фиксированный набор входных данных
    test_data = list(range(10, 300, 10))

    # Списки для хранения результатов.
    res_recursive = []
    res_iterative = []
    res_recursive_memo = []
    res_iterative_memo = []

    # Замеряем время для каждого n
    for n in test_data:
        res_recursive.append(benchmark(fact_recursive, n))
        res_iterative.append(benchmark(fact_iterative, n))
        res_recursive_memo.append(benchmark(fact_recursive_memo, n))
        res_iterative_memo.append(benchmark(fact_iterative_memo, n))

    # График: сравнение мемоизованных и немемоизованных вариантов функций (рекурсивной и нерекурсивной)
    plt.plot(test_data, res_recursive, label="Рекурсивный", marker='o')
    plt.plot(test_data, res_iterative, label="Итеративный", marker='s')
    plt.plot(test_data, res_recursive_memo, label="Рекурсивный с мемоизацией", marker='x')
    plt.plot(test_data, res_iterative_memo, label="Итеративный с мемоизацией", marker='^')
    plt.title("Сравнение реализаций факториала")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()