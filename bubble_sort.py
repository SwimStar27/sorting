my_list=[12,44,8,3]
n=len(my_list)

for i in range(n):
    print("Pass: ", i+1)
    swapped=False
    for r in range (0,n-1):
        if my_list[r]>my_list[r+1]:
            swapped = True
            temp = my_list[r]
            my_list[r] = my_list[r+1]
            my_list[r+1] = temp
            print(my_list)

    if not swapped:
        break
print("*"*20)