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
    cot_dolar_matriz = (url_cambio, nombre, compra, venta)
    return cot_dolar_matriz


def dolarCambio18():
    url = 'http://www.cambio18.com/'
    page = urllib2.urlopen(url)
    raw = BeautifulSoup(page, 'html.parser')
    cot = raw.find(
        'div',
        attrs={'class': 'wpb_column vc_column_container vc_col-sm-3'})
    cot2 = cot.findAll('td')
    compra = cot2[1].text.strip()
    venta = cot2[3].text.strip()
    nombre = 'Cambio 18'
    url_cambio = url
    cot_dolar_18 = (url_cambio, nombre, compra, venta)
    return cot_dolar_18


def dolarVarlix():
    url = 'http://www.varlix.com.uy/'
    page = urllib2.urlopen(url)
    raw = BeautifulSoup(page, 'html.parser')
    cot = raw.find('div', attrs={'class': 'cotizacion'})
    cot2 = cot.findAll('td')
    compra = cot2[4].text.strip()
    venta = cot2[5].text.strip()
    nombre = 'Cambio Varlix'
    url_cambio = url
    cot_dolar_varlix = (url_cambio, nombre, compra, venta)
    return cot_dolar_varlix


def dolarGales():
    url = 'http://www.gales.com.uy/home/'
    page = urllib2.urlopen(url)
    raw = BeautifulSoup(page, 'html.parser')
    cot = raw.find('table', attrs={'class': 'monedas'})
    cot2 = cot.findAll('td')
    compra = cot2[1].text.strip()
    venta = cot2[2].text.strip()
    nombre = 'Cambio Gales'
    url_cambio = url
    cot_dolar_gales = (url_cambio, nombre, compra, venta)
    return cot_dolar_gales


def dolarFavorita():
    url = 'http://www.lafavorita.com.uy/'
    page = urllib2.urlopen(url)
    raw = BeautifulSoup(page, 'html.parser')
    cot = raw.find('ul', attrs={'class': 'course-block'})
    cot2 = cot.findAll('li')
    compra = cot2[1].text.strip()
    venta = cot2[2].text.strip()
    nombre = 'Cambio La Favorita'
    url_cambio = url
    cot_dolar_favorita = (url_cambio, nombre, compra, venta)
    return cot_dolar_favorita
