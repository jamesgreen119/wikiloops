# -*- coding: utf-8 -*-
"""
Created on Sun May  1 01:06:41 2016

@author: Jamie
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import urllib.request as urllib2


loopr = "http://www.wikiloopr.com/"
wiki = "https://en.wikipedia.org/wiki/Special:Random"


def getPage(url):
    response = urllib2.urlopen(url)
    name=re.findall('https://en.wikipedia.org/wiki/(.+)',response.geturl())[0]
    name=re.sub('_','%20',name,count=10)
    return name
    
#print(getPage(wiki))

browser = webdriver.Firefox()

def getLoop(string):
    url = loopr+string
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html,"lxml")

    souptext = str(soup)
    path = re.findall('target="_blank">(.+?)<',souptext)
    try:
        loopstart = re.findall('<span class="loopstart">(.+?)<',souptext)[0]
        loopstartnum = int(re.findall('<span class="initialLength">(.+?)<',souptext)[0])+1
    
        return ([path,loopstart,loopstartnum])
    except:
        return (getLoop(getPage(wiki)))
    browser.close()
    browser.quit()

    

    
#print(getLoop(getPage(wiki)))

loops=[""]
allLoops=[]
paths=[]

for i in range(4):
    print("Beginning loop #"+str(i)+"...")
    paths.append(getLoop(getPage(wiki)))
    
    newloopstart = paths[i][2]
    if paths[i][1] in allLoops:
        for j in loops:
            if paths[i][1] in j:
                paths[i].append(j)
    else:    
        loops.append(paths[i][0][newloopstart:len(paths[i][0])])
        [allLoops.append(i) for i in paths[i][0][newloopstart:len(paths[i][0])]]
        paths[i].append(paths[i][0][newloopstart:len(paths[i][0])])
    print("Loop #"+str(i)+" Done!")


f = open('loops.txt','w')
f.write(str(loops))
g=open('paths.txt','w')
g.write(str(paths))
f.close()
g.close()


pairs=[]

for path in paths:
    for i in range(0,len(path[0])-1):
        pairs.append([path[0][i],path[0][i+1],path[1]])
        

print(pairs[1:5])

h=open('pairs.txt','w')

for pair in pairs:
    h.write(pair[0]+'|'+pair[1]+'|'+pair[2]+'\n')



loopPairs=[]


i=open('loopPairs.txt','w')






