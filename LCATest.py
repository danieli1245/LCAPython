from unittest import TestCase
from LCA import Node, findLCA, findPath


class LCATest(TestCase):

    def test_EmptyRoot(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        self.assertEqual(findLCA(root, 8, 4), -1, "LCA of 8 and 4 is ")


    def test_LCATest(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.right.right = Node(8)
        self.assertEqual(findLCA(root, 8, 4), 2, "LCA of 8 and 4 is ")
        self.assertEqual(findLCA(root, 0, 1), -1, "LCA of 0 and 1 is ")

    def test_LLLCATest(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.left.left.right = Node(6)
        root.left.left.left = Node(7)
        root.left.right.right = Node(8)
        self.assertEqual(findLCA(root, 8, 1), 1, "LCA of 8 and 1 is ")
        self.assertEqual(findLCA(root, 7, 3), 1, "LCA of 7 and 3 is ")
        self.assertEqual(findLCA(root, 0, 1), -1, "LCA of 0 and 1 is ")