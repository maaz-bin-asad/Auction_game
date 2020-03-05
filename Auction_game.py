import random
flag=0
i=list()
j=list()
c=str(input(('Please provide your name\n')))
print('Nice to meet you {} '.format(c))
a=int(input('Please Enter upto which you  wish to continue the game\n'))
x=int(input('Make your first call.'))
while True:
	i.append(x)
	y=random.randint(x,x+5)
	j.append(y)
	if y==x+2:
		print('You win the game, You will be  explained the code now')
		flag=1
		break
	else:
		print('Oops! Computer does not want you to win. It called {} .You need to make another call Amigo.'.format(y))
		if x>=a or y>=a:
			break
	x=int(input('Enter next call\n'))
	if x>y:
		continue
	else:
		print('You input wrong entry')
		break
print('\n')
if flag==1:
	print('Game finished')
else:
   print('You lose. The calls have reached the deadline. Never doubt yourself Amigo. This is just a game of chance.')
print('The calls you made contains the values {}'.format(i))