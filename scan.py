#Gunakan Dengan Bijak Cuk , Master Scipt Kiddie ....

import LIST
from LIST.id import *
from LIST.it import *
from LIST.jp import *
from LIST.us import *
from LIST.fr import *
from LIST.kr import *
from LIST.de import *
from LIST.tr import *
import requests,re,os

b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"
cyan = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"

def main():
    os.system('clear')

    print("{} 1î1     1î1        11          1111111  1î1   11 ").format(r)
    print("   1î1     1î1      111111       111       1î1  11  ")
    print("   1î1     1î1     111 1111     111        1î1 11   ")
    print("   1î1111111î1   111     1111  1*1         1î111     ")
    print("   1î1111111î1  111      1111  1*1         1î111     ")  
    print("{} 1î1     1î1  11-1111111-111 111         1î1 111   ").format(w)
    print("   1î1     1î1  1111      1111  11111111   1î1  1111 ")
    print("{} '--------------'----------{}--------------------------.  ").format(r,w)
    print("{} | {}Author  : {}CyberLightning {} | {}INDO{}N{}{}ESIA | ").format(r,w,r,w,r,ir,reset,w)
    print("{} | {}Youtube : {}ETOS Cenel     {} | {} We Are Legion{}|").format(r,w,w,w,lgray,w)
    print("{} '------------------------------------{}---------------'  ").format(r,w)
    print ("  {}[ 1 ] {}Italy").format(r,w)
    print ("  {}[ 2 ] {}Indonesia").format(r,w)
    print ("  {}[ 3 ] {}Japan").format(r,w)
    print ("  {}[ 4 ] {}United States").format(r,w)
    print ("  {}[ 5 ] {}France").format(r,w)
    print ("  {}[ 6 ] {}Korea").format(r,w)
    print ("  {}[ 7 ] {}German").format(r,w)
    print ("  {}[ 8 ] {}Turkey").format(r,w)
    print ("  {}[ 9 ] {}Exit").format(r,w)
    print ""
    select = input("\033[1;31m[ \033[1;37mSelect@Number \033[1;31m]\033[1;37m> ")
    filtering(select)


def filtering(pilih):
    if pilih == 1:
        italy()
    elif pilih == 2:
        indonesia()
    elif pilih == 3:
        japan()
    elif pilih == 4:
        unitedstates()
    elif pilih == 5:
        france()
    elif pilih == 6:
        korea()
    elif pilih == 7:
        german()
    elif pilih == 8:
        turkey()
    elif pilih == 9:
        print (r+"Exiting ..."+w)
        os.sys.exit()
    else:
        print (r+"Exiting ..."+w)
        os.sys.exit()

if __name__ == '__main__':
    main()
