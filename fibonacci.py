def Space(fibnum, placenum):
    FibNumLength = len(str(fibnum))
    PlaceNumLength = len(str(placenum))
    return 30 - FibNumLength - PlaceNumLength

def Fibonacci(num):
    print("Fibonacci sequence:\n")
    print("1." + Space(1, 1)*" " + "0\n")
    print("2." + Space(1, 1)*" " + "1\n")
    Fib1 = 0
    Fib2 = 1
    for i in range(3,num+1):
        FibI = Fib2 + Fib1
        SpaceNum = Space(FibI, i)
        print(str(i) + "." + SpaceNum*" " + str(FibI) + "\n")
        Fib1 = Fib2
        Fib2 = FibI

Fibonacci(int(input("Length of Fibonacci sequence: ")))