import math
from turtle import left, right

def search(left, right):

    mid = (left + right) // 2 # Calculates the middle index (or) mid = math.floor((left + right) / 2) 

    if arr[mid] == target:
        print(f"Element found at index {mid}")
    elif arr[mid] < target:
        search(mid + 1, right)
    elif arr[mid] > target:
        search(left, mid - 1)
    else:
        print("Element not found")

while True:
    print("--------------------------------------------------")
    print("Welcome to the search program")
    print("Enter 1 for binary search") 
    print("Enter 2 for linear search")
    print("Enter 3 to end the program")

    print("Enter choice")
    choice = int(input())
    if choice != 1 and choice != 2 and choice != 3:
        print("Invalid choice")
        continue

    if choice == 3:
        break

    print("Enter array size")
    n = int(input())

    print("Enter numbers in the array")
    arr = []
    for i in range(n):
        arr.append(int(input()))
    
    if choice == 1:
        print("Performing binary search...")
        arr.sort()  # Sort the array before searching
        print("Sorted Array:", arr)
        print("Enter number to be searched")
        target = int(input())
        begin=0
        last = len(arr)-1

        search(begin, last)

    elif choice == 2:
        print("Performing linear search...")
        print("Array:", arr)
        print("Enter number to be searched")
        target = int(input())
        if target in arr:
            print(f"Element found at index {arr.index(target)}")

        else:
            print("Element not found")

