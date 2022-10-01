import os

from termcolor import colored
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def anonymize():
 print(colored("1)Install","red"))
 print(colored("2)Run","green"))
 print(colored("3)Stop","blue"))
 print(colored("4)Go back","yellow"))
 nl=int(input())
 if nl == 1:
  os.system("clear")
  os.system("git clone https://github.com/Und3rf10w/kali-anonsurf")
  os.system("cd kali-anonsurf")
  os.system("./installer.sh")
  os.system("clear")
  print("type anonsurf stop")
  os.system("anonsurf start")
  os.system("python lazyscript.py")
  #print(colored('*anonsurf is started','green'))
 if nl == 2:
  os.system("anonsurf start")
 if nl == 3:
  os.system("anonsurf stop")
 if nl == 4:
  os.system("python lazyscript.py")

def ping():
    ip=input("Please Enter Ip Adress: ")
    os.system("clear")
    os.system("ping "+ip)
    os.system("python lazyscript.py")

def exit1():
   os.system("clear")
   exit()
   
   
def spam1():
 print(colored("1)Install","yellow"))
 print(colored("2)Run","green"))
 print(colored("3)Exit","red"))
 new=int(input(">> "))
 if new == 1:
  print("Please Wait While We Install it")
  os.system("git clone https://github.com/TheSpeedX/TBomb")
  os.system("clear")
  os.system("python lazyscript2.py")
 if new == 2:
  cwd = os.getcwd()
  os.chdir(cwd +"/TBomb")
  os.system("./TBomb.sh")
  #os.system("cd")
  os.chdir(cwd)
  os.system("python lazyscript2.py")
  
 if new == 3:
  os.system("python lazyscript2.py")

def nps():
 print(colored("1)URL scanining","yellow"))
 print(colored("2)ip Adress Scaning","green"))
 print(colored("3)Exit","red"))
 c2=int(input(">> "))
 os.system("clear")
 if c2 ==1 :
  print(colored("don't enter www.in url","green"))
  nip=input(colored("Please Enter The URL HERE: ","red"))
  os.system("nmap -O -v "+nip)
  #os.system("wpscan "+nip)
 if c2 ==2:
  nip=input(colored("Please Enter The Ip Adress: ","red"))
  
  os.system("nmap -O -v "+nip)
  
  #os.system("wpscan --url -sV "+nip) 
 if c2 == 3:
  os.system("clear")
  os.system("python lazyscript2.py")


def wps():
 ur=input(colored("*Please Enter URL: ","green"))
 os.system("wpscan --url "+ur)
 print(colored("1)Go back to the script","green"))
 print(colored("2)Exit from script","red"))
 nc=int(input(">> "))
 if nc == 1:
  os.system("python lazyscript2.py")
 if nc == 2:
  exit()
 
 
def sp():
 print(colored("1)Install","red"))
 print(colored("2)Run","green"))
 print(colored("99)exit","white"))
 spc=int(input())
 if spc == 1:
  print("Please Wait while We Download It")
  os.system("git clone https://github.com/htr-tech/zphisher.git")
  cwd = os.getcwd()
  os.chdir(cwd +"/zphisher")
  os.system("./zphisher.sh")
 if spc == 2:
  print("Opening The Tool wait")
  cwd = os.getcwd()
  os.chdir(cwd +"/zphisher")
  os.system("./zphisher.sh")
 if spc == 3:
  os.system("python lazyscript2.py")

def cp():
 print(colored("1)Install","red"))
 print(colored("2)Run","green"))
 print(colored("3)Exit","blue"))
 cpc = int(input(">> "))
 if cpc ==1:
  print("Please Wait while I Install It")
  os.system("git clone https://github.com/techchipnet/CamPhish") 
  cwd = os.getcwd()
  os.chdir(cwd +"/CamPhish")
  os.system("./camphish.sh")
 if cpc == 2:
  cwd = os.getcwd()
  os.chdir(cwd +"/CamPhish")
  os.system("./camphish.sh")
 if cpc == 3:
  os.system("python lazyscript2.py")
   
  
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#os.system("clear")


os.system("apt install figlet")

os.system("clear")
os.system('figlet Lazy Script')

print("                                                   --By Harshith Vadlamudi")




print("\n\n\n\n")

print(colored('1)Anonymize','red'),colored('\t\t\t2)Pinger','red'))

print(colored('3)Mail spammer','red'),colored('\t\t\t4)SMS-spammer','red'))

print(colored('5)CALL spammer','red'),colored('\t\t\t6)Social-Phishing','red'))

print(colored('7)WP-Scanner','red'),colored('\t\t\t8)Camera-Phishing','red'))

print(colored('9)NMAP-Scanner','red'))



print("\n\n99)exit\n\n")


choice=int(input(">> "))

if choice == 1:
   anonymize()


if choice == 2:
   ping()
   
   
if choice ==3:
 spam1()
  

if choice == 4:
 spam1()
 
if choice == 5:
 spam1()

if choice == 9:
 nps()


if choice == 7:
 wps()

if choice == 6:
 sp()

if choice == 8:
 cp()

if choice == 99:
  exit1()








