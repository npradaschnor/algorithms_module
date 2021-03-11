def bubble_sort(arr):
    n = len(arr)
    for outer in range(n-1, 0, -1):
        for inner in range(0,outer,1):
            print(f"inner is {inner} swapping {arr[inner]} and {arr[inner+1]}");

            if arr[inner] > arr[inner+1]:
                temp = arr[inner]
                arr[inner] = arr[inner+1]
                arr[inner+1] = temp
                
        print(f"outer is {outer}")
        print(arr)

def selection_sort(arr):
    n = len(arr)
    for outer in range(0,n,1):
        min = outer
        print(f"outer is {outer}")
        for inner in range(outer+1,n,1):
            if arr[inner] < arr[min]:
                min = inner;
                
        print(f"min is {min}")
        print(f"swapping {arr[outer]} and {arr[min]}")
        temp = arr[outer]
        arr[outer] = arr[min]
        arr[min] = temp
        
arr = [7,5,2,3,1]
#bubble_sort(arr)
selection_sort(arr)
print(arr)