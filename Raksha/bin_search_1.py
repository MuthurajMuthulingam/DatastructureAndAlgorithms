#Binary search implimentation for Descending order
# Worst case when value is not in list = O(1)
# Other cases = O(log n)
 
def bin_search():
    #Input list
    l = [int(x) for x in input("Enter list: ").split()]

    n = int(input("Enter value to be searched: "))

    low = 0
    h =len(l)-1
    mid = 0

    #Checking if list is not empty and n lies in range of values in the given list, only then execute. else terminate directly.

    if ((l == []) or (n>= l[h] and n<=l[low])):

        #Start loop
        while(low<=h):
            mid = (low+h)//2

            if l[mid] is n:
                print(f"Value {n} found at position {mid}.")
                break

            elif n > l[mid]:
                h = mid - 1

            else:
                low = mid + 1

        else:
            print(f"Value {n} not found.")
#Terminate directly if n not in range of list values.
    else:
        print(f"Value {n} not found.")

bin_search()
