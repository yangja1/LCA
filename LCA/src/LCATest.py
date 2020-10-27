import unittest
import binaryLCA


# inherited Node from binaryLCA to avoid typing binaryLCA again and again. Additionally it was an excuse to practice inheritance.
class Node(binaryLCA.Node):
    def __init__(self, value):
        super().__init__(value)


class TestLCA(unittest.TestCase):

    def test_BasicTree(self):
        #print("Test1: Test Basic Tree:")
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        # visualising the data

        #print(root)

        self.assertEqual(3, binaryLCA.findLCA(root, 6, 7), "3 should be the lowest common ancestor of 6 and 7")

    def test_EmptyTree(self):
        #print("Test2: Test Empty Tree:")
        root = None
        self.assertEqual(-1, binaryLCA.findLCA(root, 6, 7), " The output should be -1 since the tree is empty")

    def test_BothNodesNotPresent(self):
        #print("Test3: testBothNodesNotPresent:")
        root = Node(1)
        self.assertEqual(-1, binaryLCA.findLCA(root, 6, 7), " The output should be -1 both nodes are missing")

    def test_OneNodeNotPresent(self):
        #print("Test4: testOneNodeNotPresent:")
        root = Node(1)
        root.left = Node(6)
        self.assertEqual(-1, binaryLCA.findLCA(root, 6, 7), " The output should -1 since one of the nodes is missing")

    def test_CommonAncestorIsTarg(self):
        #print("Test5: commonAncestorIsTarget")
        root = Node(1)
        root.left = Node(3)
        root.right = Node(5)
        root.left.left = Node(6)
        root.left.right = Node(8)

        self.assertEqual(1, binaryLCA.findLCA(root, 1, 3),
                         "The output should be 1 since it is both the ancestor node and the target node")
        self.assertEqual(1, binaryLCA.findLCA(root, 1, 5),
                         "The output should be 1 since it is both the ancestor node and the target node")
        self.assertEqual(3, binaryLCA.findLCA(root, 3, 6),
                         "The output should be 3 since it is both the ancestor node and the target node")
        self.assertEqual(3, binaryLCA.findLCA(root, 3, 8),
                         "The output should be 3 since it is both the ancestor node and the target node")


    def test_Single(self):
        # print("Test9: testSingle")
        root = Node(1)

        assert binaryLCA.findLCA(root, 1, 1) == 1, \
            "Should be 1 but got: " + str(binaryLCA.findLCA(root, 1, 1))

    def test_CharsInNumberTree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(31)
        root.left.left = Node(4)
        root.left.right = Node(10)
        root.right.left = Node(16)
        root.right.right = Node(7)
        root.left.left.left = Node(24)

        self.assertEqual(-1, binaryLCA.findLCA(root, 'a', 'b'),
                         "Should be -1 but got: " + str(binaryLCA.findLCA(root, 'a', 'b')))

    def test_CharsInCharTree(self):
        root = Node('a')
        root.left = Node('b')
        root.right = Node('c')
        root.left.left = Node('d')
        root.left.right = Node('e')
        root.right.left = Node('f')
        root.right.right = Node('g')
        root.left.left.left = Node('h')

        self.assertEqual('b', binaryLCA.findLCA(root, 'd', 'e'),
                         "Should be b but got: " + str(binaryLCA.findLCA(root, 'd', 'e')))

if __name__ == '__main__':
    unittest.main()
