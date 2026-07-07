print("Informatio Table")
table = {}

print("Please enter 5 pairs of items (e.g., Apple and Red):")

# 1. Ask the user for 5 pairs
for i in range(5):
    print(f"\n--- Pair {i + 1} ---")
    key = input("Enter Item 1: ")
    value = input("Enter Item 2: ")
    table[key] = value

# 2. Print a clean, formatted table
print("\nYour Formatted Table:")
print("-" * 30)
print(f"{'Item 1':<15} | {'Item 2'}")

for item1, item2 in table.items():
    print(f"{item1:<15} | {item2}")
