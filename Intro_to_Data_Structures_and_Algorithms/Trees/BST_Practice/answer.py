class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if self.root is None:
            self.root = Node(new_val)

        current = self.root
        while True:
            if new_val < current.value:
                if current.left is None:
                    current.left = Node(new_val)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(new_val)
                    break
                else:
                    current = current.right
        pass

    def search(self, find_val):
        current = self.root
        while True:
            if current is None:
                return False
            if current.value == find_val:
                return True
            elif find_val < current.value:
                current = current.left
            else:
                current = current.right
        return False
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))