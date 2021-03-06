# link : -https://practice.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1
import collections 
'''
Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


def verticalOrder(root): 
    # Base case 
    if root is None: 
        return
  
    # Create empty queue for level order traversal 
    queue = [] 
  
    # create a map to store nodes at a particular 
    # horizontal distance 
    m = {} 
  
    # map to store horizontal distance of nodes 
    hd_node = {} 
  
    # enqueue root 
    queue.append(root) 
    # store the horizontal distance of root as 0 
    hd_node[root] = 0
  
    m[0] = [root.data] 
  
    # loop will run while queue is not empty 
    while len(queue) > 0: 
  
        # dequeue node from queue 
        temp = queue.pop(0) 
  
        if temp.left: 
            # Enqueue left child 
            queue.append(temp.left) 
  
            # Store the horizontal distance of left node 
            # hd(left child) = hd(parent) -1 
            hd_node[temp.left] = hd_node[temp] - 1
            hd = hd_node[temp.left] 
  
            if m.get(hd) is None: 
                m[hd] = [] 
  
            m[hd].append(temp.left.data) 
  
        if temp.right: 
            # Enqueue right child 
            queue.append(temp.right) 
  
            # store the horizontal distance of right child 
            # hd(right child) = hd(parent) + 1 
            hd_node[temp.right] = hd_node[temp] + 1
            hd = hd_node[temp.right] 
  
            if m.get(hd) is None: 
                m[hd] = [] 
  
            m[hd].append(temp.right.data) 
  
    # Sort the map according to horizontal distance 
    a=[]
    for i in sorted(m):
        for j in m[i]:
            a.append(j)
    return a




#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None



# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        res = verticalOrder(root)
        for i in res:
            print (i, end=" ")
        print()
# recursive sol 


import collections 
'''
Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


def verticalOrder(root): 
    # Base case 
    if root is None: 
        return
  
    # Create empty queue for level order traversal 
    queue = [] 
  
    # create a map to store nodes at a particular 
    # horizontal distance 
    m = {} 
  
    # map to store horizontal distance of nodes 
    hd_node = {} 
  
    # enqueue root 
    queue.append(root) 
    # store the horizontal distance of root as 0 
    hd_node[root] = 0
  
    m[0] = [root.data] 
  
    # loop will run while queue is not empty 
    while len(queue) > 0: 
  
        # dequeue node from queue 
        temp = queue.pop(0) 
  
        if temp.left: 
            # Enqueue left child 
            queue.append(temp.left) 
  
            # Store the horizontal distance of left node 
            # hd(left child) = hd(parent) -1 
            hd_node[temp.left] = hd_node[temp] - 1
            hd = hd_node[temp.left] 
  
            if m.get(hd) is None: 
                m[hd] = [] 
  
            m[hd].append(temp.left.data) 
  
        if temp.right: 
            # Enqueue right child 
            queue.append(temp.right) 
  
            # store the horizontal distance of right child 
            # hd(right child) = hd(parent) + 1 
            hd_node[temp.right] = hd_node[temp] + 1
            hd = hd_node[temp.right] 
  
            if m.get(hd) is None: 
                m[hd] = [] 
  
            m[hd].append(temp.right.data) 
  
    # Sort the map according to horizontal distance 
    a=[]
    for i in sorted(m):
        for j in m[i]:
            a.append(j)
    return a




#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None



# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        res = verticalOrder(root)
        for i in res:
            print (i, end=" ")
        print()



# } Driver Code Ends


# } Driver Code Ends
