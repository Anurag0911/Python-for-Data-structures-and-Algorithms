from collections import deque

class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None
        


class binary_tree: 

    def __init__(self):
        self.info = None

    def empty(self):
        return self.root == None

    def create_tree(self):
        self.root = Node("p")

        self.root.left = Node("q")
        self.root.left.left = Node("s")
        self.root.left.right = Node("t")


        self.root.right = Node("r")
        self.root.right.left = Node("u")
        self.root.right.right = Node("v") 
    
    def display(self):
        self._display(self.root,0) # this is private recursive method
        print()
    
    def _display(self, p , level):
        if p == None:
            return
        self._display(p.right, level+1)
        print()
        for _ in range(level):
            print("     ",end="")
        print(p.info)
        self._display(p.left, level+1)



# lets us try the Preorder traversal 
    def preorder(self):
        print("This is the preorder traversal: ", end="")
        self._preorder(self.root)
        print()
    
    def _preorder(self, p):
        if p == None:
            return 
        print(p.info, end="   ")
        self._preorder(p.left)
        self._preorder(p.right)

# lets us try the Inorder traversal 
    def inorder(self):
        print("This is the inorder traversal: ", end="")
        self._inorder(self.root)
        print()
    
    def _inorder(self, p):
        if p == None:
            return 
        self._inorder(p.left)
        print(p.info, end="   ")
        self._inorder(p.right)

# lets us try the Inorder traversal 
    def postorder(self):
        print("This is the postorder traversal: ", end="")
        self._postorder(self.root)
        print()
    
    def _postorder(self, p):
        if p == None:
            return 
        self._postorder(p.left)
        self._postorder(p.right)
        print(p.info, end="   ")
    
    def level_order(self):
        if self.root == None:
            return 
        
        q = deque()
        q.append(self.root)
        

        while len(q)!=0:
            p = q.popleft()
            print(p.info + "",end = "")
            if p.left is not None:
                q.append(p.left)
                
            if p.right is not None:
                q.append(p.right)
                

    def height(self):
        
        return self._height(self.root)
    
    def _height(self, p):
        if p is None:
            return 0
        Hleft = self._height(p.left)
        Hright = self._height(p.right)
        if Hleft > Hright:
                return 1 + Hleft
        else:
                return 1 + Hright


binary_tree1 = binary_tree()
binary_tree1.create_tree()
binary_tree1.display()
binary_tree1.preorder()
binary_tree1.inorder()
binary_tree1.postorder()
print(binary_tree1.height())
binary_tree1.level_order()
