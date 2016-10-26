#bin/python
#Written by @yassergersy
#generate valid email aliases for multi registeration with single email
#Original at https://gist.github.com/YasserGersy/29f195c0e1506b867f3e1914b1098d91
import os,sys

def PlusFactorial(num):
	# 4 + 3 + 2 + 1
	res=0
	while num !=0:
		res=res+num
		num=num-1
	return res
def DotMe(s,donottrim):
	i=(s[0] if  len(s)>0 else '')
	e=(s[-1] if len(s)>2 else '')
	mid=(s[1:] if len(s)>1 else'')
	if len(mid)>1:
		mid=mid[0:len(mid)-1]  
	res='.'
	for i2 in range(0,len(mid)+1):
		res=res+'.'+(mid[i2] if len(mid) >i2 else '')
	res='.'+i+res+e
	if donottrim ==False: #remove first char if =dot also last one
		r=res
		while  res.startswith('.'):
			res=res[1:]
		while  res.endswith('.'):
			res=res[0:len(res)-1]
	while '..' in res:
		res=res.replace('..','.')
	return res
def generate(userinp,id,adrs):
	_list=[]

	REC=-1
	stx=''

	for REC in range(len(id)-1):
	#	print('\n--------------------------'+str(REC)+' of '+str(len(id)-1)+'------['+id+']-------------------')
		REC=REC+1
		start=DotMe(id[0:REC],False).upper()
		end=id[REC:]
		nst=start
		nend=end
		for i in range(0,len(end)+1):
			t=nst+'.'+nend+adrs#+DotMe(middle,True)+end+adrs
			t=t.lower()
			if t not in _list:
				_list.append(t)
				stx=stx+t+'\n'
			if len(nend)>1:
				nst=nst+nend[0]
				nend=nend[1:]
		if len(end) > 1:
			start=start+end[0]
			end=end[1:]
	return _list,stx
	#	print(_list)

#exit()
if __name__=='__main__':
	userinp=''
	if len(sys.argv) >1:
		userinp=sys.argv[1]
	else:
		userinp=raw_input('What is your email address?: ')

	while userinp.startswith("'") or userinp.startswith('"'):
		userinp=userinp[1:]

	while userinp.endswith('"') or userinp.endswith("'"):
		userinp=userinp[0:len(userinp)-1]

	if '@' not in userinp:
		exit('[-] Error: invalid email \n Leaving ......... ')
	arr=userinp.split('@')
	id=arr[0].strip()
	adrs='@'+arr[1]

	_list,stx=generate(userinp,id,adrs)
	print '-------------------------------------------'
	print '	Result of ['+userinp+'] = '+str(len(_list))+'/ '+str(PlusFactorial(len(id)-1))+'\n-------------------------------------------\n\n'+stx#_list
	print '-------------------------------------------'
	if len(sys.argv) > 2:
		Output=sys.argv[2].lower()
		if (Output=='o' or Output =='-o') and len(sys.argv)>3:
			Output=sys.argv[3]
		strm=open(Output,'w')
		strm.write(stx)
		print('	[+]  Saved to : '+Output)
		print '-------------------------------------------'

