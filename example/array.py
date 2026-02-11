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
    if n <= 15 and n > 0:
        print("Enter elements:")
        i = 0
        while (i < n):
            tmp = int(input(""))
            arr.append(tmp)
            i += 1
        return arr, n
    else:
        print("There should be no more than 15 elements")
        exit()
arr, n = vvod()
vyvod(arr, n)