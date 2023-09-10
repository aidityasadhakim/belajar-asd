class Node:
    # Creating a node
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    linked_list = LinkedList()
    first = Node(3)
    linked_list.head = first
    second = Node(5)
    third = Node(8)
    fourth = Node(80)

    # connect the nodes
    linked_list.head.next = second
    second.next = third 
    third.next = fourth

    while (linked_list.head != None):
        print(linked_list.head.data, end=" ")
        linked_list.head = linked_list.head.next
