arr = [1, 2, 3, 4, 5]

for i in range(len(arr)):
    swapped = False

    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    if not swapped:
        print("Stopped early!")
        break

print(arr)