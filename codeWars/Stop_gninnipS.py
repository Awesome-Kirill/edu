#https://www.codewars.com/kata/5264d2b162488dc400000001
def spin_words(sentence):
    test_list = []
    for x in sentence.split(' '):
        if len(x)>=5:
            test_list.append(x[::-1])
        else:
            test_list.append(x)
    return ' '.join(test_list)
