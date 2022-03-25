

def decabin(num):
    conv=[]
    if num>0:
        i=0
        while(num > 0):
            idx = num % 2
            num = int(num / 2)
            conv.append(idx)
            i += 1
        conv.reverse()
        for i in range(len(conv)):
            print(conv[i], end="")
    else:
        print ("inserte num >0")

num = input("inserte un numero: ")
decabin(int(num))
