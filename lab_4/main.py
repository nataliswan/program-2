from collections import deque


def gen_bin_tree(height: int = 5, root: int = 8,
                 left_leaf: callable = lambda x: x + x / 2,
                 right_leaf: callable = lambda x: x * x) -> dict:
    """
    Генерирует бинарное дерево с заданными параметрами.
    
    Эта функция строит бинарное дерево рекурсивно используя заданные параметры.
    Дерево представлено в виде вложенной структуры словарей.
    
    Аргументы:
        height (int): Высота дерева. По умолчанию 5.
        root (int): Значение корня дерева. По умолчанию 8.
        left_leaf (callable): Функция для вычисления значения левого потомка. 
            По умолчанию lambda x: x + x/2.
        right_leaf (callable): Функция для вычисления значения правого потомка.
            По умолчанию lambda x: x * x.
    
    Возвращает:
        dict: Вложенный словарь, представляющий структуру бинарного дерева.
    """
    if height < 1:
        return {}
    if height == 1:
        return {str(root): {}}

    tree = {str(root): {}}
    queue = deque([(tree, root, 1)])  # Очередь для обработки узлов по уровням

    while queue:
        subtree, val, depth = queue.popleft()
        if depth >= height:
            continue

        # Вычисляем значения ветвей используя предоставленные функции
        left_val = left_leaf(val)
        right_val = right_leaf(val)

        # Формируем структуру узла
        node_dict = {
            "left leaf": {str(left_val): {}},
            "right leaf": {str(right_val): {}}
        }
        subtree[str(val)] = node_dict

        # Добавляем ветви в очередь если не достигли последнего уровня
        if depth + 1 < height:
            queue.append((node_dict["left leaf"], left_val, depth + 1))
            queue.append((node_dict["right leaf"], right_val, depth + 1))

    return tree
