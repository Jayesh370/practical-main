import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # comparison for priority queue (min-heap)
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build Huffman Tree
def build_huffman_tree(char_freq):
    heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        heapq.heappush(heap, new_node)

    return heap[0]  # Root node

# Generate Huffman Codes (Recursive Traversal)
def generate_codes(node, code="", huffman_codes={}):
    if node is None:
        return
    if node.char is not None:
        huffman_codes[node.char] = code
    generate_codes(node.left, code + "0", huffman_codes)
    generate_codes(node.right, code + "1", huffman_codes)
    return huffman_codes

# Example input
text = "DAA PRACTICAL"
print("Original Text:", text)

# Step 1: Count frequency of each character
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1

print("\nCharacter Frequencies:")
for k, v in freq.items():
    print(f"{k}: {v}")

# Step 2: Build Huffman Tree
root = build_huffman_tree(freq)

# Step 3: Generate Huffman Codes
codes = generate_codes(root)
print("\nHuffman Codes:")
for char, code in codes.items():
    print(f"{char}: {code}")

# Step 4: Encode the text
encoded_text = ''.join([codes[char] for char in text])
print("\nEncoded Text:", encoded_text)

# Step 5: Decode (optional)
def decode(encoded_text, root):
    decoded = ""
    node = root
    for bit in encoded_text:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            decoded += node.char
            node = root
    return decoded

decoded_text = decode(encoded_text, root)
print("\nDecoded Text:", decoded_text)

