import names
import random
import pyfiglet
import os 
import pwerd
import emait


em = emait.emai
def menu(x):
  print(pyfiglet.figlet_format("'account maker'"))
  hme()
  print ("Github : https://github.com/muki119")
  print("---------------------------------------")
  if x == 2 :
    print("try again")
  try:
    q = int(input("How many accounts would you like "))
  except:
    print("try again")
    os.system("clear")
    menu(2)

  creator(q)
  
def creator(q):
  for z in range(0,q):
    nme = ""
    nme += create() + " : " +pshe()
    print(nme)
    filer(nme)
   
    
def create():
  tn = random.choice(names.lon)+random.choice(names.surn).lower()
  ran = random.randint(00,100)
  if ran != 00 :
      tn+= str(ran)
  tn += ("@"+random.choice(em))
  return(tn)

def pshe ():
  ps = random.choice(pwerd.pswrd)+random.choice(pwerd.pswrd)+str(random.randint(0,99))

  return(str(ps))

def filer (nme):
  with open ("outp.txt","a") as po:
    po.writelines((nme+"\n"))

def hme():
  print ("currently",len(names.lon),"NAMES WHITH : ",len(names.surn),"surnames. Aswell as ",len(pwerd.pswrd),"passwords and ",len(em ),"emails.In total there are these many combinations: ",
  (len(names.lon)*len(names.surn)*len(pwerd.pswrd)*len(em )-106238))

if __name__ == "__main__":
  menu(1)
