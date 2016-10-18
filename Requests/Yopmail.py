# GET /en/mail.php?b=marten0mickos&id=me_ZGLjBGN2ZGRkAmH3ZQNjAQNmAGVmBD== HTTP/1.1
# Host: www.yopmail.com
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:48.0) Gecko/20100101 Firefox/48.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate
# Referer: http://www.yopmail.com/en/
# Cookie: tc=1; localtime=15:17; params=0.0; yc=JAGD0AwD4AwR4AQRkAmxkZD; compte=marten0mickos%3Amrrexceptionbot924%3Amrrexceptionbot923%3Amrrexceptionbot922%3Amrrexceptionbot921%3Amrrexceptionbot920%3Amrrexceptionbot919%3Amrrexceptionbot918%3Alimit%3Almit; _ga=GA1.2.1490717603.1469751514; ys=CBGRlZQV2ZmZkBGDjAwN5Aj; tc=1; _gat=1; PHPSESSID=tkn2fcge7r6uij0o0m1sji8qv4
# Connection: close
# Upgrade-Insecure-Requests: 1
#710233
#1199677

import requests,os
requests.packages.urllib3.disable_warnings()
proxyDict = { "http"  : "http://127.0.0.1:8080", "https" : "https://127.0.0.1:8080",   "ftp"   : "ftp://127.0.0.1:8080"}
example='https://hackerone.com/users/confirmation?confirmation_token=wKwLzpZz-dbqJdYcsFLf'
h={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:48.0) Gecko/20100101 Firefox/48.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Referer": "http://www.yopmail.com/en/",
"Cookie": "tc=1; localtime=15:17; params=0.0; yc=JAGD0AwD4AwR4AQRkAmxkZD; compte=marten0mickos%3Amrrexceptionbot924%3Amrrexceptionbot923%3Amrrexceptionbot922%3Amrrexceptionbot921%3Amrrexceptionbot920%3Amrrexceptionbot919%3Amrrexceptionbot918%3Alimit%3Almit; _ga=GA1.2.1490717603.1469751514; ys=CBGRlZQV2ZmZkBGDjAwN5Aj; tc=1; _gat=1; PHPSESSID=tkn2fcge7r6uij0o0m1sji8qv4",
"Upgrade-Insecure-Requests": "1"
}
id="xgersy0"

url='http://www.yopmail.com/en/mail.php?b='+id+'&id=me_ZGLjBGN2ZGRkAmH3ZQNjAQNmAGVmBD=='
r =requests.get(url=url,headers=h,proxies=proxyDict)

if 'Mail not found' in r.text:
	print('No inbox for '+id)
elif 'href="mail.php?b='+id in r.text:
	x=r.text.split('<a class="button button--success" href="')
	c=x[1].split('"')
	activurl=c[0]
	raw_input(activurl)
	r2=requests.get(url=activurl,proxies=proxyDict)
	if 'Resend confirmation instructions' in r2.text:
		print'expired or activated already'

