import sys
sys.setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

#main
def heightOfTree(root):
    height = 0
    for child in root.children:
        ch = heightOfTree(child)
        height = max(ch, height)
    height += 1
    return height
## Read input as specified in the question.
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
## Print output as specified in the question.
arr = list(int(x) for x in sys.stdin.readline().rstrip().rsplit())
root = createLevelWiseTree(arr)
print(heightOfTree(root))
