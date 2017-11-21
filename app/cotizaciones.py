import urllib2
from bs4 import BeautifulSoup

compra = 0
venta = 1


def dolarBrou():
    url = 'https://www.portal.brou.com.uy/cotizaciones'
    page = urllib2.urlopen(url)
    raw = BeautifulSoup(page, 'html.parser')
    cot = raw.find('tbody').findAll('p', attrs={'class': 'valor'})
    compra = cot[0].text.strip()
    venta = cot[1].text.strip()
    cot_dolar_brou = [compra, venta]
    data = {"dolar_brou": cot_dolar_brou}
    return data


def dolarSir():
    url = 'http://www.cambiosir.com.uy'
    page = urllib2.urlopen(url)
    raw = BeautifulSoup(page, 'html.parser')
    cot = raw.find('tbody').findAll('td', attrs={'class': 'cotizacion'})
    compra = cot[0].text.strip()
    venta = cot[1].text.strip()
    cot_dolar_sir = [compra, venta]
    data = {"dolar_sir": cot_dolar_sir}
    return data


datos = dolarBrou()
print "Cotizacion del Dolar en el BROU"
print "Compra: " + str(datos['dolar_brou'][compra])
print "venta : " + str(datos['dolar_brou'][venta])

datos = dolarSir()
print "Cotizacion del Dolar en el cambio Nixis"
print "Compra: " + str(datos['dolar_sir'][compra])
print "venta : " + str(datos['dolar_sir'][venta])
