#Error Detection Alorithm

data = []

def printdata_parity(a):
    print(data)
    print("Parity bit : ", data[a])

def sender():

    c = 0

    a = int(input("Enter the number of bits to be transmitted : "))
    print("Enter the bits to be transmitted ")

    for i in range(0, a):
        inp = int(input(">"))
        data.append(inp)
        if (inp != 1 and inp != 0):
            print("!!!!!!!!!!!!!!       Enter Binary Numbers i.e. 1 and 0       !!!!!!!!!!!!!!")
            exit()

    print("Data to be transmitted using parity ?")
    print("1. Even Parity\n2. Odd Parity")
    b = int(input("Enter your choice : "))

    if (b == 1):

        for i in range(0, a):
            if (data[i] == 1):
                c = c + 1

        if (c % 2 == 0):
            data.append(0)
            printdata_parity(a)

        else:
            data.append(1)
            printdata_parity(a)

    elif (b == 2):

        for i in range(0, a):
            if (data[i] == 1):
                c = c + 1

        if (c % 2 == 0):
            data.append(1)
            printdata_parity(a)

        else:
            data.append(0)
            printdata_parity(a)

    else:
        print("INVALID")
        exit()

    reciever(a,b)

    return a,b

def reciever(a,b):

    d = 0

    for i in range(0, a + 1):
        if (data[i] == 1):
            d = d + 1

    if (d % 2 == 0 and b == 1):  # COUNT OF 1 EVEN & EVEN PARITY
        print("The recieved data is CORRECT")

    elif (d % 2 == 0 and b == 2):  # COUNT OF 1 EVEN & ODD PARITY
        print("The recieved data is wrong")

    elif (d % 2 != 0 and b == 2):  # COUNT OF 1 ODD & ODD PARITY
        print("The recieved data is CORRECT")

    elif (d % 2 != 0 and b == 1):  # COUNT OF 1 ODD & EVEN PARITY
        print("The recieved data is WRONG")

sender()