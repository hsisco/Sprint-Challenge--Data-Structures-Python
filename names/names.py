import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):                # Insert the given value into the tree
        if value < self.value:              # Case 1: value < root/parent (self.value)
            if self.left is None:               # If no left child...
                self.left = BSTNode(value)      # ...insert value here
            else:                               # Else:
                self.left.insert(value)         # Repeat this process on Left subtree
        
        if value >= self.value:             # Case 2: value > or = root/parent (self.value)
            if self.right is None:              # If no right child...
                self.right = BSTNode(value)     # ...insert value here
            else:                               # Else:
                self.right.insert(value)        # Repeat this process on Right subtree

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:            # Case 1: self.value = target
            return True
        elif target < self.value:           # Case 2: target < self.value
            if self.left is None:               # If self.left is None...
                return False                    # ...its not in the tree
            else:                               # or return with proof
                return self.left.contains(target)
        else:                               # Case 3: otherwise
            if self.right is None:              # If self.left is None...
                return False                    # ...its not in the tree
            else:                               # or return with proof
                return self.right.contains(target)

start_time = time.time()

with open('names_1.txt') as f:
    names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

with open('names_2.txt', 'r') as f:
    names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
tree = BSTNode(names_1[0])

for i in names_1:
    tree.insert(i)

for i in names_2:
    if tree.contains(i):
        duplicates.append(i)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.