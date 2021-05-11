from collections import deque
class Node:
    def __init__(self, value):
        self.info = value
        self.right = None
        self.left = None

class binary_tree:
    def __init__(self):
        self.info = None

    def is_empty(self):
        return self.root == None
    
    
    def display(self):
        self._display(self.root,0) # this is private recursive method
        print()
    
    def _display(self, p , level):
        if p == None:
            return
        self._display(p.left, level+1)
        print()

        for _ in range(level):
            print("     ",end="")
        print(p.info)
        self._display(p.right, level+1)




    

    
    def create_tree(self):
        self.root = Node("p")
        self.root.left = Node("q")
        self.root.right = Node("r")
        
        self.root.left.left = Node("s")
        self.root.left.right = Node("t")
        self.root.right.left = Node("u")
        self.root.right.right = Node("v") 



binary_tree1 = binary_tree()
binary_tree1.create_tree()


binary_tree1.display()