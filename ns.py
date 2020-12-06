#!/usr/bin/python3
#print("give me a bottle of rum!")

import requests,socket,argparse

def arg():
    parse1=argparse.ArgumentParser(description='Simple open port find script ')
    parse1.add_argument('-ip',type=str,default='127.0.0.1',metavar='ip',help='Ip Addres')
    parse1.add_argument('-p',type=int,default=1000,metavar='number of ports',help='Numbers of first ports do you want to scan.default=1000' )
    parse1.add_argument('-sp',type=str,default='', metavar='port',help='Special port do you want to scan.with this parameter other ports do not scan..!')
    arg=parse1.parse_args()
    return arg;

def info(arg_data):
    ip=arg_data.ip
    if len(arg_data.sp)==0:
        ports_ran=range(arg_data.p)
    else:
        ports_ran=int(arg_data.sp)
    return ip,ports_ran;

def main():
    print('''
            [+]Coded_by_Pasindu_Sandeepa
            [@]bombtiktiktik54321.com
                ~CruZerPlayer~
    
    
    ''')
    arg_data=arg()
    ip,port=info(arg_data)

    if str(type(port))=="<class 'int'>":
        sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            sk.connect((ip,port))
        except:
            pass
            print(f'{port} Port closed..!')
        else:
            print(f"[+] {port} Port is open..!")
            sk.close()

    else:
        for aport in port:
            sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            try:
                sk.connect((ip,aport+1))
            except:
                pass
                #print(f'port close {port+1}')
            else:
                print(f"[+] Open port found > {aport+1}")
                sk.close()

if __name__ == "__main__":
    main()    