import unittest
from main import gen_bin_tree

class GenBinTree(unittest.TestCase):
    def test_tree_1(self):
        self.assertEqual(gen_bin_tree(4, 8), {'value': 8, 'left': {'value': 12.0, 'left': {'value': 18.0, 'left': {'value': 27.0, 'left': None, 'right': None}, 'right': {'value': 324.0, 'left': None, 'right': None}}, 'right': {'value': 144.0, 'left': {'value': 216.0, 'left': None, 'right': None}, 'right': {'value': 20736.0, 'left': None, 'right': None}}}, 'right': {'value': 64, 'left': {'value': 96.0, 'left': {'value': 144.0, 'left': None, 'right': None}, 'right': {'value': 9216.0, 'left': None, 'right': None}}, 'right': {'value': 4096, 'left': {'value': 6144.0, 'left': None, 'right': None}, 'right': {'value': 16777216, 'left': None, 'right': None}}}})

    def test_tree_2(self):
        self.assertEqual(gen_bin_tree(4, 4), {'value': 4, 'left': {'value': 6.0, 'left': {'value': 9.0, 'left': {'value': 13.5, 'left': None, 'right': None}, 'right': {'value': 81.0, 'left': None, 'right': None}}, 'right': {'value': 36.0, 'left': {'value': 54.0, 'left': None, 'right': None}, 'right': {'value': 1296.0, 'left': None, 'right': None}}}, 'right': {'value': 16, 'left': {'value': 24.0, 'left': {'value': 36.0, 'left': None, 'right': None}, 'right': {'value': 576.0, 'left': None, 'right': None}}, 'right': {'value': 256, 'left': {'value': 384.0, 'left': None, 'right': None}, 'right': {'value': 65536, 'left': None, 'right': None}}}})

    def test_tree_3(self):
        self.assertEqual(gen_bin_tree(0, 8), {})

    def test_tree_4(self):
        self.assertEqual(gen_bin_tree(1, 8), {'value': 8, 'left': None, 'right': None})

    def test_tree_5(self):
        self.assertEqual(gen_bin_tree(5, 7), {'value': 7, 'left': {'value': 10.5, 'left': {'value': 15.75, 'left': {'value': 23.625, 'left': {'value': 35.4375, 'left': None, 'right': None}, 'right': {'value': 558.140625, 'left': None, 'right': None}}, 'right': {'value': 248.0625, 'left': {'value': 372.09375, 'left': None, 'right': None}, 'right': {'value': 61535.00390625, 'left': None, 'right': None}}}, 'right': {'value': 110.25, 'left': {'value': 165.375, 'left': {'value': 248.0625, 'left': None, 'right': None}, 'right': {'value': 27348.890625, 'left': None, 'right': None}}, 'right': {'value': 12155.0625, 'left': {'value': 18232.59375, 'left': None, 'right': None}, 'right': {'value': 147745544.37890625, 'left': None, 'right': None}}}}, 'right': {'value': 49, 'left': {'value': 73.5, 'left': {'value': 110.25, 'left': {'value': 165.375, 'left': None, 'right': None}, 'right': {'value': 12155.0625, 'left': None, 'right': None}}, 'right': {'value': 5402.25, 'left': {'value': 8103.375, 'left': None, 'right': None}, 'right': {'value': 29184305.0625, 'left': None, 'right': None}}}, 'right': {'value': 2401, 'left': {'value': 3601.5, 'left': {'value': 5402.25, 'left': None, 'right': None}, 'right': {'value': 12970802.25, 'left': None, 'right': None}}, 'right': {'value': 5764801, 'left': {'value': 8647201.5, 'left': None, 'right': None}, 'right': {'value': 33232930569601, 'left': None, 'right': None}}}}})
        
unittest.main(argv=[''], verbosity=2, exit=False)
