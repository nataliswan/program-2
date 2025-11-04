import unittest
from main import gen_bin_tree

class GenBinTree(unittest.TestCase):
    def test_tree_1(self):
        self.assertEqual(gen_bin_tree(4, 8), {'8': {'left leaf': {'12.0': {'left leaf': {'18.0': {'left leaf': {'27.0': {}}, 'right leaf': {'324.0': {}}}}, 'right leaf': {'144.0': {'left leaf': {'216.0': {}}, 'right leaf': {'20736.0': {}}}}}}, 'right leaf': {'64': {'left leaf': {'96.0': {'left leaf': {'144.0': {}}, 'right leaf': {'9216.0': {}}}}, 'right leaf': {'4096': {'left leaf': {'6144.0': {}}, 'right leaf': {'16777216': {}}}}}}}})

    def test_tree_2(self):
        self.assertEqual(gen_bin_tree(4,4), {'4': {'left leaf': {'6.0': {'left leaf': {'9.0': {'left leaf': {'13.5': {}}, 'right leaf': {'81.0': {}}}}, 'right leaf': {'36.0': {'left leaf': {'54.0': {}}, 'right leaf': {'1296.0': {}}}}}}, 'right leaf': {'16': {'left leaf': {'24.0': {'left leaf': {'36.0': {}}, 'right leaf': {'576.0': {}}}}, 'right leaf': {'256': {'left leaf': {'384.0': {}}, 'right leaf': {'65536': {}}}}}}}})

    def test_tree_3(self):
        self.assertEqual(gen_bin_tree(0, 8), {})

    def test_tree_4(self):
        self.assertEqual(gen_bin_tree(1, 8), {'8': {}})

    def test_tree_5(self):
        self.assertEqual(gen_bin_tree(5, 7), {'7': {'left leaf': {'10.5': {'left leaf': {'15.75': {'left leaf': {'23.625': {'left leaf': {'35.4375': {}}, 'right leaf': {'558.140625': {}}}}, 'right leaf': {'248.0625': {'left leaf': {'372.09375': {}}, 'right leaf': {'61535.00390625': {}}}}}}, 'right leaf': {'110.25': {'left leaf': {'165.375': {'left leaf': {'248.0625': {}}, 'right leaf': {'27348.890625': {}}}}, 'right leaf': {'12155.0625': {'left leaf': {'18232.59375': {}}, 'right leaf': {'147745544.37890625': {}}}}}}}}, 'right leaf': {'49': {'left leaf': {'73.5': {'left leaf': {'110.25': {'left leaf': {'165.375': {}}, 'right leaf': {'12155.0625': {}}}}, 'right leaf': {'5402.25': {'left leaf': {'8103.375': {}}, 'right leaf': {'29184305.0625': {}}}}}}, 'right leaf': {'2401': {'left leaf': {'3601.5': {'left leaf': {'5402.25': {}}, 'right leaf': {'12970802.25': {}}}}, 'right leaf': {'5764801': {'left leaf': {'8647201.5': {}}, 'right leaf': {'33232930569601': {}}}}}}}}}})

unittest.main(argv=[''], verbosity=2, exit=False)
