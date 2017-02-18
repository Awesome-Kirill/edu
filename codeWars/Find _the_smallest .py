#https://www.codewars.com/kata/55a2d7ebe362935a210000b2
def findSmallestInt(arr):

    pre_min = arr[0]
    for x in arr:
        if x < pre_min:
            pre_min = x
    return pre_min
