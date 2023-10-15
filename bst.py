class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):

        if self.left is not None:
            self.left.in_order_traversal()

        print(self.data)

        if self.right is not None:
            self.right.in_order_traversal()

    def search(self, value):

        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        if value > self.data:
            if self.right:
                return self.right.search(value)

            else:
                return False

    def build_tree(elements):
        val = BinarySearchTreeNode(elements[0])

        for i in range(1, len(elements)):
            val.insert(elements[i])

        return (val)


# Insert elements to binary search tree
val = BinarySearchTreeNode(20)
val.insert(40)
val.insert(10)
val.insert(4)
val.insert(15)
val.insert(50)
val.insert(35)
val.insert(55)
val.insert(60)

# In Order Traversal the binary tree
val.in_order_traversal()

# search for the values 15 and 52 in tree
print(val.search(15))
print(val.search(52))
