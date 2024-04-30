import argparse

class Node():
    #########################
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    #########################
    def __init__(self, key):
        self.value = key
        self.left_child = None
        self.right_child = None
    def __repr__(self):
        return str(self.value)

class BS_tree():
    def __init__(self):
        self.root = None

    def _inorder_recursive(self, node, output):
        if node is not None:
            self._inorder_recursive(node.left_child, output)
            output.write(f"{node.value} ")
            self._inorder_recursive(node.right_child, output)
    def inorder(self, output):      # print the in-order traversal of binary search tree
        self._inorder_recursive(self.root, output)
        output.write("\n")
    
    def _preorder_recursive(self, node, output):
        if node is not None:
            output.write(f"{node.value} ")
            self._preorder_recursive(node.left_child, output)
            self._preorder_recursive(node.right_child, output)
    def preorder(self, output):     # print the pre-order traversal of binary search tree
        self._preorder_recursive(self.root, output)
        output.write("\n")

    def _postorder_recursive(self, node, output):
        if node is not None:
            self._postorder_recursive(node.left_child, output)
            self._postorder_recursive(node.right_child, output)
            output.write(f"{node.value} ")
    def postorder(self, output):    # print the post-order traversal of binary search tree
        self._postorder_recursive(self.root, output)
        output.write("\n")

    def _find_max(self, node):
        current = node
        while current.right_child is not None:
            current = current.right_child
        return current.value
    def find_max(self, output):     # print the maximum number in binary search tree
        max_val = self._find_max(self.root)
        output.write(f"{max_val}\n")

    def _find_min(self, node):
        current = node
        while current.left_child is not None:
            current = current.left_child
        return current.value
    def find_min(self, output):     # print the minimum number in binary search tree
        min_val = self._find_min(self.root)
        output.write(f"{min_val}\n")

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        elif key < node.value:
            node.left_child = self._insert_recursive(node.left_child, key)
        else:
            node.right_child = self._insert_recursive(node.right_child, key)
        return node
    def insert(self, key):          # insert one node
        self.root = self._insert_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.value:
            node.left_child = self._delete_recursive(node.left_child, key)
        elif key > node.value:
            node.right_child = self._delete_recursive(node.right_child, key)
        else:
            if node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child
            temp_val = self._find_min(node.right_child)
            node.value = temp_val
            node.right_child = self._delete_recursive(node.right_child, temp_val)
        return node
    def delete(self, key):          # delete one node
        self.root = self._delete_recursive(self.root, key)

    def _level(self, node):
        if node is None:
            return -1
        else:
            left_height = self._level(node.left_child)
            right_height = self._level(node.right_child)
            return max(left_height, right_height) + 1
    def level(self, output):        # print the height of binary search tree(leaf = 0)
        height = self._level(self.root)
        output.write(f"{height}\n")

    def _internalnode_recursive(self, node, output):
        if node is not None:
            self._internalnode_recursive(node.left_child, output)
            if node.left_child is not None or node.right_child is not None:
                output.write(f"{node.value} ")
            self._internalnode_recursive(node.right_child, output)
    def internalnode(self, output): # print the internal node in binary search tree from the smallest to the largest 
        self._internalnode_recursive(self.root, output)
        output.write("\n")

    def _leafnode_recursive(self, node, output):
        if node is not None:
            if node.left_child is None and node.right_child is None:
                output.write(f"{node.value} ")
            self._leafnode_recursive(node.left_child, output)
            self._leafnode_recursive(node.right_child, output)
    def leafnode(self, output):     # print the leafnode in BST from left to right
        self._leafnode_recursive(self.root, output)
        output.write("\n")
    def main(self, input_path, output_path):
        #########################
        # DO NOT MODIFY CODES HERE
        # DO NOT MODIFY CODES HERE
        # DO NOT MODIFY CODES HERE
        # It's important and repeat three times
        #########################
        output = open(output_path, 'w', newline='')
        with open(input_path, 'r', newline='') as file_in:
            f = file_in.read().splitlines()
            for lines in f:
                if lines.startswith("insert"):
                    value_list = lines.split(' ')
                    for value in value_list[1:]:
                        self.insert(int(value))
                if lines.startswith('inorder'):
                    self.inorder(output)
                if lines.startswith('preorder'):
                    self.preorder(output)
                if lines.startswith('postorder'):
                    self.postorder(output)
                if lines.startswith('max'):
                    self.find_max(output)
                if lines.startswith('min'):
                    self.find_min(output)
                if lines.startswith('delete'):
                    value_list = lines.split(' ')
                    self.delete(int(value_list[1]))
                if lines.startswith('level'):
                    self.level(output)
                if lines.startswith('internalnode'):
                    self.internalnode(output)
                if lines.startswith('leafnode'):
                    self.leafnode(output)
        output.close()
if __name__ == '__main__' :
    #########################
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    #########################
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default = './input_3.txt',help="Input file root.")
    parser.add_argument("--output", type=str, default = './output_3.txt',help="Output file root.")
    args = parser.parse_args()
    
    BS = BS_tree()
    BS.main(args.input, args.output)

    