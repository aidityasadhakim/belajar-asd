'''
Traversal
Insertion
Deletion
Search
Sort
'''

# fourth
# new_node(head) -> first -> new_node -> second -> None
# 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("Node sebelumnya harus ada di LinkedList")
            return

        new_node = Node(new_data) # new_node
        new_node.next = prev_node.next 
        prev_node.next = new_node
    
    def deleteNode(self, position):
        if self.head == None:
            return
        
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break
        
        if temp is None:
            return
        
        if temp.next is None:
            return
        
        next = temp.next.next

        temp.next = None

        temp.next = next

    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insertAtBeginning(3)
    linked_list.insertAtBeginning(5)
    linked_list.insertAtBeginning(8)
    linked_list.deleteNode(1)

    linked_list.printList()