import time

a = [2,3,5,6,8,1,4,7]
b = [6,3,7,4,8,2,5,1]
c = [8,2,5,7,1,6,4,3]

def bubbleSort_method_1(someList):
    start_time = time.time()
    continueLoop = True
    i = 0
    while continueLoop:
        #print(i, continueLoop)
        if i == len(someList)-1:
            continueLoop = False
        elif someList[i]>someList[i+1]:
            someList[i], someList[i+1] = someList[i+1], someList[i]
            i = 0
        elif i < len(someList):
            i += 1
    end_time = time.time()
    print(end_time-start_time)
    return someList

print(bubbleSort_method_1(a))
print(bubbleSort_method_1(b))
print(bubbleSort_method_1(c))

def bubbleSort_method_2(someList):
    start_time = time.time()
    for j in range(len(someList)-1):
        for i in range(len(someList)-1-j):
            if someList[i]>someList[i+1]:
                someList[i], someList[i+1] = someList[i+1], someList[i]
    end_time = time.time()
    print(end_time-start_time)
    return someList

print(bubbleSort_method_2(a))
print(bubbleSort_method_2(b))
print(bubbleSort_method_2(c))