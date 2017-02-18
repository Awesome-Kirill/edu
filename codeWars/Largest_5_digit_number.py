#https://www.codewars.com/kata/51675d17e0c1bed195000001
def solution(digits):
    test_lst = []
    for x in range(len(digits)-4):
        test_lst.append(int(digits[0+x:5+x]))
    test_lst.sort()
    return test_lst[-1]
