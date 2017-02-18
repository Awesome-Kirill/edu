
arg_1 = float(input())
operand = input()
arg_2 = float(input())
'''
Поддерживаемые операции: +, -, /, *, mod, pow, div, где 
mod — это взятие остатка от деления, 
pow — возведение в степень, 
div — целочисленное деление.
'''
def calc(arg1,arg2,ope):
	try:
		func_dict = {'+': lambda x, y: x + y, 
			'-': lambda x, y: x-y,
			'/': lambda x, y: x/y,
			'*': lambda x, y: x*y,
			'mod': lambda x, y: x%y,
			'pow': lambda x, y: x**y,
			'div': lambda x,y: x//y
			}

		result=func_dict[ope](arg1,arg2)
		
	except ZeroDivisionError:
		result = 'Деление на 0!'

	except KeyError:
		result = 'Операция не потдерживается'

	finally:
		return result


print(calc(arg_1,arg_2,operand))

input()
