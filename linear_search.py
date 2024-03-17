x = int(input("Enter an array size"))
print("Enter the elements")
arr =[]

for i in range (0,x):
    element = int(input())
    arr.append(element)

target = int(input("Enter tageted value"))

def liner_search(arr,target):
    for i in range (0,len(arr)):
        if(target==arr[i]):
            return i 

print(liner_search(arr,target))