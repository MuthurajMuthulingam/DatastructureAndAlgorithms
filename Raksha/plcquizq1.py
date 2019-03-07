#Placement quiz 1 Q1

def count_values():

    #Input list P
    p = [int(x) for x in input("Enter list P: ").split()]
    #Input list Q in ascending order
    q = [int(x) for x in input("Enter list Q in ascending order: ").split()]

    #count = 0
    for i in range(len(p)):
        count = 0
        n = p[i]

        if ((n>= q[0]) and (n<= q[len(q)-1])):

            low = 0
            h =len(q)-1
            mid = 0

            #Start loop
            while(low<=h):
                mid = (low+h)//2

                if q[mid] is n:
                    count = mid+1
                    break

                elif n > q[mid]:
                    count = mid+1
                    l = mid + 1

                else:
                    break

            print(count, end=' ')

        #Terminate directly if n not in range of list values.
        elif n<q[0]:
            print("0",end = ' ')
        else :
            print(len(q),end = ' ')


count_values()
#Placement quiz 1 Q1

def count_values():

    #Input list P
    p = [int(x) for x in input("Enter list P: ").split()]
    #Input list Q in ascending order
    q = [int(x) for x in input("Enter list Q in ascending order: ").split()]

    #count = 0
    for i in range(len(p)):
        count = 0
        n = p[i]

        if ((n>= q[0]) and (n<= q[len(q)-1])):

            low = 0
            h =len(q)-1
            mid = 0

            #Start loop
            while(low<=h):
                mid = (low+h)//2

                if q[mid] is n:
                    count = mid+1
                    print(count, end=" ")
                    break

                elif n > q[mid]:
                    count = mid+1
                    l = mid + 1

                else:
                    break
            else:
                print(count, end=' ')

        #Terminate directly if n not in range of list values.
        elif n<q[0]:
            print("0",end = ' ')
        else :
            print(len(q),end = ' ')


count_values()
