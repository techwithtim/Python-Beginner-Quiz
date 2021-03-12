# Q1
# Determine the evaluation of each expression
v = 12 % 5
w = 2 * 3 + 2
x = 'a' < 'b' 
y = 'a' < 'a'
z = 1 == True

# Q2
# Determine the evaluation of each expression
a = 6 ** 2
b = (5 % 2) ** 2
c = str(234) + "5"
d = a // b

# Q3
# Determine the value of variable q3 at each line
q3 = 10
q3 += 5
q3 -= 10
q3 *= 2
q3 = str(q3)
q3 += "1"

# Q4 
# Determine the output of the program
x = 1
while x:
	print(x)
	x += 1
	if x < 5:
		break

# Q5 
# Determine the output of the program
answer = 10
if answer < 10:
	print("less than")
elif answer > 5:
	print("greater than")
else:
	print("run")

# Q6 
# Determine the output of the program
answer = 10
if answer < 10:
	print("less than")
else:
	print("run")

if answer > 5:
	print("greater than")
elif answer == 10:
	print('10')


# Q7
# Determine the output of the program
y = 25
x = y + 5
z = y - x
print(x)

# Q8 
# Determine the output of the program
d = {}
d['tim'] = 5
d['joe'] = 6
del d['joe']
d[6] = 'joe'
d[5] = 'tim'
print(d['tim'])
print(d[6])

# Q9
# Determine the output of the program
x = True
y = False
z = True
ans = x and y and z or x
print(ans)

# Q10
# Determine which of the following expressions is the same as q10
# b1, b2 and b3 are boolean values
q10 = not (b1 or b2) and not (b3 and b1)

# Pick from the following options
a = (not b1 and not b2) or not (b3 or b1)
b = (b1 or b2) or (b3 and b1)
c = (b1 or b2) and (b3 and b1)
d = (not b1 and not b2) and (not b3 and not b1)

# Q11
# Determine the output of the program
lst = [1, 2, 3, 4, 5, 6]
print(lst[::2])
print(lst[::-1])
print(lst[1:2])
print(lst[2])
print(lst[-1])

# Q12
# Determine the output of the program
lst = (1, 2, 3, 4, 5, 6)
print(lst[::2])
print(lst[::-1])
print(lst[1:2])
print(lst[2])
print(lst[-1])

# Q13
# Does the following code produce an error, if so why?
lst = (1, 2, 3, 4, 5, 6)
lst[2] = 3

# Q14
# Does the following code produce an error, if so why?
lst = [1, 2, 3, 4, 5, 6]
lst[2] = 3

# Q15
# Does the following code produce an error, if so why?
lst = [1, 2, 3, 4, 5, 6]
lst[6] = 3

# Q16
# Determine the output of the following program
x = "tim, yes, no"
print(x.split())
print(x.split(","))

# Q17
# Determine the output of the following program
x = "aabbccddeeFEFaaA"
print(x.count('a'))

# Q18
# Determine the output of the following program
x = "aabbccddeeFEFaaA"
y = x.split('a')
print(','.join(y))

# Q19
# Determine the output of the following program
x = [1, 2, 3]
print(','.join(str(x)))

# Q20
# Determine the output of the following program
x = [False, 0, 1, True]
x[:2] = x[1:3]
print(x)

# Q21
# Determine the output of the following program
x = []
y = x
print(x is y)
print(id(x) == id(y))
y = []
print(x is y)
print(id(x) == id(y))
x = y
x.append(1)
print(x)
print(y)

# Q22
# Determine the output of the following program
for i in range(1, 10, 2):
	print(i)

# Q23
# Determine the output of the following program
total = 0
last = -1
for i in range(0, 100):
	total += int(i % 2 == 0)
	if i < 5:
		last = i

print(total, last)

# Q24
# Determine the output of the following program
numbers = [10, 20, 30, 40, 50, -10]
for num in numbers:
	print(num)

# Q25
# Determine the output of the following program
lst = ['tim', 'is', 'really', 'great']
for a, b in enumerate(lst):
	print(a, end=" | ")
	print(b)
	b = 5

# Q26
# Determine the output of the following program
numbers = [10, 20, 30, 40, 50, -10]
for num in range(len(numbers)):
	print(numbers)

# Q27
# Determine the output of the following program
numbers = [10, 20, 30, 40, 50, -10]
for num in range(len(numbers)):
	print(num)

# Q28
# Determine the output of the following program
numbers = [10, 20, 30, 40, 50, -10]
for i in range(len(numbers)):
	numbers[i], numbers[-i] = numbers[-i], numbers[i]

print(numbers)

# Q29
# Determine the output of the following program
a = []
b = 10
c = 5
for i in range(b):
	a.append([])
	for j in range(c):
		a[i].append(j)

print(a)

# Q30
# Determine the output of the following program
a = []
b = 5
c = 4
for i in range(b):
	a.append([])
	for j in range(c):
		a[i].append(j)
		if j % 2 == 1:
			a[i].append([])

print(a)