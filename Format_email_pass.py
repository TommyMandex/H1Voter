#this script converts file with the following format
#email@gmail.com
#Email@usa.com
#email@egymail.com
#
#to the following format
#
#email@gmail.com:custompassword
#Email@usa.com:custompassword
#email@egymail.com:custompassword

import os

promptonce=False
fileExist=False
fil=''
while fileExist==False:
	if promptonce==False:
		fil=raw_input('Where is the emails File : ')
		promptonce=True
	else:
		fil=raw_input('Invalid file or non existed \n insert again :')
	if os.path.isfile(fil):
		fileExist=True
		break

passdone=False
while passdone==False:
	ps=raw_input('\n What is your passowrd ex "123!@#qweQWE"')
	if len(ps)==0:
		ps='123!@#qweQWE'
		print('Your password set to '+ps+'\n\n')
	if len(ps)>7:
		break

data=''
count=0
with open(fil) as read:
	lines=read.readlines()
	if len(lines) < 1:
		print('Empty file \n leaving ...')
		exit(0)
	for ls in lines:
		l=ls.strip()
		if len(l)<3:
			continue
		data=data+l+':'+ps+'\n'
		count=count+1
if len(data) < 3 :
	print('Empty lines')
osx=open('result.txt','w')
osx.write(data)
osx.close()

print('Saved to result.txt '+str(count))