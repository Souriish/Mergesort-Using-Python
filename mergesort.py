def mergeSort(x):
    if len(x)>1:
        mid=len(x)//2
        L=x[:mid]
        R=x[mid:]
        mergeSort(L)
        mergeSort(R)

        x.clear()
        while len(L)>0 and len(R)>0:
            if L[0]<=R[0]:
                x.append(L[0])
                L.pop(0)
            else:
                x.append(R[0])
                R.pop(0)

        for i in L:
            x.append(i)
        for i in R:
            x.append(i)

x=[1050,1,291,5555555,88888,12,9]
print("Array to be sorted is:")
print(*x)

mergeSort(x)

print("Array after sorting is:")
print(*x)
