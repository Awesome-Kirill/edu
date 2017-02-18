def markovka(input_str):
    output_dict = {}
    for x in input_str.lower().split(' '):
        if x in output_dict:
            output_dict[x] +=1
        else:
            output_dict[x] = 1

    for x in output_dict:
        print('{} {}'.format(x, output_dict[x]))


input_str_0 = str(input())
markovka(input_str_0)
