'''
Basic Operations:
Enqueue
Dequeue
isEmpty
isFull
peek
'''

# Object Oriented Programming

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueu(self, element):
        self.queue.append(element)
    
    def isEmpty(self):
        return len(self.queue) == 0

    def deque(self):
        if(self.isEmpty()):
            print("Queue is empty")
            return None
        return self.queue.pop(0)
    
    def display(self):
        print(self.queue)

objQueue = Queue()
objQueue.enqueu(1)
objQueue.deque()
objQueue.enqueu(2)
objQueue.enqueu(3)
objQueue.enqueu(4)
objQueue.enqueu(1)
objQueue.enqueu(5)
objQueue.deque()
objQueue.deque()
objQueue.display()