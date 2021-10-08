def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        swap = 1
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap += 1
        if swap == 0:
            break


a = [3,2,5,4,25,2,43,34,2,2,34,2,32]
bubble_sort(a)
print(a)
