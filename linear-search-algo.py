def search(arr, N, x):
    for i in range(0, N):
        if(arr[i] == x):
            return i
    return -1

if __name__ == "__main__":
    arr=[10,20,50,90,120,40,80]
    x= 110
    N = len(arr)

    result = search(arr, N, x)
    if(result != -1):
        print("Element is present at index : ", result)
    else:
        print("Element is not present in the array")   


