from typing import Callable, Dict, Any


def gen_bin_tree(
        height: int,
        root: float,
        left_leaf: Callable[[float], float] = lambda x: x + x / 2,
        right_leaf: Callable[[float], float] = lambda x: x * x
) -> Dict[str, Any]:
    """
    Рекурсивно строит бинарное дерево заданной высоты с указанным корневым значением.

    Каждый узел дерева представлен в виде словаря со следующими ключами:
    - 'value': значение в текущем узле,
    - 'left': левое поддерево (или None, если достигнута максимальная глубина),
    - 'right': правое поддерево (или None, если достигнута максимальная глубина).

    Значения левого и правого потомков вычисляются с помощью переданных функций
    left_leaf и right_leaf. По умолчанию используются формулы из варианта №8:
    левый потомок = root + root / 2, правый потомок = root ^ 2.

    Аргументы:
        height (int): Высота дерева. Должна быть неотрицательным целым числом.
        root (float): Значение в корне дерева.
        left_leaf (Callable[[float], float]): Функция для вычисления левого потомка.
        right_leaf (Callable[[float], float]): Функция для вычисления правого потомка.

    Возвращает:
        Dict[str, Any]: Словарь, представляющий бинарное дерево.
    """
    if height <= 0:
        return {}
    if height == 1:
        return {"value": root, "left": None, "right": None}

    return {
        "value": root,
        "left": gen_bin_tree(height - 1, left_leaf(root), left_leaf, right_leaf),
        "right": gen_bin_tree(height - 1, right_leaf(root), left_leaf, right_leaf)
    }
