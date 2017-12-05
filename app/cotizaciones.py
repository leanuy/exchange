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
    nombre = 'BROU'
    url_cambio = url
    cot_dolar_brou = (url_cambio, nombre, compra, venta)
    return cot_dolar_brou


def dolarSir():
    url = 'http://www.cambiosir.com.uy'
    page = urllib2.urlopen(url)
    raw = BeautifulSoup(page, 'html.parser')
    cot = raw.find('tbody').findAll('td', attrs={'class': 'cotizacion'})
    compra = cot[0].text.strip()
    venta = cot[1].text.strip()
    nombre = 'Cambio Sir'
    url_cambio = url
    cot_dolar_sir = (url_cambio, nombre, compra, venta)
    return cot_dolar_sir


def dolarMatriz():
    url = 'http://www.cambiomatriz.com.uy/'
    page = urllib2.urlopen(url)
    raw = BeautifulSoup(page, 'html.parser')
    cot = raw.find('div', attrs={'class': 'cont cotizaciones'})
    cot = cot.findAll('td')
    compra = cot[2].text.strip()
    venta = cot[4].text.strip()
    nombre = 'Cambio Matriz'
    url_cambio = url
    cot_dolar_sir = (url_cambio, nombre, compra, venta)
    return cot_dolar_sir
