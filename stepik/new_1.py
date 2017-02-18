input_str = input()
lst1  = [int(x) for x in input_str.split()]





def test(lst):
	if len(lst) == 1:
		lst[0] = str(lst[0])
		return ''.join(lst)
	else:

		n_lst = 3*lst
		index = len(lst)
		new_lst = [str(n_lst[x-1]+n_lst[x+1]) for x in range(index,2*index)]
		return ' '.join(new_lst)

print(test(lst1))