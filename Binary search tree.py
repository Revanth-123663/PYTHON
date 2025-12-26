#        1
#     2    3
#   4  5  10

# DFS

class Treenode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
        
    def __str__(self):
        return str(self.val)
        
        A = TreeNode(1)
        B = TreeNode(2)
        C = TreeNode(3)
        D = TreeNode(4)
        E = TreeNode(5)
        F = TreeNode(10)

        A.left = B
        A.right = C
        B.left = D
        B.right = E
        C.left = F
        
        print("A")
        
        def pre_order(node):
            if not node:
                return
            
            print(node)
            pre_order(node.left)
            pre_order(node.right)

        print(pre_order(A))
        
        def in_order(node):
            if not node:
                return

            in_order(node.left)
            print(node)
            in_order(node.right)

        print(in_order(A))

# BFS
        from collections import deque

        def level_order(node):
            q = deque()
            q.append(node)

            while q:
                node = q.popleft()
                print(node)
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)

        level_order(A)
