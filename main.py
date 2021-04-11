import urllib

import requests

erabiltzaile=''
pasahitza=''
cookie=''


def saioaLortu():
    global cookie
    metodoa = 'GET'
    uria = "https://egela.ehu.eus/"
    goiburua = {'Host': 'egela.ehu.eus',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': cookie}  # cookie-a aldagai globala bezala definitu
    erantzuna = requests.request(metodoa, uria, headers=goiburua, allow_redirects=True)

    # Erantzunak 4 atal ditu: kodea, deskribapena, goiburuak eta edukia

    kodea = erantzuna.status_code
    deskribapena = erantzuna.reason
    print(str(kodea) + " " + deskribapena)
    edukia = erantzuna.content
    print(edukia)
    return


def cookieLortu():
    global cookie
    # Eskaerak 4 atal ditu: metodoa, uria, goirburuak eta edukia
    metodoa = 'POST'
    uria = "https://egela.ehu.eus/login/index.php?testsession=55883"
    goiburua = {'Host': 'egela.ehu.eus',
                'Content-Type': 'application/x-www-form-urlencoded'}
    datuak = {'username': erabiltzaile, 'password': pasahitza}  # datu hauek aldagai globalak bezala jarri

    edukia = urllib.parse.urlencode(datuak)  # ez da hutsik joango
    goiburua['Content-Length'] = str(len(edukia))
    erantzuna = requests.request(metodoa, uria, headers=goiburua, data=edukia, allow_redirects=False)

    # Erantzunak 4 atal ditu: kodea, deskribapena, goiburuak eta edukia

    kodea = erantzuna.status_code
    deskribapena = erantzuna.reason
    print(str(kodea) + " " + deskribapena)
    edukia = erantzuna.content
    print(edukia)
    cookie = erantzuna.headers["Set-Cookie"].split(';')[0]
    print(cookie)
    return

def loginLortu():
    global erabiltzaile,pasahitza
    erabiltzaile = input('Enter your name:')
    pasahitza = input('Enter your password:')
    metodoa = 'POST'
    uria = "https://egela.ehu.eus/login/index.php" #login-aren uria
    goiburua = {'Host': 'egela.ehu.eus',
                'Content-type': 'application/x-www-form-urlencoded'}
    datuak = {'username': erabiltzaile,
              'password': pasahitza}  #erabiltzailearen login datuak, aldagai globalak.

    edukia = urllib.parse.urlencode(datuak)  # ez da hutsik joango
    goiburua['Content-Length'] = str(len(edukia))
    erantzuna = requests.request(metodoa, uria, headers=goiburua, data=edukia, allow_redirects=False)
    #orain, esteka berria testsession zenbakiarekin hartu eta aldagai batean sartu, hurrengo eskaeran sartu ahal izateko.
    return

if __name__ == "__main__":

    loginLortu()
    cookieLortu()
    saioaLortu()