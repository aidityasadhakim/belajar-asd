'''
Basic Operations:
- Push
- Pop
- isEmpty
- isFull
- peek
'''

stack = []

def isEmpty(stack):
    return (len(stack) == 0)

def push(stack, element):
    stack.append(element)
    print("Pushed element: ", element)

def pop(stack):
    if(isEmpty(stack)):
        print("Stack is empty")
        return "Stack is empty"
    
    return stack.pop()

# Buat fungsi untuk peek the top of the stack
def peek(stack):
    return stack[-1]

push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))
pop(stack)
print(peek(stack)) # Should return 4
print("Stack after popped: " + str(stack))