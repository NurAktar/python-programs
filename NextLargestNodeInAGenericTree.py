from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def nextLargestUtil(root, x):
    global res
    if root is None:
        return
    if root.data > x:
        if ((res == None or res.data > root.data)):
            res = root
    countChildren = len(root.children)
    for i in range(countChildren):
        nextLargestUtil(root.children[i], x)
    return
def nextLargest(root, n):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    global res
    res = None
    nextLargestUtil(root, n)
    return res



def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in stdin.readline().strip().split())
n = int(input())
tree = createLevelWiseTree(arr)
if nextLargest(tree, n):
    print(nextLargest(tree, n).data)
