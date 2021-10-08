class Node:
    def __init__(self, value):
        self.info = value
        self.link = None

class SingleLinkedList:
    def __init__(self):
        self.start = None

    def display_list(self):
        """
        For Displaying the Linked List
        """
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is: ",end = "")
            pointer = self.start
            while pointer is not None:
                print(pointer.info ,end = " ")
                pointer = pointer.link
            print()

    # def count_node(self):
    #     """
    #     for displaying the linked list

    #     """
    #     pass
    # def search(self):
    #     """
    #     for displaying the linked list

    #     """
    #     pass
    # def insert_at_beginning(self):
    #     """
    #     for displaying the linked list

    #     """
    #     pass




    def insert_at_end(self, data):
        """
        for displaying the linked list

        """
        temp = Node(data)
        if self.start == None:
            self.start = temp
            return

        pointer = self.start
        while pointer.link is not None:
            pointer = pointer.link

        pointer.link = temp

    def create_list(self):
        """
        for Creating the Linked List
        """
        length_of_list = int("Enter the Length: ")
        if length_of_list == 0:
            return
        for i in range(n):
            data = int(input("Enter the value: "))
            self.insert_at_end(data)









    # def insert_after(self):
    #     """
    #     for displaying the linked list

    #     """
    #     pass
    # def insert_before(self):
    #     """
    #     for displaying the linked list

    #     """
    #     pass
    # def insert_at_position(self):
    #     """
    #     for displaying the linked list

    #     """
    #     pass
    # def delete_node(self):
    #     """
    #     for displaying the linked list

    #     """
    #     pass
    # def delete_first_node(self):
    #     """
    #     for displaying the linked list

    #     """
    #     pass
    # def delete_last_node(self):
    #     """
    #     for displaying the linked list

    #     """
    #     pass
    # def display_list(self):
    #     """
    #     for displaying the linked list

    #     """
    #     pass
    # def display_list(self):
    #     """
    #     for displaying the linked list

    #     """
    #     pass




list1 = SingleLinkedList()
list1.insert_at_end(4)
list1.insert_at_end(3)
list1.insert_at_end(2)
