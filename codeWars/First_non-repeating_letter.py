#https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
def first_non_repeating_letter(string):
    new_test_str = string.lower()
    test_arr = list(new_test_str)
    for x in string:
        if test_arr.count(x.lower())<=1:
            return x

    return ""
