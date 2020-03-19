data = []

def reciever(s):
    su = sum(data)
    if (su == 0):
        print("Data Sent Successfully")
    else:
        print("Data is not sent Successfully")

def sumsfunc(data):
    s = sum(data)
    print("Checksum : ",s)
    data.append(-s)
    print("SENDING.....")
    print("Transmitted data is : ",data)
    reciever(data)

a = int(input("Enter the number of data bits to be transmitted : "))
print("Enter the  bits to be transmitted ")

for i in range (a):
    inp = int(input(">"))
    data.append(inp)

sumsfunc(data)