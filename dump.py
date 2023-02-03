import os, sys, rich
import requests,random
from rich.panel import Panel as nel
from rich import print as cetak
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
##### INDICATION ######
tokenku = []
uid = []
id = []
loop = 0
append = []
##### WARNA WARNA INDAH #####
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
Ip = requests.get("http://ip-api.com/json/").json()["query"]
negara = requests.get("http://ip-api.com/json/").json()["country"]
##### DEF LOGIN LOGIN #####
def login():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			print('Internet Anda Sedang Sibuk/Tidak Ada')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	os.system('clear')
	try:
		ses = requests.Session()
		logo()
		print('='*51)
		cookie = input('\nMasukan Cookie : ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open(".tok.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		print('\nLogin Berhasil bre ')
		login()
	except Exception as e:
		print(" Cookies Invalid bro")
		os.system('rm -rf .tok.txt && rm -rf .cok.txt')
		print(e)
		exit()
def logo():
     print(f'''  {P}  ____    __  __    __  ___    ____            ____    ____ 
   / __ \  / / / /   /  |/  /   / __ \          /  _/   / __ \
 
  / / / / / / / /   / /|_/ /   / /_/ /          / /    / / / /
 / /_/ / / /_/ /   / /  / /   / ____/         _/ /    / /_/ / 
/_____/  \____/   /_/  /_/   /_/             /___/   /_____/  

({P}DI BUAT OLEH {H}KALL - XR{P})''')
##### DEF MENU MENU DUMP ######
def menu(name,uid):
    os.system('clear')
    logo()
    print('='*51)
    print(f'Nama    : {name}')
    print(f'Id anda : {uid}')
    print(f'Ip Anda : {Ip} ')
    print(f'Ip Anda : {negara} ')
    print('='*51)
    print(f'{P}1.Dump Id Publik\n2.Dump Id Dari Followers\n3.Keluar {M}LogOut{P}')
    print('='*51)
    ica = input(f'{P}Pilih : ')
    if ica in ['1']:dump_publik()
    elif ica in['2']:dump_follow()
    elif ica in['3']:os.system('rm -rf .tok.txt && rm -rf .cok.txt')
    print(f'{H}SELAMAT JALAN MAS BRO SEMOGA TENANG DI SANA')
    
###### META DUMP DUMP ######
def dump_publik():		
	try:
		os.mkdir('dump')
	except:pass
	try:
		xaco = input(f"{P}id public  :\x1b[38;5;46m ")
		cuy = input(f"{P}nama file  :\x1b[38;5;46m ")
		print("")
		wkwk  = ('DUMP/' + cuy + '.txt').replace(' ', '_')
		xxx = open(wkwk, 'w')
		token = open('.tok.txt','r').read()
		cookie = open('.cok.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(xaco,token),cookies=coki).json()
		for fuck in cyna['friends']['data']:
			id.append(fuck['id']+'|'+fuck['name'])
			xxx.write(fuck['id']+'|'+fuck['name'] + '\n')
			sys.stdout.write(f'\r\033[0m   %s {H}•--->\033[0m%s                  \r\n\x1b[38;5;231m [ \x1b[38;5;46m%s\x1b[38;5;231m ] [ \x1b[38;5;46m%s\x1b[38;5;231m ] \x1b[0;96mSEDANG DUMP.'%(fuck['id'],fuck['name'],datetime.datetime.now().strftime('%H:%M:%S'), len(id)
			)); sys.stdout.flush()
			time.sleep(0.0050)
			
		xxx.close()
		print(f"\nberhasil dump id dari publik");print(f"salin output file + [ %s%s%s ]"%(H,wkwk,P))
		input(f" kembali ")
		back()
	except (KeyError,IOError):
		os.remove(wkwk)
		print(f"gagal dump id, kemungkinan id tidak ada.\n")
		input(f" kembali ")
		back()
##### META FOLLOWRS ######
def dump_follow():
	print(f'{H}MAAF FITUR INI MASIH EROR JADI SAYA HAPUS DULU TUNGGU UPDATE SELANJUTNYA ')
	input('ENTER')
	login()
if __name__=='__main__':
	try:os.mkdir('DUMP')
	except:pass
	login()	