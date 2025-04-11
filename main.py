class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Recursively insert a value into the binary search tree"""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        """Search for a value in the binary search tree"""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
    def inorder_traversal(self):
        """Perform inorder traversal of the binary tree"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        """Perform preorder traversal of the binary tree"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        """Perform postorder traversal of the binary tree"""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)
    
    def find_height(self):
        """Find the height of the binary tree"""
        return self._find_height_recursive(self.root)
    
    def _find_height_recursive(self, node):
        if node is None:
            return -1
        
        left_height = self._find_height_recursive(node.left)
        right_height = self._find_height_recursive(node.right)
        
        return max(left_height, right_height) + 1

# Example usage
if __name__ == "__main__":
    # Create a binary search tree
    bst = BinaryTree()
    
    # Insert some values
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        bst.insert(value)
    
    # Demonstrate different traversals
    print("Inorder traversal:", bst.inorder_traversal())    # Expected: [2, 3, 4, 5, 6, 7, 8]
    print("Preorder traversal:", bst.preorder_traversal())  # Expected: [5, 3, 2, 4, 7, 6, 8]
    print("Postorder traversal:", bst.postorder_traversal())# Expected: [2, 4, 3, 6, 8, 7, 5]
    
    # Search for values
    print("\nSearching for values:")
    for value in [4, 9]:
        node = bst.search(value)
        if node:
            print(f"Found value {value} in the tree")
        else:
            print(f"Value {value} not found in the tree")
    
    # Get tree height
    print("\nTree height:", bst.find_height())  # Expected: 2