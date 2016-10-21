import requests
import datetime,time,os
import time
import random, string

debugmode=False
requests.packages.urllib3.disable_warnings()



def randomNumber(l):
	s=string.digits
	return ''.join(random.sample(s,l))

def randomstr(l):
	s=string.digits+string.lowercase+string.uppercase
	return ''.join(random.sample(s,l))


os.system('rm -rf errors')
class stx:    
	RED='\033[1;31m'
	brown='\033[0;33m'
	Blue='\033[0;34m'
	Green='\033[1;32m'    
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	yel = '\033[93m'
	White='\033[1;37m'
	crims=' \033[1;38m'
	magenta='\033[1;35m'									
	lin='\n---------------------------------------------------------------------------------\n'
randomNames=['hany_ramzy','adel_emam','ghada_abdel_razek','youssra','Abla_kamel','Mona_zaki','abu_trika','hossam_hassan','mofeed_fawzy','samira_sa3eed','Hend_rostom','sara_jay','anjelica','sophie_dee','maysa','mamdooh','bill_gates','Abd_elfattah','taha_hussien','john','levis','brad','max','haven','tapol','lexi','sam','michil','henry','chris','frank','jobert','steven','dep','smith','franklein','zak','josef','merlin','donald','barak','adel','sarah','taison','fawzya','nermeen','hend','zakaria','yasser','emad']
#Testing only
proxyDict = { "http"  : "http://127.0.0.1:8080", "https" : "https://127.0.0.1:8080",   "ftp"   : "ftp://127.0.0.1:8080"}
cokstr="__cfduid=d1cdfc0b504bd870dc94c5509a2f41bd71472917466; _ga=GA1.2.1635264352.1472917475; __Host-session=anhEcDkzOVVwYWxDL2pVSTJ3NTZWeHFVUzhTTzVHbDNzK1lQUWl3eG53Q0xyNHdLY3Y5aHJsQnl4VUNtSjI4OWx6bFozRDZDcFBRQVlXdjBsMXpaUEFNR3ZpTFV6c1NVU2s0TnBvMFhVZTAxWEVyUXVQT2FDSExUNjFZQW16UG1IWWlxaE9Zd0h1SFNmKytFWW52eG81N0xqWTh1QW16bS9leThwME1sQXllWE00bHJCN2NqNTlMN3pWckN2eXFULS1qcFJoTW1SSVF6VkVVQXllT1QwUy93PT0%3D--94bd223fffd82f1c61b2d03cc2f0be5ac1f3b93a; _gat=1"
csrft="JSFMAnHPA7fm7d3cQWtmU220kwibz1Ojc/74HYpYx8WJDa/tabBr9JpaeJQJtrc/z3UmTEBO354TZWvyhDuCVA=="
url = 'https://hackerone.com/users'

x=[]
os.system('clear')

print'\n -------------------------------------------------------------------------\n'
print('\n ------------------- Hackerone Bots Maker--------------------------------')
print('\n If you want to generate random bots , just press enter for every prompt ')
print'\n -------------------------------------------------------------------------\n'
f = raw_input(stx.Green+'\nCounter  \nStarting from (ex: 0):')
if len(f)==0:
	f=0
	print('Starting from 0')
else :
	f=int(f)
t=0
donet=False
while donet==False:
	donet=True
	t=raw_input('Emails count (ex: 100 or max) : ')
	if len (t) ==0:
		t=100
		t='max'
		print('count=100')
	elif t.isdigit():
		t=int(t)
	elif t!='max':
		donet=False

validchoice=False
xc=''
ea=''
emailsList=[]
sufx=''
FromFile=False
while  validchoice==False:
	xc=raw_input('\n Choose (1/2)\n1- Random emails\n2-From File\n:')
	if xc.isdigit():
		xc=int(xc)
		validchoice=True
	else:
		validchoice=False

if xc==1:
	FromFile=False
	if t=='max':
		t=100
	name=raw_input(stx.yel+'\nWhat is Your name?: ')
	if len(name) ==0 :
		msx=''.join(random.choice(string.lowercase) for i in range(5))
		name='BotX'+msx+'N'
		print ('Your new name is '+name)
	ea=raw_input(stx.brown+'\nWhere are your emails registered "email domain"?\n (ex: yopmail.com): ')
	if ea.startswith('@'):
		ea=ea[1:]

	if len(ea) ==0:
		ea='yopmail.com'
		print('Email domain set to "'+ea+'"')
	elif '.' not in ea:
		print 'Invalid email domain name\n 		Valid example: "yopmail.com"'
		exit()

	sufx=raw_input('\nIf you want to add sufx type it :')
else:
	FromFile=True
	pathofemails=raw_input('Where is the emails file located ?')
	if os.path.isfile(pathofemails)==False:
		print('non existed file ['+pathofemails+']\nleaving...')
		exit(0)
	else:
		try:
			with open(pathofemails) as reader:
				emailsList=reader.readlines()
			if len(emailsList)<1:
				print('\n empty file \n leaving ...')
				exit()

		except Exception :
			ger=1
	if t=='max' :
		t=len(emailsList)
	elif t> len(emailsList):
		t=len(emailsList)

pas=raw_input(stx.Green+'\nWhat is your New password: ')
if len(pas)==0:
	pas='123!@#qweQWE'
	print ('Password set to "'+pas+'"')
elif len(pas) < 8:
	print(stx.RED+'Password minmum 8 chars ')
	exit()


ty=raw_input(stx.magenta+'\n If you want to add new  cookis \n paste it  , if not press Enter :')
if len(ty) >0:
	cokstr=ty

tys=raw_input(stx.yel+'\n If you want to add new CSRF token \n paste it  , if not press Enter :')
if len(tys) >0:
	csrft=tys

h = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:47.0) Gecko/20100101 Firefox/47.0",
"Accept": "application/json, text/javascript, */*; q=0.01"
,"Accept-Language": "en-US,en;q=0.5"
,"X-CSRF-Token":csrft
,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
,"X-Requested-With": "XMLHttpRequest"
,"Referer": "https://hackerone.com/users/sign_up"
,"Cookie":cokstr 
}

ids=''
end=f+t

print'\n -------------------------------------------------------------------------\n'
print(stx.Blue+'\n 				Starting registeration '+str(f)+':'+str(end)+'\n'+stx.yel)

FroCount=-1
if FromFile and end >= len(emailsList):
	end=len(emailsList)-1
for u in range(f,end):
	FroCount=FroCount+1
	reg=False

	while reg ==False:
		if FromFile:
			compemail=emailsList[u].strip()
			if '@' not in compemail:
				print('invalid email '+compemail)
				break
			else:
				#s=compemail.split('@')[0].strip()
				randint=randomNumber(2)
				randint=int(randint)+5
				while randint >= len(randomNames):
					randint=randint-1
				s=randomNames[randint]+'_'+randomNumber(5)
		else:
			s=name+str(u)+sufx
			compemail=s+'@'+ea

		encodedEmail=((s+'%40'+ea) if FromFile==False else (compemail.strip().replace('@','%40')))
		print(stx.yel+str(FroCount+1)+' Registering with ['+compemail+']'+stx.Green)
		s=s.replace('.','')
		if len(s) > 25:
			s=s[0:25]

		da="user[name]=Egy+Bots&user[username]="+s+"&1=iiiiiiiiiiiiiiiiiiiiiiii&user[email]="+encodedEmail+"&user[password]="+pas+"&user[password_confirmation]="+pas
		noerror=False
		r=''
		while noerror==False:
			noerror=True
			try:	
				if debugmode:
					r =requests.post(url=url,data=da,headers=h,proxies=proxyDict)
				else:
					r =requests.post(url=url,data=da,headers=h)#,proxies=proxyDict)
			except Exception:
				noerror=False
				print('Error ... Retrying again ')
				time.sleep(3)

		usernameemailstatue=''
		if 'been taken' in r.text:
			if 'username'in r.text:
				usernameemailstatue='    Username Reserved ['+s+']  '
			if 'email' in r.text:
				usernameemailstatue = usernameemailstatue+'\n    Email : registered before\n'
			print(stx.RED+usernameemailstatue)
			reg=True
		
		elif  'redirect_path":"/users/sign_in","errors":{}}' in r.text :
			print stx.Green+'Register  succeeded  ['+compemail+"]\n"
			#x.append(s)
			reg =True
			ids=s+'@'+ea+':'+pas+'\n'
		elif 'later' in r.text:
			print stx.RED+'Detected Retring in 5 seconds'
			time.sleep(5)
			reg=False

		elif 'redirect_path":"/users/sign_in","errors":{}}' in r.text:
			print ("invalid password Please enter a strong one ")
			exit()
		elif '8 characters)","does not contain enough entropy. Pick a more secure password' in r.text:
			print('weak password try one like "aAbBcC123!!!"\n') 
			exit()
		else:
			print r.text
	if f!=end:	
		time.sleep(1)
rand=datetime.datetime.now()
path='Bots_'+str(rand)
path=path.replace(' ','').replace(':','').replace('-','').replace('.','')+"_.txt"
strm=open(path,'w')
strm.write(ids)
strm.close()
print('\n\n Saved to '+path)

