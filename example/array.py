def vyvod (arr,n):
    print("Array:")
    i = 0
    while (i < n):
        print(arr[i], end=" ")
        i += 1
    print("")
def vvod():
    arr = list()
    n = int(input("Enter number of elements: "))
    print("Enter elements:")
    i = 0
    while (i < n):
        tmp = int(input(""))
        arr.append(tmp)
        i += 1
    return arr, n
arr, n = vvod()
vyvod(arr,n)