# 0-1 Knapsack Problem using Dynamic Programming
# Exam-ready version

def knapsack_01(values, weights, capacity):
    n = len(values)

    # Step 1: Initialize DP table (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Step 2: Fill DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Max of including the item or not including it
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Step 3: Backtrack to find selected items
    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  # store index of selected item
            w -= weights[i - 1]           # reduce remaining capacity
        i -= 1

    selected_items.reverse()  # optional: for original order
    return dp[n][capacity], selected_items, dp  # return DP table too

# ------------------- USER INPUT -------------------
print("0-1 Knapsack Problem")
n = int(input("Enter number of items: "))

values = []
weights = []

for i in range(n):
    v = int(input(f"Enter value of item {i+1}: "))
    w = int(input(f"Enter weight of item {i+1}: "))
    values.append(v)
    weights.append(w)

max_capacity = int(input("Enter maximum capacity of knapsack: "))

# ------------------- CALCULATION -------------------
max_value, selected_items, dp_table = knapsack_01(values, weights, max_capacity)

# ------------------- OUTPUT -------------------
print("\n--- DP Table ---")
for row in dp_table:
    print(row)

print("\nSelected Items:")
for idx in selected_items:
    print(f"Item {idx+1} -> Weight: {weights[idx]}, Value: {values[idx]}")

print(f"\nMaximum value achievable: {max_value}")

