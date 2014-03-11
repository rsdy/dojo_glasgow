#!/usr/bin/env python2

from unidecode import unidecode
from bs4 import BeautifulSoup
import re, os

def file_list():
    root_dir = 'jargon-4.4.7/html'
    return (os.path.join(root_dir, f) for f in os.listdir(root_dir)
            if re.match('[A-Z].html', f))

for f in file_list():
    with open(f) as doc:
        soup = BeautifulSoup(doc)
        print '\n'.join(unidecode(i.a.text) for i in soup.findAll('dt') if i.a is not None)

