#IMPORTING BEAUTIFULSOUP & REQUESTING URL FROM WEB
import requests
from bs4 import BeautifulSoup
url = "https://dunyanews.tv/"
r = requests.get(url)
#STORING CONTENT IN VARIABLE
htmlcontent = r.content
#USING BEAUTIFULSOUP TO PARSE THROUGH HTML
soup = BeautifulSoup(htmlcontent,'html.parser')
#ACESSING LATEST HEADLINES BY DIV AND ITS CLASS
headlines = soup.findAll('div',class_='sectionBody')
#USING FOR LOOP PRINTING & STORING TEXT CONTENT IN TXT FILE
for headline in headlines:
    headlines_text = headline.text
with open(f'headlines.txt', 'w') as f:
    f.write(headlines_text)
    print("file saved")


