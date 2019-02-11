import argparse # proposé par l'énnoncé
import click  # proposé par l'énnoncé
import markdown2  # proposé par l'énnoncé
import re  # regular expression
import os 
from os.path import split

# Variable pour Html
head = "<!DOCTYPE html><html><head>\t<meta charset='utf-8'/>\t<title></title>\t<link rel='stylesheet' type='text/css' href='main.css'/></head><body>"
finHead = "</body></html>"

def conversion(md_i, html_j):
    list = os.listdir(+md_i)
    for i in  list:
        f = open(f'./{md_i}/{i}')
        html = markdown2.markdown(f.read())
        nom_du_fichier = os.path.split(i)[0]
        html_file = open(f'./{html_j}/{nom_du_fichier}.html')
        html_file.write(head)
        html_file.write(html)
        html_file.write(finHead)

print('Pour que cela fonctionne il faut ecrire : -i fichier.md -o fichier.html')

parser = argparse.ArgumentParser()
parser.add_argument("-o", '--output',help='Inserer le chemin du fichier .html')
parser.add_argument("-i", '--input',help='Inserer le chemin du fichier .md')
args = parser.parse_args()
conversion(args.input, args.output)
