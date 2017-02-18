def get_str(lst, num):
	return_str = ''
	for index, x in enumerate(lst):
		if x == num:
			return_str += str(index)

	return return_str if return_str else 'Отсутствует'




test_sr = input()
num = int(input())


output_lst = [int(s) for s in test_sr.split()]






print(get_str(output_lst, num))
