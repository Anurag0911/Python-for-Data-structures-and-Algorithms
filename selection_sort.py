def select_sort(ls):
    for i in range(len(ls)-1):
        minIndex = i
        for j in range(i+1, len(ls)):
            if ls[j]< ls[minIndex]:
                minIndex = j
            if i != minIndex:
                ls[i], ls[minIndex] = ls[minIndex], ls[i]
    return ls


a = [3,2,5,4,25,2,43,34,2,2,34,2,32]
select_sort(a)
print(a)