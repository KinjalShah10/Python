x= int(input("Enter array size"))
print("Enter the elemnets")
arr=[]

for i in range(0,x):
    elements=int(input())
    arr.append(elements)

target = int(input("Enter tageted value"))    

def binary_sort(arr,target):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(high+low)//2
        if(target==arr[mid]):
            return mid
        elif(target<arr[mid]):
            high=mid-1
        else:
             low=mid+1
    return -1         


result=binary_sort(arr,target)   
if result==-1:
    print("elemnt not found")
else:
    print(f"element found at index {result}")    




