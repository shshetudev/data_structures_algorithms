import array

## append operations: add at the bottom
arr = array.array('i', [1, 2, 3])

for i in range(0, 3):
    print(arr[i], end=" ")
print("\r")

arr.append(4);
print("APPEND:")
print("Printing appended array is: ", end="")
for i in range(len(arr)):
    print(arr[i], end=" ")

## insert: add value at the ith position, O(n)
print("\n\nINSERT:")
arr.insert(2, 5)
for i in range(len(arr)):
    print(arr[i], end=" ")

# pop(): Removes the element at the mentioned position and returns it
print("\n\nPOP:")
arr.pop(2)
for i in range(len(arr)):
    print(arr[i], end=" ")


# remove(): Removes first occurrence of the value mentioned in its argument
print("\n\nREMOVE:")
arr.remove(2)
for i in range(len(arr)):
    print(arr[i], end=" ")

# index(): Returns the index of the value mentioned in the arguments
print("\n\nINDEX:")
arr.index(3)

# reverse():
print("\n\nREVERSE:")
arr.reverse()
for i in range(len(arr)):
    print(arr[i], end=" ")