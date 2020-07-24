import requests
page = requests.get("https://www.google.com")
type(page)
page.text


rating_pages = []
for year in range(2010, 2019):
    for month in range(1, 13):
        for week in range(0, 5):
            url = 'https://workey.codeit.kr/ratings/index?year={0}&month={1}&weekIndex={2}'.format(year, month, week)
            page = requests.get(url)
            rating_pages.append(page.text)

print(len(rating_pages))
print(rating_pages[0])

# bs4
from bs4 import BeautifulSoup

html_code = """<!DOCTYPE html>
<html>
<head>
    <title>Sample Website</title>
</head>
<body>
<h2>HTML exercise!</h2>

<p>This is first paragraph.</p>
<p>This is second paragraph!</p>

<ul>
    <li>coffee</li>
    <li>green tea</li>
    <li>milk</li>
</ul>

<img src='https://i.imgur.com/bY0l0PC.jpg' alt="coffee"/>
<img src='https://i.imgur.com/fvJLWdV.jpg' alt="green-tea"/>
<img src='https://i.imgur.com/rNOIbNt.jpg' alt="milk"/>

</body>
</html>"""

# convert to BeautifulSoup type
soup = BeautifulSoup(html_code, 'html.parser')

# select all <li> tags
li_tags = soup.select('li')

# create blank list
beverage_names = []

# extract and put in the list
for li in li_tags:
    beverage_names.append(li.text)

print(beverage_names)

# select all <img> tags
img_tags = soup.select('img')

# create blank list
img_srcs = []

# extract img url and put in the list
for img in img_tags:
    img_srcs.append(img["src"])

print(img_srcs)


#####
response = requests.get("https://workey.codeit.kr/music/index")

soup = BeautifulSoup(response.text, 'html.parser')

li_tags = soup.select(".popular__order li")

popular_artists = []

for li in li_tags:
    popular_artists.append(li.text.strip())

print(popular_artists)


# q
response = requests.get("https://workey.codeit.kr/orangebottle/index")

soup = BeautifulSoup(response.text, 'html.parser')
phone_tags = soup.select(".branch .phoneNum")

phone_numbers = []
for tags in phone_tags:
    phone_numbers.append(tags.text.strip())

print(phone_numbers)

# q
response = requests.get("https://workey.codeit.kr/music/index")

soup = BeautifulSoup(response.text, 'html.parser')

li_tags = soup.select(".rank__order li") # ".rank__order .liist" also works

search_ranks = []
for li in li_tags:
    search_ranks.append(li.text.strip().split()[2])

print(search_ranks)


##### real data
import time
import requests
from bs4 import BeautifulSoup

pages = []

page_num = 1

while True:
    response = requests.get("http://www.ssg.com/search.ssg?target=all&query=nintendo&page=" + str(page_num))

    soup = BeautifulSoup(response.text, 'html.parser')

    # contain HTML code only when ".csrch_tip" doesn't exist
    if len(soup.select('.csrch_tip')) == 0:
        pages.append(soup)
        print(str(page_num) + "page scraping completed")
        page_num += 1
        time.sleep(3)
    else:
        break

print(len(pages))


# q
import requests
from bs4 import BeautifulSoup

rating_pages = []
for year in range(2010, 2019):
    for month in range(1, 13):
        week = 0
        while True:
            page = requests.get('https://workey.codeit.kr/ratings/index?year={0}&month={1}&weekIndex={2}'.format(year, month, week))
            soup = BeautifulSoup(page.text, 'html.parser')
            if len(soup.select('.row')) != 1:
                rating_pages.append(page.text)
                week += 1
            else:
                break

print(len(rating_pages))
print(rating_pages[0])

# sample answer
import requests
from bs4 import BeautifulSoup

years = list(range(2010, 2019))
months = list(range(1, 13))
weeks = list(range(0, 5))

rating_pages = []

for year in years:
    for month in months:
        for week in weeks:
            response = requests.get("https://workey.codeit.kr/ratings/index?year=" + str(year) + "&month=" + str(month) + "&weekIndex=" + str(week))
            soup = BeautifulSoup(response.text, 'html.parser')

            if len(soup.select('.row')) > 1:
                rating_pages.append(response.text)


# webpage to data frame
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

records = []
page_num = 1

while True:
    response = requests.get("http://www.ssg.com/search.ssg?target=all&query=nintendo&page=" + str(page_num))

    soup = BeautifulSoup(response.text, 'html.parser')

    # get product info where "prodName" class exists
    if len(soup.select('.csrch_tip')) == 0:
        product_names = soup.select('.cunit_info > div.cunit_md.notranslate > div > a > em.tx_ko')
        product_prices = soup.select('.cunit_info > div.cunit_price.notranslate > div.opt_price > em')
        product_urls = soup.select('.cunit_prod > div.thmb > a > img')
        page_num += 1
        time.sleep(3)
        
        for i in range(len(product_names)):
            record = []
            record.append(product_names[i].text)
            record.append(product_prices[i].text.strip())
            record.append("https://www.ssg.com" + product_urls[i].get('src'))
            records.append(record)
    else:
        break

df = pd.DataFrame(data = records, columns = ["name", "price", "img url"])

df.head()

# q
import pandas as pd
import requests
from bs4 import BeautifulSoup

years = list(range(2010, 2019))
months = list(range(1, 13))
weeks = list(range(0, 5))

rating_pages = []
records = []

for year in years:
    for month in months:
        for week in weeks:
            response = requests.get("https://workey.codeit.kr/ratings/index?year=" + str(year) + "&month=" + str(month) + "&weekIndex=" + str(week))
            soup = BeautifulSoup(response.text, 'html.parser')
            
            if len(soup.select('.row')) > 1:
                rating_pages.append(response.text)
    
                period = soup.select('#weekSelectBox [selected="selected"]')[0].text
                rank = soup.select('.row .rank')[1:]
                channel = soup.select('.row .channel')[1:]
                program = soup.select('.row .program')[1:]
                percent = soup.select('.row .percent')[1:]
                
                for i in range(10):
                    a = []
                    a.append(period)
                    a.append(rank[i].text)
                    a.append(channel[i].text)
                    a.append(program[i].text)
                    a.append(percent[i].text)
                    records.append(a)

df = pd.DataFrame(data=records, columns=['period', 'rank', 'channel', 'program', 'rating'])
df.head()

# sample answer
rating_pages = []

for year in years:
    for month in months:
        for week in weeks:
            response = requests.get("https://workey.codeit.kr/ratings/index?year=" + str(year) + "&month=" + str(month) + "&weekIndex=" + str(week))
            soup = BeautifulSoup(response.text, 'html.parser')

            if len(soup.select('.row')) > 1:
                rating_pages.append(soup)

records = []

for page in rating_pages:
    date = page.select('option[selected=selected]')[2].text
    ranks = page.select('.row .rank')[1:]
    channels = page.select('.row .channel')[1:]
    programs = page.select('.row .program')[1:]
    percents = page.select('.row .percent')[1:]

    for i in range(10):
        record = []
        record.append(date)
        record.append(ranks[i].text)
        record.append(channels[i].text)
        record.append(programs[i].text)
        record.append(percents[i].text)
        records.append(record)

df = pd.DataFrame(data=records, columns=['period', 'rank', 'channel', 'program', 'rating'])
df.head()
