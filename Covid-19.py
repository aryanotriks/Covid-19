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
link = 'https://covid19.mathdro.id/api/countries/'
req = requests.get(link)
jeson = json.loads(req.text)
try:
    for data in jeson['data']:
        j += 1
        print('{}['.format(W)+str(j)+']', data['countries'])
        print('   {}- {}Positive Cases   :{}'.format(W,K,
   W),data['confirmed'])
        print('   {}- {}Recovered Cases  :{}'.format(W,H,
   W),data['recovered'])
        print('   {}- {}Death Cases      :{}'.format(W,M,
   W),data['deaths'])
        print('')
        print('Stay Home Stay Safe')
        print('May Allah Bless All The Muslims Died Due To Covid-19')
        waktu(0.1)
except KeyboardInterrupt:
    print('')
