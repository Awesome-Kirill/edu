test_input = str(input())
sum = 0

for x in test_input.split():
	sum = sum + int(x)

print(sum)