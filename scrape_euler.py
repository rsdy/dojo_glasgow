#!/usr/bin/env python2

from unidecode import unidecode
from bs4 import BeautifulSoup

with open('./euler.html') as euler:
    soup = BeautifulSoup(euler.read())
    print '\n'.join(unidecode(i.a.text).split(':')[1].strip() for i in soup.findAll('h3'))
