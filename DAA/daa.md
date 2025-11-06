🧠 Line-by-Line Explanation

Step 1 – Import heapq

import heapq
	• Imports heapq, a module that helps maintain a min-heap (priority queue).
	• Used to always pick the two smallest frequency characters first — that’s the greedy strategy.

Step 2 – Define Node class

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""
	• Each Node represents either:
		○ a leaf node → single character, or
		○ an internal node → combination of two smaller nodes.
	• freq – frequency (number of occurrences)
	• symbol – character name (like "a" or "b")
	• left, right – children (used to form the tree)
	• huff – code assigned ("0" or "1")

def __lt__(self, other):
    return self.freq < other.freq
	• Allows comparison of two nodes by frequency (needed for heapq to work).
	• Ensures smallest frequency node gets higher priority.

Step 3 – Recursive print function

def printNodes(node, val=""):
    newval = val + node.huff
	• val stores the Huffman code accumulated so far.
	• When we go left, we add "0", when we go right, we add "1".

    if node.left:
        printNodes(node.left, newval)
    if node.right:
        printNodes(node.right, newval)
	• Recursively travels the entire Huffman tree.

    if not node.left and not node.right:
        print(f"{node.symbol} -> {newval}")
	• When there’s no left and right, it’s a leaf node → print the final Huffman code for that symbol.

Step 4 – Take user input

n = int(input("Enter number of characters: "))
	• User tells how many unique characters there are.
Then we take each character and its frequency:

for i in range(n):
    c = input(f"Enter character {i+1}: ")
    f = int(input(f"Enter frequency of {c}: "))
    chars.append(c)
    freqs.append(f)

Step 5 – Create priority queue

nodes = []
for i in range(n):
    heapq.heappush(nodes, Node(freqs[i], chars[i]))
	• Pushes each node into a heap.
	• Heap always keeps smallest frequency on top.

Step 6 – Build Huffman Tree (Main Greedy Logic)

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
	• Pops the two smallest frequency nodes.

    left.huff = "0"
    right.huff = "1"
	• Assigns binary codes: 0 for left, 1 for right.

    newnode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
	• Combines two nodes into a new one with:
		○ frequency = sum of both
		○ symbol = combination of both characters

    heapq.heappush(nodes, newnode)
	• Pushes this new combined node back into the heap.
The loop continues until there’s only one node left → the root of Huffman Tree.

Step 7 – Print Huffman Codes

print("\nHuffman Codes for characters:")
printNodes(nodes[0])
	• Calls the recursive function to print all character codes.

🧠 Theory Recap (For Viva)
Concept	Explanation
Huffman Encoding	Compression algorithm using variable-length binary codes.
Greedy Strategy	Always combine two smallest frequencies first.
Heap (Priority Queue)	Helps pick smallest elements efficiently.
Tree Structure	Each leaf represents a character; internal nodes store frequency sums.
Prefix Property	No code is the prefix of another → ensures lossless decoding.
Time Complexity	O(n log n).
Space Complexity	O(n).

🎤 Common Viva Questions (and Answers)
Question	Answer
What is Huffman Encoding?	A greedy algorithm used for data compression.
Why greedy?	It picks the smallest two frequencies at every step.
What data structure is used?	A min-heap (priority queue).
What is the output of the algorithm?	Unique binary code for each character.
What is the prefix property?	No code is the prefix of another, ensuring safe decoding.
What are the leaf and internal nodes?	Leaf → actual character; Internal → combined frequencies.
Time complexity?	O(n log n).
Where is it used?	ZIP, JPEG, MP3 compression.

✅ In short for viva:
	“This code builds a Huffman Tree using a greedy approach. It takes character frequencies, repeatedly merges the two smallest nodes, and assigns binary codes (0 and 1) based on the tree path. The result is a prefix-free, efficient compression code for each character.”
	
	
	
🧩 Practical: Fractional Knapsack Problem (Using Greedy Method)
Problem Statement:
	Write a program to solve a Fractional Knapsack problem using a greedy method.

🎯 Objective:
We want to maximize the total value we can put into a knapsack (bag) of limited capacity.
Each item has:
	• a weight
	• a value
We can take fractions of items (not necessarily whole), unlike 0/1 knapsack.

🧠 Step-by-step Code Explanation

Step 1: Define the Item class

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
Explanation:
	• This creates a simple Item class with two properties:
		○ weight → how heavy the item is
		○ value → how valuable it is
	• For example, if Item(10, 60) → weight = 10, value = 60.
🧠 Why a class?
It’s easier to handle items as objects instead of managing separate weight and value lists.

Step 2: Define the fractional_knapsack() function

def fractional_knapsack(items, capacity):
	• Takes two inputs:
		○ items → list of Item objects
		○ capacity → total weight the knapsack can hold

Step 3: Compute the value-to-weight ratio for each item

value_weight_ratio = [(item.value / item.weight, item) for item in items]
Explanation:
	• For each item, calculate its value per unit weight = value / weight.
	• Example:
		○ If item value = 100, weight = 20 → ratio = 5
		○ If item value = 120, weight = 30 → ratio = 4
	• Store each ratio along with the item itself in a list of tuples:

[(5, item1), (4, item2), (3, item3)]
🧠 Why?
This is the greedy choice — we always pick the item with the highest value/weight ratio first to maximize gain.

Step 4: Sort items by decreasing ratio

value_weight_ratio.sort(reverse=True)
Explanation:
	• Sorts the list in descending order so the item with the highest value per weight is considered first.
	• That’s the core of the greedy strategy.
🧩 Example after sorting:

[(5, item1), (4, item2), (3, item3)]

Step 5: Initialize total value and knapsack list

total_value = 0.0
knapsack = []
Explanation:
	• total_value: total profit/value accumulated in knapsack.
	• knapsack: stores which items (and how much of them) are selected.

Step 6: Select items greedily

for ratio, item in value_weight_ratio:
    if capacity == 0:
        break
Explanation:
	• Loop through all sorted items one by one.
	• If the knapsack capacity is already full → stop.

Step 7: Take as much as possible of each item

    weight_taken = min(item.weight, capacity)
Explanation:
	• If item’s weight ≤ remaining capacity → take full item.
	• Otherwise → take only the fraction that fits (hence “Fractional Knapsack”).

Step 8: Update total value and capacity

    total_value += weight_taken * ratio
    capacity -= weight_taken
Explanation:
	• Increase total value by: (taken weight × value per unit weight)
	• Reduce remaining capacity.
🧠 Example:
	• ratio = 5 (value/weight)
	• weight_taken = 10
	• total_value += 10 × 5 = 50

Step 9: Record what we took

    knapsack.append((item, weight_taken))
Explanation:
	• Adds item and the portion taken to knapsack list for reference.

Step 10: Return results

return total_value, knapsack
Explanation:
	• Returns:
		○ total_value → maximum profit achieved
		○ knapsack → details of what and how much was chosen

🧾 User Input Section

n = int(input("Enter number of items: "))
items = []
	• Asks user for how many items are there.
	• Initializes an empty list items.

Take item details from user

for i in range(n):
    value = float(input(f"Enter value of item {i+1}: "))
    weight = float(input(f"Enter weight of item {i+1}: "))
    items.append(Item(weight, value))
Explanation:
	• For each item, user enters:
		○ value
		○ weight
	• Creates a new Item object and adds it to the items list.
Example:

Enter number of items: 3
Enter value of item 1: 60
Enter weight of item 1: 10
Enter value of item 2: 100
Enter weight of item 2: 20
Enter value of item 3: 120
Enter weight of item 3: 30

Ask for knapsack capacity

capacity = float(input("Enter maximum capacity of knapsack: "))
Explanation:
	• The maximum total weight the bag can hold.
Example:

Enter maximum capacity of knapsack: 50

🧮 Step 11: Call the function to solve

max_value, selected_items = fractional_knapsack(items, capacity)
Explanation:
	• Calls the function defined earlier.
	• Returns:
		○ max_value: total value obtained
		○ selected_items: list of items chosen with how much of each

🧾 Step 12: Display results

print("\n--- Fractional Knapsack Result ---")
for i, (item, weight_taken) in enumerate(selected_items):
    fraction = weight_taken / item.weight
    print(f"Item {i+1}: Weight = {item.weight}, Value = {item.value}, Fraction taken = {fraction:.2f}")
Explanation:
	• Loops through each selected item and prints:
		○ Weight of item
		○ Value of item
		○ Fraction taken (e.g., 0.50 means half the item was taken)

Step 13: Print total maximum value

print(f"\nMaximum value achievable: {max_value:.2f}")
Explanation:
	• Prints the total maximum profit/value obtained from chosen items.

💡 Example Output

Enter number of items: 3
Enter value of item 1: 60
Enter weight of item 1: 10
Enter value of item 2: 100
Enter weight of item 2: 20
Enter value of item 3: 120
Enter weight of item 3: 30
Enter maximum capacity of knapsack: 50
--- Fractional Knapsack Result ---
Item 1: Weight = 10.0, Value = 60.0, Fraction taken = 1.00
Item 2: Weight = 20.0, Value = 100.0, Fraction taken = 1.00
Item 3: Weight = 30.0, Value = 120.0, Fraction taken = 0.67
Maximum value achievable: 240.00
✅ Meaning:
We took all of item 1 and 2, and ⅔ of item 3, reaching total capacity of 50 with maximum value 240.

🧠 THEORY (for Viva)
Concept	Explanation
Problem Type	Optimization Problem
Approach Used	Greedy Algorithm
Objective	Maximize total value with given capacity
Choice Criterion	Highest value-to-weight ratio
Partial Selection Allowed?	Yes (fractional knapsack)
Data Structure Used	List of items
Time Complexity	O(n log n) (due to sorting step)
Space Complexity	O(n)

🎤 Viva Questions & Answers
Question	Answer
What is the difference between 0/1 and Fractional Knapsack?	In 0/1, we take whole item or none; in fractional, we can take part of an item.
What is the greedy choice property here?	Always select the item with highest value/weight ratio first.
What is the stopping condition?	When the bag becomes full (capacity = 0).
Can the fractional knapsack algorithm be solved using dynamic programming?	No need — greedy gives optimal result directly.
What is the time complexity?	O(n log n), because we sort the items by ratio.
What is the optimal substructure property?	The optimal solution of the problem includes optimal solutions of its subproblems.
Real-life example?	Filling a backpack with most valuable items, cargo loading, resource allocation.

✅ Summary for Viva
	“This program implements the Fractional Knapsack problem using the greedy method. We first calculate the value-to-weight ratio of each item, sort items in descending order of this ratio, and then add items to the knapsack until full. If the next item doesn’t fit completely, we take only a fraction of it. This approach ensures we always get the maximum possible value within the capacity limit.”


Perfect, Jayesh 👏
Now you’ve brought one of the most important DAA practicals — the 0-1 Knapsack Problem using Dynamic Programming (DP).
This one is often heavily discussed in viva, so I’ll explain it line-by-line, including the concept, logic, and expected viva questions with answers.

🧩 Practical 4 — 0/1 Knapsack Problem Using Dynamic Programming
Problem Statement:
	Write a program to solve the 0–1 Knapsack problem using the Dynamic Programming approach.

🎯 Objective
We have a set of n items, each with:
	• A value (profit)
	• A weight
We have a knapsack with maximum capacity (W).
We must choose items such that:
	• The total weight ≤ capacity, and
	• The total value is maximized.
🧠 Condition:
You can either take the whole item (1) or leave it (0) — no fractions allowed.
Hence, it’s called the 0–1 Knapsack problem.

✅ Step-by-Step Code Explanation

Step 1 — Function Definition
def knapsack_01(values, weights, capacity):
    n = len(values)
	• We define a function knapsack_01() that takes:
		○ values: list of item values
		○ weights: list of item weights
		○ capacity: maximum weight knapsack can hold
	• n = number of items.

Step 2 — Initialize the DP Table
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
Explanation:
	• We create a 2D Dynamic Programming (DP) table of size (n+1) × (capacity+1).
	• Each cell dp[i][w] represents:
The maximum value that can be achieved using the first i items with a total weight ≤ w.
	• Initialize all to 0 (base case — if no items or capacity 0, value = 0).
🧠 Example:
If n = 3, capacity = 5 → table size = 4 × 6
dp = 
[[0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0]]

Step 3 — Fill the DP Table
for i in range(1, n + 1):
    for w in range(1, capacity + 1):
	• Loop through all items (1 to n)
	• Loop through all capacities (1 to W)
	• For each item, we check whether to include or exclude it.

Step 4 — Choice Condition
if weights[i - 1] <= w:
    dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],
                   dp[i - 1][w])
else:
    dp[i][w] = dp[i - 1][w]
Let’s understand this clearly:
✅ Case 1 — Item can fit (weight ≤ capacity):
We have two choices:
	1. Include the item:
		○ Add its value → values[i-1]
		○ Reduce the remaining capacity → w - weights[i-1]
		○ Add whatever max value we could get with that remaining capacity
→ dp[i-1][w - weights[i-1]]
		○ Total = values[i-1] + dp[i-1][w - weights[i-1]]
	2. Exclude the item:
		○ Just take whatever max value we got without it → dp[i-1][w]
👉 Choose the maximum of these two using max().
✅ Case 2 — Item too heavy (weight > capacity):
	• Can’t include it, so take the previous best value:
dp[i][w] = dp[i - 1][w]


Step 5 — Backtracking to Find Which Items Were Chosen
selected_items = []
i, w = n, capacity
while i > 0 and w > 0:
    if dp[i][w] != dp[i - 1][w]:
        selected_items.append(i - 1)
        w -= weights[i - 1]
    i -= 1
Explanation:
	• After filling the DP table, dp[n][capacity] gives the maximum value.
	• Now we backtrack to find which items were included:
		○ If dp[i][w] != dp[i-1][w] → item i-1 was included.
		○ Subtract its weight from w (remaining capacity).
		○ Move to previous item (i -= 1).
	• Repeat until no capacity or items left.

Step 6 — Reverse Selected Items (optional)
selected_items.reverse()
Just reorders items to original input order (for neat output).

Step 7 — Return Results
return dp[n][capacity], selected_items, dp
	• Returns:
		○ dp[n][capacity] → maximum value achievable
		○ selected_items → which items were selected
		○ dp → full DP table (for visualization)

🧾 User Input Section
Take Inputs
n = int(input("Enter number of items: "))
values = []
weights = []
Then loop to read each item:
for i in range(n):
    v = int(input(f"Enter value of item {i+1}: "))
    w = int(input(f"Enter weight of item {i+1}: "))
    values.append(v)
    weights.append(w)
Ask for knapsack capacity:
max_capacity = int(input("Enter maximum capacity of knapsack: "))

Call the Function
max_value, selected_items, dp_table = knapsack_01(values, weights, max_capacity)

Display DP Table
print("\n--- DP Table ---")
for row in dp_table:
    print(row)
Prints the table showing how subproblems are solved step by step.

Show Which Items Were Selected
print("\nSelected Items:")
for idx in selected_items:
    print(f"Item {idx+1} -> Weight: {weights[idx]}, Value: {values[idx]}")

Print Maximum Value
print(f"\nMaximum value achievable: {max_value}")

🧮 Example Output
0-1 Knapsack Problem
Enter number of items: 3
Enter value of item 1: 60
Enter weight of item 1: 10
Enter value of item 2: 100
Enter weight of item 2: 20
Enter value of item 3: 120
Enter weight of item 3: 30
Enter maximum capacity of knapsack: 50
--- DP Table ---
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
...
Selected Items:
Item 2 -> Weight: 20, Value: 100
Item 3 -> Weight: 30, Value: 120
Maximum value achievable: 220
✅ The optimal solution gives maximum profit = 220, using items 2 and 3.

🧠 THEORY (For Viva)
Concept	Explanation
Problem Type	Optimization
Approach	Dynamic Programming
Objective	Maximize total value without exceeding capacity
Choices per item	Either take it (1) or leave it (0)
Subproblem	Best value for first i items and weight w
DP Relation	dp[i][w] = max(value[i-1] + dp[i-1][w-weight[i-1]], dp[i-1][w])
Base Case	dp[0][*] = 0, dp[*][0] = 0
Time Complexity	O(n × W)
Space Complexity	O(n × W)
Algorithm Type	Bottom-up Dynamic Programming

🎤 Common Viva Questions & Answers
Question	Answer
What is the difference between 0-1 and Fractional Knapsack?	In 0-1, you either take the whole item or not; in fractional, you can take part of an item.
Why can’t the greedy method be used here?	Because local optimum (best ratio) doesn’t guarantee global optimum — only DP ensures the best total.
What is the recurrence relation?	dp[i][w] = max(value[i-1] + dp[i-1][w-weight[i-1]], dp[i-1][w])
What does dp[i][w] represent?	The maximum value attainable with first i items and capacity w.
What is time complexity?	O(n × W).
What is the space complexity?	O(n × W).
Can it be optimized for space?	Yes, we can use a 1D array instead of 2D (space-optimized DP).
What is backtracking used for?	To find which items were selected to get the optimal value.
Is it an NP-complete problem?	Yes, but dynamic programming gives a pseudo-polynomial time solution.

✅ Viva Summary (To Speak)
	“In this practical, we implemented the 0–1 Knapsack problem using dynamic programming.
	We created a DP table to store solutions of subproblems, where each cell represents the maximum profit achievable with given items and capacity.
	By filling this table iteratively, we obtain the maximum value possible without exceeding the capacity.
	Unlike the fractional knapsack, we can’t take fractions — each item is either taken or left.
	This approach has time complexity O(n×W) and ensures an optimal solution.”

Would you like me to also give you a comparison table of 0-1 Knapsack vs Fractional Knapsack (used frequently in viva)?

From <https://chatgpt.com/c/690a20bd-f458-8320-89ad-e31c4ae06d95> 

Excellent Jayesh 👏
This is a clean and exam-ready implementation of the N-Queens Problem using Backtracking, where the first queen is already placed — exactly as required by your practical.
Now, let’s go step by step 👇
I’ll explain every line of your code clearly — what it does, why it’s written that way, and also give theory + viva questions and answers for your understanding and practical exam.

🧩 Practical 5 — N-Queens Problem using Backtracking
Problem Statement:
	Design an n × n chessboard having the first Queen placed.
	Use backtracking to place the remaining Queens to generate the final N-Queens matrix.

🎯 Objective
The goal is to place n queens on an n×n chessboard such that:
	• No two queens attack each other.
That means:
	1. No two queens share the same row
	2. No two queens share the same column
	3. No two queens share the same diagonal

🧠 Step-by-Step Code Explanation

Step 1 — Function to Print the Board
def print_board(board):
    n = len(board)
    for i in range(n):
        row = ""
        for j in range(n):
            if board[i] == j:
                row += " Q "
            else:
                row += " . "
        print(row)
    print("\n")
Explanation:
	• The board list keeps track of queen positions:
board[i] = j means Queen at row i, column j.
	• We loop through each row and column:
		○ If there’s a queen (board[i] == j), print " Q "
		○ Else, print " . " (empty space)
	• After each row, we print a new line for the chessboard format.
🧩 Example Output for 4×4:
 .  Q  .  .
 .  .  .  Q
 Q  .  .  .
 .  .  Q  .

Step 2 — Check if Position is Safe
def is_safe(board, row, col):
    for i in range(row):
        # Check column conflict
        if board[i] == col:
            return False
        # Check diagonal conflicts
        if abs(board[i] - col) == abs(i - row):
            return False
    return True
Explanation:
Before placing a queen at (row, col), we check for conflicts with all previously placed queens.
	• Column Conflict:
If another queen already exists in the same column (board[i] == col), it’s unsafe.
	• Diagonal Conflict:
If two queens are on the same diagonal,
the absolute difference between their columns equals the difference between their rows:
abs(board[i] - col) == abs(i - row)
If neither condition is true, the position is safe, and we return True.

Step 3 — Backtracking Function
def solve_n_queens(board, row):
    n = len(board)
    if row == n:
        print("Solution found:")
        print_board(board)
        return True  # Change to False to find all solutions
Explanation:
	• row == n means all queens are placed successfully (we reached the end of the board).
	• Print the board as one valid solution.
	• return True stops after finding the first solution.
	• You can change it to False if you want to find all possible solutions.

Step 4 — Try Placing a Queen in Each Column
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col  # Place queen
            if solve_n_queens(board, row + 1):
                return True  # Stop after first solution
            board[row] = -1   # Backtrack
    return False
Explanation:
	• Try each column in the current row (for col in range(n)).
	• If is_safe() returns True, place the queen (board[row] = col).
	• Then recursively call the function for the next row (row + 1).
🧠 Backtracking Concept:
	• If placing a queen leads to no solution further,
remove the queen (board[row] = -1) and try next column.
	• This is the backtrack step — undo the previous move and explore a new one.
If no column works in this row → return False → go back (backtrack).

Step 5 — Main Code Section
n = int(input("Enter size of board (n): "))
	• Takes board size (number of queens) from user.
Example:
Enter size of board (n): 4

Step 6 — Initialize Board
board = [-1] * n
Explanation:
	• Creates a list with -1 meaning no queen placed in any row yet.
	• Example for n=4 → [-1, -1, -1, -1]

Step 7 — Take Input for First Queen
first_row = int(input("Enter row for first queen (0-based index): "))
first_col = int(input("Enter column for first queen (0-based index): "))
board[first_row] = first_col  # Place the first queen
Explanation:
	• You manually specify where the first queen is already placed.
	• Example:
Enter row for first queen (0-based index): 0
Enter column for first queen (0-based index): 1

→ First queen placed at (0,1)

Step 8 — Choose Starting Row
start_row = 0 if first_row != 0 else 1
Explanation:
	• If first queen is not in row 0, start solving from row 0.
	• If first queen is in row 0, start from next row (row 1).

Step 9 — Solve the N-Queens Problem
if not solve_n_queens(board, start_row):
    print("No solution exists.")
Explanation:
	• Calls the recursive solver function.
	• If no solution found, prints “No solution exists”.

🧮 Example Run
Enter size of board (n): 4
Enter row for first queen (0-based index): 0
Enter column for first queen (0-based index): 1
Solution found:
 .  Q  .  .
 .  .  .  Q
 Q  .  .  .
 .  .  Q  .
✅ All queens are placed safely — none attack each other.

🧠 THEORY — N-Queens and Backtracking
Concept	Explanation
Problem Type	Constraint Satisfaction Problem
Algorithm Used	Backtracking
Objective	Place n queens such that no two attack each other
Constraints	No two queens share same row, column, or diagonal
Data Structure Used	1D list representing the board
Base Case	If all queens are placed (row == n), print solution
Backtracking Step	Remove queen (board[row] = -1) and try next column
Time Complexity	O(N!) (factorial)
Space Complexity	O(N)
Real-world use	Scheduling, puzzle solving, circuit layout, AI search problems

🎤 Common Viva Questions (and Answers)
Question	Answer
What is the N-Queens problem?	It’s the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Why is backtracking used?	Because we explore possible positions, and backtrack when a position leads to no solution.
What does “backtracking” mean?	It means undoing the previous move when a dead-end is reached and trying another path.
What is the base condition?	When all queens are placed (row == n).
How do we check diagonal conflicts?	If abs(board[i] - col) == abs(i - row) for any i < row.
Can we solve this using brute force?	Yes, but it’s inefficient — backtracking reduces unnecessary checks.
What is the time complexity?	O(N!), as we try all possible placements.
What is the space complexity?	O(N), for the board array and recursion stack.
What if we want all solutions?	Replace return True with return False to continue searching.
Real-life use?	Solving constraint-based problems like Sudoku, job assignment, and resource allocation.

✅ Short Viva Summary (How to Answer)
	“In this practical, we implemented the N-Queens problem using backtracking.
	We first place one queen manually and then use recursion to place the remaining queens one by one in safe positions.
	If a position causes a conflict, we backtrack and try the next possible column.
	This continues until all queens are placed or no solution exists.
	The algorithm’s time complexity is O(N!), and it’s a classic example of backtracking.”

Would you like me to show a diagrammatic explanation (4×4 example) of how the queens are placed and backtracked step by step? It’s very useful to explain visually during viva.

From <https://chatgpt.com/c/690a20bd-f458-8320-89ad-e31c4ae06d95> 


![Uploading image.png…]()
