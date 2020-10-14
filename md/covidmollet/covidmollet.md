# Covid Mollet - Webscraping

## Introduction

The intention of this notebook is to explain a python script that it's created at the beginning of the pandemic to automatically receive (via crontab on a linux server for example) the local news (from my town) about covid collected news in different local media.

## Local Media 'Scraped'

[Nacio Granollers](https://www.naciodigital.cat/naciogranollers/)

[Som Mollet](https://www.sommollet.cat/)

[El 9nou Valles Oriental](https://el9nou.cat/valles-oriental/)

[Mollet a Ma](https://www.clicama.cat/)

[Ajuntament Mollet del Valles](https://www.molletvalles.cat/)

[Revista del Valles](https://revistadelvalles.es/)

## Steps
The script mainly does:

1. Scrape the local medium with the address that seemed easiest to scrape.
2. From the news content look for 3 keywords, 'covid','coronavirus' and 'mollet', after some cleaning to let us catch these 2 words in all the article.
3. If both are met, add the title of the news, part of the text (can be configured) and the link of the news in a data frame, which will finally be formatted as html and send by mail.

### Some little notes
In the notebook I will avoid using different local modules, but the python script developed it's much clean and readable.

*You will see that variables and descriptions are in spanish this is because target mail people are spaniards basically :P*

## Code and explanation

All libraries used:

```python
#### Data manipulation
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
#### Mail libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#### Data string cleaning
import re
import string
```

Let's create the 'work' dataframe in which I will export the news at the end and that I will send by email in 'html' format, it is not necessary to define it, but it helps me to visualize what data I use and for what etc ...

```python
noticias = pd.DataFrame(columns=['Titulo','Link','Texto','Origen'])
pd.set_option('display.max_colwidth', None) #avoid link truncation
```
### Functions definition

- *f_get_data:* When the link for the article has been detected, this function is getting all the article in an string to work with it.
    - You will see that some user-agents to request function has been added. This is because some webs are not working fine if no user-agent is defined.
- *f_mollet_corona:* When string article is cleaned and arranged, this function returns 1 if it's desired article or 0 if not.
- *busca_mollet:* Work function that uses *f_mollet_corona* in the dataframe to drop the rows that are not 'Important' or relevant.

```python
def f_get_data(url):
    #Import html information
    request = urllib.request.Request(url,
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
    response = urllib.request.urlopen(request, timeout=20)
    content = response.read()
    #Soup object (identify tgs, etc..)
    soup = BeautifulSoup(content, "html.parser")
    return soup

def f_mollet_corona(text):
    value = text.find('mollet')
    value2 = text.find('coronavirus')
    value3 = text.find('covid')
    if value > 0 and ( value2 > 0 or value3 >0):
        return 1
    else:
        return 0

def busca_mollet(noticias):
    encontrar = lambda x: f_mollet_corona(x)
    noticias['Importante']=noticias.Clean.apply(encontrar)
    noimportante = noticias[noticias['Importante']==0].index
    noticias.drop(labels=noimportante,inplace=True)
    return noticias
```

When we have the complete string of the article to avoid any disturbing find element (uppercase, strange symbols, etc..) we are going to clean our strings and let it easy to find some word or sentence. For that this function is defined:

```python
def clean_web_text(text):
    #Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.
    text = text.lower()
    text = re.sub('\[.*?¿\]\%', ' ', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub('\w*\d\w*', '', text)
    #some additional punctuation and non-sensical text
    text = re.sub('[‘’…«»]', '', text)
    text = re.sub('\n', ' ', text)    
    return text
```

### WebScraping media

Ok, let's webscrap the news media one by one, as each web has it's own particular way to publish and it's own classes, etc... The most easy way it's if you find some *rss* summary that helps a lot to get a list of latest news, if not, no problem, but you have to search in the div cascade a bit more.

#### El9nou

```python
url = 'https://el9nou.cat/valles-oriental/'
soup = nt.f_get_data(url)
art = soup.find(class_='noticies-portada')

items = art.find_all('article')

for i,item in enumerate(items):
    url_item = item.find('a')['href']
    tit_item = item.find('h1').getText()
    soup2 = nt.f_get_data(url_item)
    text_art = soup2.find(class_="col-md-12 marge")
    body = text_art.find_all('p')
    texto = ''
    origen = '9nou'
    for body_item in body:
        texto = texto + body_item.getText()
    noticias.loc[len(noticias)]=[tit_item,url_item,texto,origen]
```

#### Nacio Granollers

```python
url2 = 'https://www.naciodigital.cat/naciogranollers/rss'
request = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(request, timeout=20)
content = response.read()
# Soup object (identify tags, etc..)
soup = BeautifulSoup(content, "lxml")
art = soup.find_all('item')
for art_item in art:
    title = art_item.find('title').getText()
    link  = art_item.find('guid').getText()
    soup2 = nt.f_get_data(link)
    body = soup2.find_all(class_='amp_textnoticia')
    texto = ''
    origen = 'nacio'
    for body_item in body:
       texto = texto + body_item.getText()
    noticias.loc[len(noticias)]=[title,link,texto,origen]
```

#### Som mollet

```python
url3 = 'https://www.sommollet.cat/rss'
request = urllib.request.Request(url3, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(request, timeout=20)
content = response.read()
# Soup object (identify tags, etc..)
soup = BeautifulSoup(content, "lxml-xml")
art = soup.find_all('item')
for art_item in art:
    title = art_item.find('title').getText()
    link  = art_item.find('guid').getText()
    soup2 = nt.f_get_data(link)
    body = soup2.find_all(class_='interior-main__content')
    origen = 'sommollet'
    texto = ''
    for body_item in body:
       texto = texto + body_item.getText()
    noticias.loc[len(noticias)]=[title,link,texto,origen]
```

#### Mollet a ma

```python
url4 = 'https://www.clicama.cat/rss'
request = urllib.request.Request(url4, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(request, timeout=20)
content = response.read()
# Soup object (identify tags, etc..)
soup = BeautifulSoup(content, "lxml-xml")
art = soup.find_all('item')
for art_item in art:
    title = art_item.find('title').getText()
    link  = art_item.find('guid').getText()
    soup2 = nt.f_get_data(link)
    body = soup2.find_all(class_='content-data')
    origen = 'molletama'
    texto = ''
    for body_item in body:
       texto = texto + body_item.getText()
    noticias.loc[len(noticias)]=[title,link,texto,origen]
```

#### Ajuntament Mollet

```python
url5 = 'https://www.molletvalles.cat/continguts-es-es/actualitat-es-es/notcies-es-es/'
request = urllib.request.Request(url5, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(request, timeout=20)
content = response.read()
# Soup object (identify tags, etc..)
soup = BeautifulSoup(content, "html.parser")
art = soup.find_all(class_='capsa_noticies_item')
for i,art_item in enumerate(art):
    link = art_item.find('a')['href']
    origen = 'ajuntament'
    if art_item.find('h3') != None:
        title = art_item.find('h3').getText()
        soup2 = nt.f_get_data(link)
        body = soup2.find_all(style='text-align:justify')
        texto = body[0].getText()
        noticias.loc[len(noticias)]=[title,link,texto,origen]
```

#### Revista del Valles

```python
url6 = 'https://revistadelvalles.es/feed/'
request = urllib.request.Request(url6, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
response = urllib.request.urlopen(request, timeout=20)
content = response.read()
# Soup object (identify tags, etc..)
soup = BeautifulSoup(content, "lxml-xml")
art = soup.find_all('item')
for art_item in art:
    title = art_item.find('title').getText()
    link  = art_item.find('guid').getText()
    soup2 = nt.f_get_data(link)
    body = soup2.find_all(class_='td-post-content tagdiv-type')
    origen = 'revistavalles'
    texto = ''
    for body_item in body:
       texto = texto + body_item.getText()
    noticias.loc[len(noticias)]=[title,link,texto,origen]
```

The idea, is to webscrap all the articles (header, text, link...) and fill my dataframe, then I will filter with the ones we want.

### Cleaning and filtering

Saving all data in one dataframe makes me easy then to apply any function, filter or data manipulation. I have also let the filtering to the end, so I could re-use this code if I want to apply different filters in the future.

With defined functions and our dataframe, selecting which articles we want it's really easy

```python
#Cleaning
clean_text = lambda x: clean_web_text(x)
noticias['Clean'] = noticias.Texto.apply(clean_text)

#Filtering
resultado = nt.busca_mollet(noticias)
#For html visualization reasons
resultado.drop(labels=['Texto','Clean','Importante','Origen'],axis=1,inplace=True)
resultado.reset_index(drop=True, inplace=True) s
```

Now we have our dataframe with the news we want ^^.

### Send the formatted mail

To send the mails, let at first define function for mail sending

```python
def send_news_mail(direccion,df):
    # Server smtp security
    MY_ADDRESS = 'mailuser'
    PASSWORD = 'password'

    # Smtp server configuration
    s = smtplib.SMTP(host='smtp.host.com', port=587) # server and port
    s.starttls() # Conexion tls
    s.login(MY_ADDRESS, PASSWORD) # login SMTP

    # Create the message
    msg = MIMEMultipart('alternative')
    text = 'Hi All,\n'
    html = '''<h3>Últimas notícias sobre #covid #coronavirus y #Mollet.</h3><p><p>
    Las notícias pueden estar repetidas, se busca todas las que los medios 
    tienen publicadas en sus paginas principales<p>{}<p><p>Sergi García
    <p>Python Analysis Tools'''.format(df.to_html())
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    # Attach parts into message container.
    msg.attach(part1)
    msg.attach(part2)

    # Configurar los parametros del mensaje
    msg['From']=MY_ADDRESS
    msg['To']= direccion
    msg['Subject']="Notícias Locales - #Covid #Coronaviurs #Mollet"

    # Send the message and empty memory
    s.send_message(msg)
    del msg

    # Stop SMTP session
    s.quit()
```

And that's all you can send your news list in a correct formatted html mail to all you want.

```python
to = 'mail@gmail.com,mail2@mail.com,...'
send_news_mail(to,resultado)
```

![mailsample](/static/notebooks/covidmollet/images/mail.png)



