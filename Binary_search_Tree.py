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
            p.left = self._insert(p.left, x)
        elif x > p.info :
            p.right = self._insert(p.left, x)
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


        def _delete(self,p,x):
            if p is None:
                print(x, " this element is not found")
                return p


            if x < p.info:
                p.left = self._delete(p.left, x)
            elif x > p.info:
                p.left = self._delete(p.right, x)
            else:
                if p.left is not None and p.right is not None:
                    s= p.right
                    while s.left is not None:
                        s= s.left
                    p.info = s.info

                    p.right = self._delete(p.right,s.info)

                else:
                    if p.left is not None:
                        ch = p.left 
                    else:
                        ch = p.right
                    p = ch
            return p

        def delete1(self, x):
            p = self.root
            par = None
            while p is not None:
                if x== p.info:
                    break
                par = p 
                if x< p.info:
                    p = p.left
                else:
                    p = p.right
                if p == None:
                    print(x, "not found")
                
                # Case c: 2 children 
                #find inorder success and its parent 

                if p.left is not None and p.right is not None:
                    ps = p 
                    s = p.right 

                    while s.left is not None:
                        ps = p
                        s = s.left

                    p.info = s.info
                    p = s
                    par = ps

                    #case B and Case A : 1 or no child
                    if p.left is not None : # node to be deleted has left child 
                        ch = p.left 

                    else:   # node that has to be deleted has a right chilf pt no child
                        ch = p.right 



                    if par == none : # node to be deleted is self.root 
                        self.root = ch
                    elif p == par.left: # node is left child of the parent 
                        par.left = ch 
                    else: # node is orght child of its parent 

                        par.right = ch 



        def min1(self):
            if self.empty():
                raise TreeEmtyEroor("Tree is Empty")
            p = self.root
            while p.left is not None:
                p = p.left 
            return p.info


                
        def max1(self):
            if self.empty():
                raise TreeEmptyError("tress is empty"):
            p = self.root
            while p.right is not None:
                p = p.right
            return p.info 


        def min2(self):
            if self.empty():
                raise TreeEmptyError("tress is empty")
            return self._min(self.root).info
        
        def _min(self,p):
            if p.left is None:
                return p

            return self._min(p.left)

        def max2(self):
            if self.empty():
                raise TreeEmptyError("tress is empty")
            return self._max(self.root).info
        def _max(self):
            if p.right is None:
                return p
            return self._max(p.right)





    
         



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
