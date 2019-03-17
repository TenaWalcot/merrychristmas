a=int(input("Please input the size of your Christmas tree:"))
for i in range(1,a):
	for j in range(1,a-i):
		print(' ',end='')
	print('*'*(2*i-1))
b=(2*(a-1)-1)//3
c=((2*(a-1)-1)-b)//2
for i in range(0,b):
	print(' '*b+'*'*c)
d=((a-1)*2-1-15)//2
print(" "*d+"%s %s!\n"%('Merry','Christmas'))
e=((a-1)*2-1-24)/2
input()
