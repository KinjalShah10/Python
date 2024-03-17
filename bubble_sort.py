# array=input("Enter the array")
# print(array)
arr =[]
x = int(input("Enter an array"))
print("Enterr the elements")
for i in range (0,x):
    element = int(input())
    arr.append(element)


def bubble_sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1):
            if(arr[j]>arr [j+1]):
                arr[j],arr[j+1] = arr[j+1], arr[j]  
    return arr

print(bubble_sort(arr))


