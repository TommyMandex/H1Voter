#!/bin/python

import requests,os,urllib,sys,datetime,time
requests.packages.urllib3.disable_warnings()

forceVote=True
#Reg 0 : 1250
#unconfirmed 770 : 790

def DetectCloudFlare(r):
	if 'px;">DDoS protection by CloudFlare</a>' in r:
		return True
	return False
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


proxyDict = { "http"  : "http://127.0.0.1:8080", "https" : "https://127.0.0.1:8080",   "ftp"   : "ftp://127.0.0.1:8080"}



def extract_csrf_tok_from_json(body):
	try:
		xz=body.split('"')
		return xz[3].strip()			
	except Exception,o:
			return ""
def log (msg):
	fil1=str(datetime.datetime.now().time()).replace(':','.')+'.txt'
	fil ='errors/'+fil1.replace(' ','-')
	strm=open(fil,'w')
	strm.write(msg)
	strm.close()
	raw_input('\nError ['+fil1+']\n Press Enter to continue\n')

def extract_sess_from_Cookie(cok):
	try:
		v=cok.split('__Host-session')
		x=v[1].split(';')
		nb=x[0][1:]
		nb='__Host-session='+nb+';'
		return nb		
	except Exception,o:
			return ""


def returnresponseMSG(r):
	res=str(r.status_code)+' '+str(r.reason)
	for i, j in sorted(r.headers.items(), key=lambda x: x[0].lower()): 
		res = res +i+': '+j+'\n'
	res = res +'\n'+r.text
	return res



def _init_():
	#------Script vars---#
	global ids,startindex,passwords,idsPath,reports,reports_string,userAgentH,votes,acceptH,AcceptLanguageH,xreqwith,conttypeH,url6,url5,url4,url3,url2,url1,hostsession,csrf_token_header_name,csrf_value
	ids =[]
	passwords=[]
	idsPath=''
	reports_string=''
	reports=[]
	votes=10
	#-----Headers-------#
	userAgentH='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:47.0) Gecko/20100101 Firefox/47.0'
	acceptH='text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
	AcceptLanguageH='en-US,en;q=0.5'
	xreqwith='XMLHttpRequest'
	conttypeH='application/x-www-form-urlencoded; charset=UTF-8'
	#-------Req--------#
	url1='https://hackerone.com/users/sign_in'          #get
	url2='https://hackerone.com/current_user'           #get
	url3='https://hackerone.com/sessions'               #POST
	url4='https://hackerone.com/users/sign_in'          #POST
	url5='https://hackerone.com/current_user'           #get
	url6='https://hackerone.com//reports/<repid>/votes' #POST
	hostsession=''
	csrf_token_header_name='X-CSRF-Token'
	csrf_value=''
	startindex=0
	if os.path.isdir('errors') is False:
		os.system('mkdir errors')
	
def leavewithnotexistedfile():
	print(stx.RED+"The file you entered is not found 404 :D"+stx.Green)
	exit()
def leaveusage():
	if len(sys.argv) > 1:	
		if sys.argv[1] == 'download':
			trydownload(True)
	else :
		print(stx.RED+"""+
		+Usage python voter.py  file.txt   <ids>        votesCount
		       python voter.py  list.txt 158872,154325    20 
								 """+stx.Green+"'add many reports separated by comma'\n type 'python voter.py download' to get list of bots """+stx.Green)
	exit()
def downloadlist():
	urlpasswords='https://gist.githubusercontent.com/YasserGersy/8f1a4713c5c02c64b4106471f3917972/raw/91da23cfbe754163f00d188a057b083dd2f2c00d/H1_Bots.txt'
	reqdone=False
	while reqdone==False:#
		req=requests.get(url=urlpasswords,allow_redirects=False)
		reqdone=True
		if DetectCloudFlare(req.text):
			reqdone=False
			print('Sleeping for cloud flare')
			time.sleep(5)
	if 'yopmail' in req.text:
		strm=open('list.txt','w')
		strm.write(req.text)
		lines=req.text.split('\n')
		print('['+str(len(lines))+'] Ids Downloaded successfully')
	else:
		print('failed to download')
		exit()
def trydownload(force):
	global idsPath
	idsPath='list.txt'
	if os.path.isfile(idsPath) is False:
		downloadlist()
	else:
		with open(idsPath) as xb:
			if force is False:
				if len(xb.readlines()) < 2 :
					print('Empty file')
					force=True
		if force is True:
					downloadlist()

def load():
	global idsPath,votes,ids,reports,reports_string,ids,passwords,votes,startindex
	#python voter.py list 3,3,4,5 66 100
	votes=1
	if len(sys.argv) < 4:
		leaveusage()
	else:
		idsPath=sys.argv[1]
		if os.path.isfile(idsPath) is False :
		    if 'download' != idsPath :
		    	leavewithnotexistedfile()
		    else:
		    	trydownload(False)
		
		reports_string=sys.argv[2]
		del reports[:]
		if ',' in reports_string:
			treps=reports_string.split(',')
			for t in treps:
				ne=t.strip()
				if ne.startswith('#'):
					continue
				if len(ne) > 4:
					reports.append(ne)
		else:
			reports.append(reports_string.strip())
		votes=sys.argv[3]
		try:  
			votes=int(votes)

			if votes<1:
				print('Minimum value for voting is 0')
				votes=1

		except Exception, e:
			if votes=='max':
				votes=10000000
			else:
				print(stx.RED+"invalid number for votes ["+str(votes)+"]"+stx.Green)
				exit()
		
		if len(sys.argv) >4:
			tmpind=sys.argv[4]
			try:
				startindex=tmpind
			except Exception,v:
				startindex=0
				print('\n Start index=0 as default')

	print '_____________________________________________________\n'
	os.system('clear')
	print stx.Blue+"""
  _________________________________________________________________________________
 |::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
 |:##::::'##::::'##::::::::::::'##::::'##::'#######::'########:'########:'########::
 |:##:::: ##::'####:::::::::::: ##:::: ##:'##.... ##:... ##..:: ##.....:: ##.... ##:
 |:##:::: ##::.. ##:::::::::::: ##:::: ##: ##:::: ##:::: ##:::: ##::::::: ##:::: ##:
 |:#########:::: ##:::::::::::: ##:::: ##: ##:::: ##:::: ##:::: ######::: ########::
 |:##.... ##:::: ##::::::::::::. ##:: ##:: ##:::: ##:::: ##:::: ##...:::: ##.. ##:::
 |:##:::: ##:::: ##:::::::::::::. ## ##::: ##:::: ##:::: ##:::: ##::::::: ##::. ##::
 |:##:::: ##::'######:'#######:::. ###::::. #######::::: ##:::: ########: ##:::. ##:
 |..:::::..:::......::.......:::::...::::::.......::::::..:::::........::..:::::..::
 |::::::::::::::::::::::::"""+stx.Green+"Increase your reports popularity"+stx.Blue+"""..::........::..:::::...::
 |::::::::::::::::::::::::::::::::"""+stx.RED+"By"+stx.yel+""" Yasser Gersy 2016"""+stx.Blue+"""..::........::..:::::...::..::
 |::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
"""
	print(stx.yel+stx.lin+"Started at         [ "+str(datetime.datetime.now())+" ]")
	print("Reports to Vote on [ "+reports_string+" ]")
	print("Accounts  file     [ "+idsPath+' ]')
	print("Starting from      ["+str(startindex) +"]")
	print("Requested Voted    ["+str(votes)+"]")
	print '\n'
	h=0

	with open(idsPath) as strm:
		lines=strm.readlines()
		del ids[:]
		del passwords[:]		
		for l in lines:
			if ':' in l :
				if l.startswith('#'):
					h=h+1
					continue
				else:
					tempids=l.split(':')
					ids.append(tempids[0].strip())
					passwords.append(tempids[1].strip())
	

	if len(ids) < votes :
		votes=len(ids)
	startindex=int(startindex)
	print(stx.Blue+"Loading accounts.....")
	print("Found accounts :"+str(len(ids)))
	if len(ids) <1 :
		print(stx.RED+'\n 	The file does not have any valid accounts'+stx.Green)
		if h >0: 
			print('		Ignored accountes = '+str(h)+stx.yel)
		exit()

def _exec_():
	
	global url1,url2,url3,url4,url5,url6,ids,passwords,userAgentH,acceptH,AcceptLanguageH,xreqwith,conttypeH,hostsession,csrf_value,csrf_token_header_name,reports,votes
	#Checking ids 
	h={"User-Agent":userAgentH,"Accept":acceptH,"Accept-Language":AcceptLanguageH}
	validreports=[]		
	reportsTitles=[]
	invalidIds=[]
	done=[]
	print stx.Green+'\nChecking ids ....'
	for uid in reports:
		reporturl='https://hackerone.com/reports/'+str(uid)
		
		reqdone=False
		while reqdone==False:#
			rep_req=requests.get(reporturl,headers=h,allow_redirects=False)#,proxies=proxyDict)
			reqdone=True
			if DetectCloudFlare(rep_req.text):
				reqdone=False
				print('Sleeping for cloud flare')
				time.sleep(5)

		
		if rep_req.status_code ==200 or forceVote:
			if uid not in validreports or forceVote:
				validreports.append(uid)
				done.append(0)
				tit=''
				if len(rep_req.text ) > 350 :
					f = rep_req.text.split('<meta property="og:title" content=')
					try:	
						 if 'disclosed on HackerOne' in f[1]:
						 	
						 	f5=f[1].split(':')[1].split('"/>')[0]
						 	reportsTitles.append(f5[:-25])
						 	vn=stx.Blue
						 	if len(reportsTitles) % 2==0:
					 			vn=stx.Green

						 	print (vn+'['+uid+'] ['+reportsTitles[len(reportsTitles)-1]+']')
					except Exception:
						some=2
		else :
			print stx.yel+'['+uid+'] is '+stx.RED+'invalid or not available '+stx.yel+'yet\n'+stx.yel
	reports=validreports
	if len(reports) < 1:
		print(stx.RED+'No valid/public reports to vote on\n Leaving..'+stx.White)
		exit()
	

	#0Voting Process00000
	requestedvotes=votes
	_break_=False
	onevotesend=False
	if requestedvotes < 1 :
		print "Minimum value=1"
		requestedvotes=1
	for c in range(startindex,len(ids)):
		for ddone in done:
			if ddone >= requestedvotes:
				_break_result=True
		if _break_ is True:
			bc=0										  
			print stx.yel+'\n--------------------Voting Results ---------------------------'+stx.Green
			for d in done:
				liner=stx.Green
				if bc % 2==0:
					liner=stx.Blue
				print( liner+"-----["+str(done[bc])+"]   ("+str(done[bc])+")--Votes sent to ["+reports[bc]+"]----------")
				bc=bc+1
			break
		time.sleep(3)
		alldone=0
		counter=c
		while alldone==0:
			alldone=1
			hostsession=csrf_value=''
			
			s1=requests.session()
			s1.headers.update({"User-Agent":userAgentH,"Accept":acceptH,"Accept-Language":AcceptLanguageH})
			
			reqdonex=False
			while reqdonex==False:#
				r1=s1.get(url1) 
				reqdonex=True
				if DetectCloudFlare(r1.text):
					reqdonex=False
					print('Sleeping for cloud flare')
					time.sleep(5)

			
			
			cok=r1.headers['Set-Cookie']
			hostsession=extract_sess_from_Cookie(cok)
			if hostsession == '':
				log(url1)
			print (stx.brown+stx.lin+'['+str(counter)+'] ['+str(done)+'] \n[A]-Requesting sign in ..... ')####################

			s2=requests.session()
			s2.headers.update({"User-Agent":userAgentH,"Accept":acceptH,"Accept-Language":AcceptLanguageH,'X-Requested-With':xreqwith,'Cookie':hostsession})
			

			reqdonex=False
			while reqdonex==False:#:
				r2=s2.get(url2)
				reqdonex=True
				if DetectCloudFlare(r2.text):
					reqdonex=False
					print('Sleeping for cloud flare')
					time.sleep(5)


			cok2=r2.headers['Set-Cookie']
			hostsession=extract_sess_from_Cookie(cok2)
			csrf_value=extract_csrf_tok_from_json(r2.text)
			print(stx.brown+'[B] +-Getting CSRF token ...')############
	
			
			print stx.RED+'[c] --------[Login with "'+stx.magenta+ids[counter]+stx.RED+'" ]------------'
			h3={"User-Agent":userAgentH,"Accept":acceptH,"Accept-Language":AcceptLanguageH,'X-Requested-With':xreqwith,csrf_token_header_name:csrf_value,'Content-Type':conttypeH,'Cookie':hostsession}
			body3={'email':ids[counter],'password':passwords[counter],'remember_me':'false'}
			bodyStr3=urllib.urlencode(body3)
	
			r3done=0
			while r3done==0:
				r3done=1+r3done
				
			reqdonex=False
			while reqdonex==False:#:
				r3=requests.post(url=url3,data=bodyStr3,headers=h3)
				reqdonex=True
				if DetectCloudFlare(r3.text):
					reqdonex=False
					print('Sleeping for cloud flare')
					time.sleep(5)


				cok3=r3.headers['Set-Cookie']			
				hostsession=extract_sess_from_Cookie(cok3)


				st3='	  Checking Credits: '
				vres=stx.RED+'Error'
				if 'result_code":"valid-credentials' in r3.text:	
					vres=stx.Green+'Valid Credetnitals'+stx.RED		
					print(st3+' :['+vres+']')
				else:
					msg=''
					if 'invalid-credentials' in r3.text:
						print(st3+'invalid credentials for ['+ids[counter]+':'+passwords[counter])
						vres='invalid'
					elif 'Retry later' in r3.text:
						print(st3+'\n         Firewall detected us :( Retry later)  in 30 seconds ')
						time.sleep(30)
						r3done=0
					else:			
						msg=returnresponseMSG(r3)
						log(msg)
						print(st3+' :['+vres+']')


	
			h4={"User-Agent":userAgentH,"Accept":acceptH,"Accept-Language":AcceptLanguageH,'X-CSRF-Token':csrf_value,'Content-Type':conttypeH,'Referer':'https://hackerone.com/login',	    'Cookie':hostsession}
			body4={'authenticity_token':csrf_value,'user[email]':ids[counter],'user[password]':passwords[counter]}
			bodyStr4=urllib.urlencode(body4)
	
			reqdonex=False
			while reqdonex==False:#:
				r4=requests.post(url=url4,data=bodyStr4,headers=h4,allow_redirects=False)
				reqdonex=True
				if DetectCloudFlare(r4.text):
					reqdonex=False
					print('Sleeping for cloud flare')
					time.sleep(5)


			cok4=r4.headers['Set-Cookie']
			hostsession=extract_sess_from_Cookie(cok4)
			if 'm/hacktivity">redirected' in r4.text:
				print(stx.yel+'[D]   +Initiating session : [Initiated successfully]'+stx.Green)
			else:
				print(stx.yel+'[D]   +Initiating session : [Failed]'+stx.Green)



			h5={"User-Agent":userAgentH,'x-requested-with': 'XMLHttpRequest',"Accept":acceptH,"Accept-Language":AcceptLanguageH,'X-CSRF-Token':csrf_value,'Content-Type':conttypeH,'Referer':'https://hackerone.com/login',	    'Cookie':hostsession}
			
			reqdonex=False
			while reqdonex==False:#:
				r5=requests.get(url=url5,headers=h5,allow_redirects=False)##,proxies=proxyDict)
				reqdonex=True
				if DetectCloudFlare(r5.text):
					reqdonex=False
					print('Sleeping for cloud flare')
					time.sleep(5)

			csrf_value=extract_csrf_tok_from_json(r5.text)
			st =   '[E]   +Requesting New Token:'
			if '{"csrf_token":"' in r5.text:
				print( st+stx.Green+"[ Received ]     ["+str(len(csrf_value))+"]")
			else:
				print(stx.Green+st+stx.RED+" [Failed] "+stx.Green)


			h6={"User-Agent":userAgentH,'x-requested-with': 'XMLHttpRequest',"Accept":acceptH,"Accept-Language":AcceptLanguageH,'X-CSRF-Token':csrf_value,'Content-Type':conttypeH,'Referer':'https://hackerone.com/login',	    'Cookie':hostsession}
			repcounter=-1


			breakreports=False
			for repid in reports:
				repcounter=repcounter+1
				urlfinal='https://hackerone.com/reports/'+str(repid)+'/votes'
				
			reqdonex=False
			while reqdonex==False:#:
				r6=requests.post(url=urlfinal,headers=h6,allow_redirects=False)##,proxies=proxyDict)
				reqdonex=True
				if DetectCloudFlare(r5.text):
					reqdonex=False
					print('Sleeping for cloud flare')
					time.sleep(5)

				temp=r6.text
				justf=''
				indxer='['+str(repcounter+1)+']'
				if len(reports) <2:
					indxer=''
				if repcounter<1:				
					justf='[F]'
				if '{"vote_id":' in temp:
					print(stx.Blue+justf+'     ['+indxer+']  +Voting result : '+stx.Green+'[Voting on '+str(repid)+' Succeeded]')
					onevotesend=True
					done[repcounter] =done[repcounter]+1
				elif '{"report":["user already voted"]}' in temp:
						print(stx.Blue+justf+'     '+indxer+'  +Voting result : '+stx.magenta+'[Already voted before on '+str(repid)+']')
				elif '{"status":"404","error":"Not Found"}' in temp:
					print(stx.Blue+justf+'     '+indxer+' +Voting result : Unavailable report ['+str(repid)+']')

				else:
					print(stx.White+justf+" "+indxer+" +Voting on "+str(repid)+stx.RED+"[ Failed ] "+stx.Green)
					invalidIds.append(ids[counter])
					alldone=0
					breakreports=True
					counter=counter+1
					break
					#log(returnresponseMSG(r6))
			#if breakreports is False:
				
	if onevotesend is False:
		print(stx.RED+'\nNo Votes made')
	if len(invalidIds) > 0 :
		print(stx.yel+'Invalid ids ',invalidIds)




if __name__=='__main__':
	_init_()
	load()
	_exec_()
	print stx.Green+'--------------------------------------------------'
	