from Trees import Node


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        current: Node = self.root
        while True:
            if new_val <= current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(new_val)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(new_val)
                    break

    def search(self, find_val):
        current = self.root
        while current:
            if find_val > current.value:
                current = current.right
            elif find_val < current.value:
                current = current.left
            else:
                return True
        return False


if __name__ == '__main__':
    tree = BST(4)

    # Insert elements
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)

    print(tree.search(4))
    print(tree.search(6))
