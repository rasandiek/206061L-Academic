#Python program to demonstrate stack implementation using list

stack=[]

#append function to push data into the stack

stack.append('a')
stack.append('b')
stack.append('c')

print('Initial Stack')
print(stack)

#pop function is used to pop element from stack in LIFO order

print('\nElements popped from stack')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after popping all the elements above')
print(stack)

#Python program to demonstrate stack implementation using queue module
from queue import LifoQueue

#Initialise Stack
stack = LifoQueue(maxsize=3)

#show the number of elements in the stack
print(stack.qsize())

#put function is used to push elements into the stack
stack.put('a')
stack.put('b')
stack.put('c')

print ("Full:  ", stack.full())
print ("Size:  ", stack.qsize())


















