# Fractional Knapsack Problem using Greedy Method

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def fractional_knapsack(items, capacity):
    # Step 1: Calculate value-to-weight ratio for each item
    value_weight_ratio = [(item.value / item.weight, item) for item in items]

    # Step 2: Sort items by decreasing ratio (greedy choice)
    value_weight_ratio.sort(reverse=True)

    total_value = 0.0
    knapsack = []

    # Step 3: Pick items for knapsack
    for ratio, item in value_weight_ratio:
        if capacity == 0:
            break
        weight_taken = min(item.weight, capacity)       # Take full item or fraction
        total_value += weight_taken * ratio
        capacity -= weight_taken
        knapsack.append((item, weight_taken))

    return total_value, knapsack

# ---------- USER INPUT ----------
n = int(input("Enter number of items: "))
items = []

for i in range(n):
    value = float(input(f"Enter value of item {i+1}: "))
    weight = float(input(f"Enter weight of item {i+1}: "))
    items.append(Item(weight, value))

capacity = float(input("Enter maximum capacity of knapsack: "))
# --------------------------------

# Step 4: Solve Fractional Knapsack
max_value, selected_items = fractional_knapsack(items, capacity)

# Step 5: Display results
print("\n--- Fractional Knapsack Result ---")
for i, (item, weight_taken) in enumerate(selected_items):
    fraction = weight_taken / item.weight
    print(f"Item {i+1}: Weight = {item.weight}, Value = {item.value}, Fraction taken = {fraction:.2f}")

print(f"\nMaximum value achievable: {max_value:.2f}")

