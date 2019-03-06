print("Hello World!")

def minmax():
    l = (int(x) for x in input("Enter numbers: ").split())


    min = l[0]
    max = l[0]

    for i in l:
        if i < min:
            min = i
        if i > max:
            max = i

    print("Min = ",min)
    print("Max = ",max)

minmax()
