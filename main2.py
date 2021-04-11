import urllib

import requests
from bs4 import BeautifulSoup

metodoa='GET'
goiburua={'Host':'egela.ehu.eus'}
datuak=''
erantzuna=''
uria='https://egela.ehu.eus/'
cookie=''

def pdfDeskargatu(soup):
    global uria,metodoa,goiburua
    lista= soup.find_all("div",{"class": "activityinstance"})
    print(lista)
    for i in lista:
        if i.find("img", {"src": "https://egela.ehu.eus/theme/image.php/fordson/core/1611567512/f/pdf"}):
            uria = str(i).split("onclick=\"window.open('")[1].split("\'")[0].replace("amp;", "")
            metodoa='POST'
            goiburua['Content-Length'] = str(0)
            erantzuna = requests.request(metodoa, uria, data=datuak, headers=goiburua, allow_redirects=False)
            uria= erantzuna.headers["Location"]
            erantzuna = requests.request(metodoa, uria, data=datuak, headers=goiburua, allow_redirects=False)
            filename = uria.split("mod_resource/content/")[1].split("/")[1].replace("%20", "_")
            with open(filename, 'wb') as fd:
                for chunk in erantzuna.iter_content():
                    fd.write(chunk)



def ikasgaiaLortu():
    global uria,erantzuna,goiburua
    soup=BeautifulSoup(erantzuna,'html.parser')
    ikasgai = soup.find_all("a",{"class":"ehu-visible"})
    print(ikasgai)
    ws=0
    i=1
    while(ws!=1):
        if("Web Sistemak" not in ikasgai[i]):
            i=i+1 #hurrengoa
        else:
            ws=1
    print(ikasgai[i])
    #web sistemak ikasgaia lortu dut, beraz orain ikasgaiaren barrura eskaera bat egin
    uria=ikasgai[i]["href"]
    goiburua={'Host': 'egela.ehu.eus','Cookie': cookie}
    erantzuna= requests.request(metodoa, uria, headers=goiburua, allow_redirects=False)
    soup= BeautifulSoup(erantzuna.content,'html.parser')
    print(soup)
    erantzuna=erantzuna.content
    pdfDeskargatu(soup)









def sartu():
    global metodoa,uria,cookie,erantzuna
    goiburua = {'Host': 'egela.ehu.eus','Cookie': cookie}
    erantzuna= requests.request(metodoa, uria, headers=goiburua, allow_redirects=False)
    print(erantzuna.text)
    erantzuna=erantzuna.content
    return


def saioaHasi():
    global cookie,metodoa,uria
    metodoa='GET'
    datuak={'username': '909785', 'password': 'Nueva2020'}
    edukia = urllib.parse.urlencode(datuak)
    goiburua = {'Host': 'egela.ehu.eus','Cookie': cookie}
    erantzuna = requests.request(metodoa, uria, headers=goiburua, data=edukia, allow_redirects=False)
    uria=erantzuna.headers["Location"]
    sartu()

def datuakSartu():
    global uria,cookie
    metodoa='POST'
    datuak={'username':'909785','password':'Nueva2020'}
    edukia = urllib.parse.urlencode(datuak)
    goiburua={'Host':'egela.ehu.eus',
              'Content-Length': str(len(edukia)),
                'Content-Type':'application/x-www-form-urlencoded',
              'Cookie': cookie}
    erantzuna = requests.request(metodoa, uria, headers=goiburua,data=edukia, allow_redirects=False)
    print(erantzuna.headers["Location"])
    uria=erantzuna.headers["Location"]
    cookie=erantzuna.headers["Set-Cookie"].split(';')[0]
    saioaHasi()

def loginLortu():
    global cookie,uria
    erantzuna=requests.request(metodoa,uria,headers=goiburua,allow_redirects=False)
    cookie = erantzuna.headers["Set-Cookie"].split(';')[0]
    uria= erantzuna.headers["Location"]
    print(uria)
    datuakSartu()



if __name__ == "__main__":
    loginLortu()
    ikasgaiaLortu()