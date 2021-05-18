from collections import deque

class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None
        


class binary_search_tree: 

    def __init__(self):
        self.info = None

    def empty(self):
        return self.root == None


     def insert(self, x):
         self.root = self._insert(self.root, x)

    def _insert(self, p, x):
        if p is None:
            p = Node(x)
        elif x < p.info:
            p.left = self._insert(.left, x)
        elif x > p.info :
            p.right = self._insert(.left, x)
        else:
            print(x, "already present ")
        return p

    def insert1(self, x):
        p = self.root
        par = None
        while p is not None:
            par = p
            if x < p.info:
                p = p.left 
            elif x > p.info:
                p = p.right
            else:
                print(x + "already in the tree")
                return 
            temp = Node(x)

            if par == None:
                self.root = temp 
            elif x < par.info:
                p = p.right 
            else:
                par.right = temp

        def search(self, x):
            return self._search(self.rooot, x)

        def _search(self, p, x):
            if p is None:
                return None
            if x < p.info:
                return self._search(p.left, x)
            if x > p.info:
                return self._search(p.right, x)
            return p

        
        def search1(self, x):
            p = self.root
            while p is not None:
                if x<p.info:
                    p = p.left
                elif x>p.info:
                    p= p.right
                else:
                    return True
            return False

        def delete(self, x):
            self.root = self._delete(self.root, x)

         



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


bst = binary_Serach_tree()
bst.create_tree()
bst.display()
bst.preorder()
bst.inorder()
bst.postorder()
print(bst.height())
bst.level_order()
