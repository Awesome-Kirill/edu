#https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
def reverse_words(str):
    return_str = ''
    for x in str.split(' '):
        return_str+=x[::-1]+' '
    return return_str[:-1]
