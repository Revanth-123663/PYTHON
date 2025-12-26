A = [6,-2,0,-5,7,56,45,-90]
import heapq
heapq.heapify(A)
print(A)

heapq.heappush(A, 4)
print(A)

minn = heapq.heappop(A)

print(A, minn)

def heapsort(arr):
  heapq.heapify(arr)
  n = len(arr)
  new_list = [0] * n

  for i in range(n):
    minn = heapq.heappop(arr)
    new_list[i] = minn

  return new_list

print(heapsort(A))

push_pop=heapq.heappushpop(A, 99)
print(push_pop)

B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(B)

for i in range(n):
  B[i] = -B[i]

heapq.heapify(B)

print(B)

largest = -heapq.heappop(B)

print(largest)

heapq.heappush(B, -7) # Insert 7 into max heap

print(B)

for i in range(n):
  B[i] = -B[i]
  
print(B)
