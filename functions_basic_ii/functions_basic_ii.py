# 1.
def countDown(max):
    for x in range(max,-1,-1):
        print(x)
countDown(10)

print('')
#2.
def printReturn(first, second):
    print(first)
    return(second)
print(printReturn(1,2))

print('')

#3.

x = [1,2,3,4,5,6,7,8,9]

def firstPlusLength(x):
    print(x[0] + len(x))
firstPlusLength(x)

print('')

#4.
def valuesGreaterThanSecond(arr):
    new_arr = []
    if len(arr) < 2:
        return False
    else:
        print(arr[2])
        for x in arr:
            if x >= arr[2]:
                new_arr.append(x)
    return new_arr

print(valuesGreaterThanSecond([1,10,3,5,8]))

# 5
def thisLengthThatValue(length, value):
    return(f'{value},' * length)
print(thisLengthThatValue(4,7))



