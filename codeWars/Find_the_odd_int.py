#https://www.codewars.com/kata/54da5a58ea159efa38000836
def find_it(seq):
    for x in seq:
        if seq.count(x)%2:
            return x
    return None
