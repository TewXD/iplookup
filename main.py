from requests import get
import json, os, socket, sys, time
from urllib.request import urlopen
a = True
ipv = input("IP:")
#Tarkistaaa onko IP Osoite validi. jos ei ole niin sammuttaa.
while True:
  try:
    socket.inet_aton(ipv)
    print("IP Yhdistetty")
    print("Kirjoita help()")
    break
  except socket.error:
    print ("IP Osoitteeseen ei voitu yhdistää.")
    sys.exit(0)
#API
loc = get('https://ipapi.co/'+ipv+'/json/')
data = json.load(urlopen('https://ipapi.co/'+ipv+'/json/'))
#Tekee apista saadusta kaupungista variablen.
kaupunki = data[u'city']
#Ottaa tiedot yllä olevasta APIsta
def main():
  print ("IP Osoite >> "+data[u'ip'])
  print ("Alue >> "+data[u'region'])
  print ("Kaupunki >> "+data[u'city'])
  print ("Valuutta >> "+data[u'currency'])
  print ("Yritys >> "+data[u'org'])
#Sammutus function.
def poistu():
  print ("Sovellus sammutetaan pian.....")
  time.sleep(1)
  sys.exit(0)
def help():
 print("--------------------")
 print("IP Osoittella saatavat tiedot.")
 print("main() -Kertoo tietoa IP Osoitteesta.")
 print("poistu() -Poistuu sovelluksesta.")
 print("ping() -Näyttää viiveen IP osoitteeseen.")
 print("--------------------")
#Näyttää viiveen IP osoitteeseen.
def ping():
  for x in range (2):
    os.system('ping ' + ipv)  
  
