from collections import deque


def gen_bin_tree(height: int, root: int,
                 left_branch=lambda x: x + x / 2,
                 right_branch=lambda x: x * x) -> dict:
    """
    Генерирует бинарное дерево заданной высоты с использованием нерекурсивного подхода.
    
    Функция строит бинарное дерево, где каждый узел содержит значение и имеет двух потомков:
    левого и правого. Значения потомков вычисляются с помощью переданных функций.
    
    Аргументы:
        height (int): Высота дерева. Должна быть неотрицательной.
        root (int): Значение корневого узла дерева.
        left_branch (callable): Функция для вычисления значения левого потомка. 
                               По умолчанию: lambda x: x + x/2
        right_branch (callable): Функция для вычисления значения правого потомка.
                                По умолчанию: lambda x: x * x
    
    Возвращает:
        dict: Словарь, представляющий структуру бинарного дерева. 
              Формат: {str(value): {"left leaf": left_subtree, "right leaf": right_subtree}}
              Для листьев возвращается пустой словарь.
    """
    if height < 1:
        return {}
    
    if height == 1:
        return {str(root): {}}

    tree = {str(root): {}}
    # Используем упрощенный подход с хранением глубины
    queue = deque([(tree[str(root)], root, 1)])  # (поддерево, значение, глубина)

    while queue:
        current_node, current_val, current_depth = queue.popleft()
        
        if current_depth >= height:
            continue

        # Вычисляем значения потомков
        left_val = left_branch(current_val)
        right_val = right_branch(current_val)

        # Создаем структуру для текущего узла
        current_node.update({
            "left leaf": {str(left_val): {}},
            "right leaf": {str(right_val): {}}
        })

        # Добавляем потомков в очередь для дальнейшей обработки
        if current_depth + 1 < height:
            queue.append((current_node["left leaf"][str(left_val)], left_val, current_depth + 1))
            queue.append((current_node["right leaf"][str(right_val)], right_val, current_depth + 1))

    return tree
