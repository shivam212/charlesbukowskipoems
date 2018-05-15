#!python3
#downloads charles bukowski poems
import requests, sys, os, bs4, time
os.makedirs('CharlesBukowski',exist_ok=True)
cb=requests.get('https://bukowski.net/poems/')
cb.raise_for_status()
cbht=bs4.BeautifulSoup(cb.text,"html.parser")
links=cbht.select('a[class=noline]')
length=len(links)
print(length)
for i in range(length):
    text=links[i].get('href')
    text='https://bukowski.net/poems/'+text
    material=requests.get(text)
    material.raise_for_status
    matedown=bs4.BeautifulSoup(material.text,"html.parser")
    stuff=matedown.select('p')
    string='\n'.join(str(v) for v in stuff)
    cleantext =bs4.BeautifulSoup(string, "html.parser").text
    textfile=open(os.path.join('CharlesBukowski',os.path.basename(text)+'.txt'),'w')
    textfile.write("{}".format(cleantext))
    textfile.close()
