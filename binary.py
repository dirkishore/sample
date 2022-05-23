def binary_search(list_arr):
       print(list_arr)
       #binary search algo...
       search_input=int(input("enter the number to search:"))
       start=0;
       end=len(list_arr)-1
       mid=0
       while(start<=end):
         mid=(end+start)//2
         if(list_arr[mid]<search_input):
             start=mid+1
         elif(list_arr[mid]>search_input):
             end=mid-1
         else:
             return mid;
       return-1

obj_res=binary_search([1,2,3,4,5,6,7,8,9,10])
print("The Element in the index at:'"+str(obj_res)+"'"if(obj_res!=-1)else"Element not present");
