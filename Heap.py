class HeapEmptyError(Exception):
    pass

class Heap:
    def __init__(self, maxSize):
        self.a = [None] * maxSize
        self.n = 0 #size of th the array
        self.a[0] = 99999

    def insert(self, value):
       self.n+=1 #increase the size by one 
       self.a[self.n] = value
       self.restore_up(self.n)

    def restore_up(self, i):
        k = self.a[i]
        iparent = i//2

        while self.a[iparent] < k:
            self.a[i] = self.a[iparent]
            i = [iparent]
            iparent = i//2
        self.a[i]=k

    def delete_root(self):
        if self.n == 0:
            raise HeapEmptyError("Heap is empty")

        maxValue = self.a[1]
        self.a[1] = self.a[self.n]
        self.n -= 1
        self.restore_down(1) # assuming the root child is violationg
        return maxValue

    def restore_down(self, i):
        k = self.a[i]
        lchild = 2*i
        rchild = lchild + 1

        while rchild <= self.n:
            if k >= self.a[lchild] and k>=self.a[rchild]:
                self.a[i] = self.a[lchild]
                i = lchild
            else:
                self.a[i] = self.a[rchild]
            lchild = 2*i

            rchild = lchild + 1


        if lchild == self.n and k< self.a[lchild]:
            self.a[i] = self.a[lchild]
            i=lchild
        self.a[i] =k


    def display(self):
        if self.n == 0:
            print("heap is empty")
            return
        
        print("heap size = ",self.n)
        for i in range(q,self.n+1):
            print(self.a[i],end ="     ")
        print()



        


h = Heap(20)
while True:
    print("1 Insert")
    print("2 delete root")
    print("display")
    print("4 exite")
    print("choice:")
    choice = int(input("enter choice"))

    if choice==1:
        value = int(input("enter value"))
        h.insert(value)
    elif choice==2:
    
        print("max valaue", h.delete_root())
    elif choice==3:
        h.display()
    elif choice==4:
        break
    else:
        print("wrong choice") 
