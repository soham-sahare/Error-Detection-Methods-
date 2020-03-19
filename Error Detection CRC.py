def xor(a, b):
    data = []

    for i in range(1, len(b)):
        if a[i] == b[i]:
            data.append('0')
        else:
            data.append('1')

    return ''.join(data)

def bindiv(data, genbit):
    z = len(genbit)

    tempvar = data[0: z]

    while z < len(data):

        if tempvar[0] == '1':
            tempvar = xor(genbit, tempvar) + data[z]

        else:
            tempvar = xor('0' * z, tempvar) + data[z]

        z += 1

    if tempvar[0] == '1':
        tempvar = xor(genbit, tempvar)
    else:
        tempvar = xor('0' * z, tempvar)

    checkword = tempvar
    return checkword

def reciever(correct,genbit):
    bindiv(correct,genbit)
    print("Reciever's Side.... ")
    if (int(remainder1) == 0):
        print("Data is transmitted Successfully")
    else:
        print("Data is NOT transmitted Successfully")

data = input("Enter the data bits to be transmitted : ")
for i in range(0, len(data)):
    if (data[i] == '1' or data[i] == '0'):
        pass
    else:
        print("!!!!!!!!!!!!!!       Enter Binary Number i.e. 1 and 0       !!!!!!!!!!!!!!")
        exit()

genbit = input("Enter the generator bits : ")
for i in range(0, len(genbit)):
    if (genbit[i] == '1' or genbit[i] == '0'):
        pass
    else:
        print("!!!!!!!!!!!!!!       Enter Binary Number i.e. 1 and 0       !!!!!!!!!!!!!!")
        exit()

length = len(genbit)

appended_data = data + '0' * (length - 1)
remainder = bindiv(data, genbit)

correct = data + remainder
print("Remainder (CRC): ", remainder)
print("Transmitted data : ",correct)
remainder1 = bindiv(correct,genbit)
reciever(correct,genbit)