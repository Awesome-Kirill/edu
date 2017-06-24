def find_substring(input_str,pre_str):
	out_str = ''
	LEN_INPUT_STR = len(input_str)
	LEN_PRE_STR = len(pre_str)
	for x in range(LEN_INPUT_STR):
		if pre_str == (input_str[x:x+LEN_PRE_STR]):
			out_str = out_str +' '+ str(x)
	if not out_str:
		out_str = -1
	return out_str




input_str = input()
pre_str = input()



print(find_substring(input_str,pre_str))