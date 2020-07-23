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


