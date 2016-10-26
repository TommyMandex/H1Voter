

res=''

with open('list.txt') as red:
	lines=red.readlines()
	for l in lines:
		p=l.strip()
		if len(p)<2:
			continue

		if p.startswith('#'):
			x=p
		else:
			p='#'+p
		res=res+p+'\n'

os=open('listx.txt','w')
os.write(res)
		
