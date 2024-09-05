from Node import Node

class My_LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

    # def printList(self):
    #     if self.head == self.tail:
    #         print(self.head.value)
    #     else:
    #         new_node = self.head
    #         while new_node.next is not None:
    #             print(new_node.value)
    #             new_node = new_node.next 



