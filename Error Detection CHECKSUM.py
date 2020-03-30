data = []

def reciever(data, n):
    s1 = 0
    for c in range(0, n+1):
        m1 = 0
        m1 = data[c]
        m1 = int(m1, 2)
        s1 = s1 + m1
    if (s1 == 0):
        print("Data Sent Successfully")
    else:
        print("Data is not sent Successfully")

def sumsfunc(data, n):
    s = 0
    for c in range(0, n):
        m = 0
        m = data[c]
        m = int(m,2)
        s = s + m

    print("Checksum : ",+s)
    print("Checksum : ",bin(s))
    data.append(bin(-s))
    print("SENDING.....")
    print("Transmitted data is : ",data)

    reciever(data, n)

a = int(input("Enter the number of data bits to be transmitted : "))
print("Enter the  bits to be transmitted ")

for i in range (a):
    inp = int(input(">"))
    data.append(bin(inp))

sumsfunc(data, a)
