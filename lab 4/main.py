from collections import deque

def gen_bin_tree(height: int, root: int,
                 left_branch=lambda x: x + x / 2,
                 right_branch=lambda x: x * x) -> dict:
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

        # Вычисляем значения ветвей
        left_val = left_branch(val)
        right_val = right_branch(val)

        # Формируем структуру узла
        node_dict = {
            "left leaf": {str(left_val): {}},
            "right leaf": {str(right_val): {}}
        }
        subtree[str(val)] = node_dict

        # Добавляем ветви в очередь, если не достигли последнего уровня
        if depth + 1 < height:
            queue.append((node_dict["left leaf"], left_val, depth + 1))
            queue.append((node_dict["right leaf"], right_val, depth + 1))

    return tree
