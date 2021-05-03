import names
import random
import pyfiglet
import os 
import pwerd
import emait


em = emait.emai
def menu(x):
  print(pyfiglet.figlet_format("'account maker'"))
  print ("currently",len(names.lon))
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
  tn = random.choice(names.lon)+random.choice(names.surn)
  ran = random.randint(00,10)
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


menu(1)