'''
Jayesh Borase
Roll No. XX
BE Computer
RMDSSOE, Warje, Pune
'''

'''
Write a program to implement Huffman Encoding using a greedy strategy.
'''

import heapq   # for priority queue (min-heap)

# Step 1: Create Node class
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq          # Frequency of symbol
        self.symbol = symbol      # Character itself
        self.left = left          # Left child
        self.right = right        # Right child
        self.huff = ""            # Binary code (0 or 1)

    # To make the node work with heapq (compare using frequency)
    def __lt__(self, other):
        return self.freq < other.freq

# Step 2: Recursive function to print Huffman codes
def printNodes(node, val=""):
    newval = val + node.huff
    if node.left:
        printNodes(node.left, newval)
    if node.right:
        printNodes(node.right, newval)
    if not node.left and not node.right:  # leaf node (actual character)
        print(f"{node.symbol} -> {newval}")

# Step 3: Take user input
n = int(input("Enter number of characters: "))

chars = []
freqs = []

for i in range(n):
    c = input(f"Enter character {i+1}: ")
    f = int(input(f"Enter frequency of {c}: "))
    chars.append(c)
    freqs.append(f)

# Step 4: Create priority queue
nodes = []
for i in range(n):
    heapq.heappush(nodes, Node(freqs[i], chars[i]))

# Step 5: Build Huffman Tree using greedy method
while len(nodes) > 1:
    left = heapq.heappop(nodes)     # smallest frequency node
    right = heapq.heappop(nodes)    # next smallest
    left.huff = "0"
    right.huff = "1"
    # combine two smallest nodes into one new node
    newnode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, newnode)

# Step 6: Print Huffman Codes
print("\nHuffman Codes for characters:")
printNodes(nodes[0])
