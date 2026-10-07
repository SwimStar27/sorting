arr = [15, 32, 59, 21, 48]

for i in range(len(arr)):
    for j in range(len(arr) - 1 - i):
        if (arr[j] % 10) > (arr[j + 1] % 10):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)