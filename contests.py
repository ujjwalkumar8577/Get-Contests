import urllib.request, urllib.parse, urllib.error
import requests
import json
import string

# formats string by adding spaces
def pf(string,n):
    s=str(string)
    return s[:n].ljust(n)

# returns JSON object received from URL with predefined User Agent
def getJSONwithUserAgent(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    result = requests.get(url, headers=headers)
    data = result.content.decode()
    try:
        js = json.loads(data)
    except:
        js = None
    return js

# return the list of available sites
def getSites():
    url='https://kontests.net/api/v1/sites'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    result = requests.get(url, headers=headers)
    data = result.content.decode()
    js = json.loads(data)
    return js

# print the given list of sites
def printSites(js):
    for ind in range(0,len(js)):
        sn=ind+1
        sname=js[ind][0]
        uname=js[ind][1]
        url=js[ind][2]
        print(pf(sn,4),pf(sname,20),pf(uname,20),pf(url,30))

# print contests from given site
def getContests(site):
    url='https://kontests.net/api/v1/'+site
    js = getJSONwithUserAgent(url)
    print('Data Received')
    lst=list()
    print('Contests Found : ',len(js),'\n')

    print('- '*77)
    print('S.N.',pf('name',40),pf('url',12),pf('start_time',25),pf('end_time',25),pf('site',25),pf('is_near',10),pf('status',10))
    print('- '*77)

    for ind in range(0,len(js)):
        sn=ind+1
        name=js[ind]['name']
        url='click here'
        start_time=js[ind]['start_time']
        end_time=js[ind]['end_time']
        near=js[ind]['in_24_hours']
        status=js[ind]['status']

        try:
            site=js[ind]['site']
        except:
            site='NA'

        if 'Lunchtime' in name or 'Cook-Off' in name:
            lst.append((name,start_time))
        
        print(pf(sn,4),pf(name,40),pf(url,12),pf(start_time,25),pf(end_time,25),pf(site,25),pf(near,10),pf(status,10))
    print('- '*77)

    print("\n***  IMPORTANT CONTESTS ***\n")
    for (n,t) in lst:
        print(n,'\t',t)
    print()

if __name__ == '__main__':

    print()
    js=getSites()
    choice=1
    while choice>=0:
        printSites(js)
        choice=int(input('Enter your choice or -1 to Exit\n'))

        if choice>0:
            getContests(js[choice-1][1])
        elif choice==0:
            getContests('all')
        else:
            print('Exiting...')