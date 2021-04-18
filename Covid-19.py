#!/usr/bin/python
#Covid-19 Tracer
#Mr-Robot
from os import system as bodoamat
from time import sleep as waktu
import json
# nge klir
bodoamat("clear")
# nginstall bahan
try:
    import requests
except ImportError:
    print('install his libraries requests first')
    input('[< Press Enter To Install>]')
    bodoamat('pip install requests')
# warna
M = "\033[31;1m"
B = "\033[34;1m"
H = "\033[32;1m"
K = "\033[33;1m"
W = "\033[37;1m"
# nge klir
bodoamat('clear')
iyeu_logo = """{}
\t    ┏━━━┓╋┏┓╋╋┏┳━━━┓╋╋┏┓┏━━━┓
\t    ┃┏━┓┃╋┃┗┓┏┛┣┓┏┓┃╋┏┛┃┃┏━┓┃
\t    ┃┃╋┗╋━┻┓┃┃┏┫┃┃┃┃╋┗┓┃┃┗━┛┃
{}\t    ┃┃╋┏┫┏┓┃┗┛┣┫┃┃┃┣━━┫┃┗━━┓┃
\t    ┃┗━┛┃┗┛┣┓┏┫┣┛┗┛┣━┳┛┗┳━━┛┃
\t    ┗━━━┻━━┛┗┛┗┻━━━┛╋┗━━┻━━━┛
\t\033[37;1m[\033[41;1m created Mr-Robot \033[34;1m|\033[37;1m World of Code \033[00;1m\033[37;1m]
""".format(M,W)
print(iyeu_logo)
j = 0
link = 'https://indonesia-covid-19.mathdro.id/api/provinsi/'
req = requests.get(link)
jeson = json.loads(req.text)
try:
    for data in jeson['data']:
        j += 1
        print('{}['.format(W)+str(j)+']', data['provinsi'])
        print('   {}- {}Positif   :{}'.format(W,K,
   W),data['kasusPosi'])
        print('   {}- {}Sembuh    :{}'.format(W,H,
   W),data['kasusSemb'])
        print('   {}- {}Meninggal :{}'.format(W,M,
   W),data['kasusMeni'])
        print('')
        waktu(0.1)
except KeyboardInterrupt:
    print('')
