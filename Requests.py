import requests
from bs4 import BeautifulSoup

req = requests.get('https://republika.co.id/')

obj = BeautifulSoup(req.text,"html.parser")

print("----Menampilkan Semua Teks Headline----")
print("=======================================")


file = open(r'C:\Users\Faizal\Documents\Pemrograman\Python\Projek1\headline.txt','w')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
    file.write(headline.find('h2').text)
    file.write('\n')
file.close()

file = open(r'C:\Users\Faizal\Documents\Pemrograman\Python\Projek1\headline.txt','r')
for f in file:
    print(f)
