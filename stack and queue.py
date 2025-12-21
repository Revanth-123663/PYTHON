stack = []
print(stack)
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)
stack.pop()
print(stack)
stack.pop(1)
print(stack)
if stack == 3 or stack == 1:
    print("True")
else:
    print("False")
    
# We use dynamic arrays for stacks

from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft()
A = queue[1]
B = queue[-1]

print(queue)
print(A)
print(B)
