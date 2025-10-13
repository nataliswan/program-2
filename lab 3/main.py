def gen_bin_tree(height: int, root: int) -> dict:
    if height < 1:
        return {}
    if height == 1:
        return {str(root): {}}
    return {
        str(root): {
            "left leaf": gen_bin_tree(height - 1, root + root/2),
            "right leaf": gen_bin_tree(height - 1, root * root)
        }
    }
