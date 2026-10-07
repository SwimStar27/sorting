arr = [12, 18, 22, 3, 48]
n = len(arr)

for i in range(1,n):
    key = arr[i]
    print("Key",key)
    r = i-1
    while r>= 0 and key<arr[r]:
        arr[r+1]=arr[r]
        r-=1
        print(arr)
    arr[r+1] = key
    print(arr)
    print("-"*20)