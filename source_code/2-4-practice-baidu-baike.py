from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
from urllib.parse import quote

base_url = "https://baike.baidu.com"

his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

for i in range(20):
    url = base_url + his[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    print(i, soup.find('h1').get_text(), '    url: ', his[-1])

    # find valid urls
    sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("^(/item/)((%.{2})+|[\u4e00-\u9fa5]+)$")})

    if len(sub_urls) != 0:
        temp=random.sample(sub_urls, 1)[0]['href']
        if len(re.findall("([\u4e00-\u9fa5]+)",temp))==0:
            his.append(temp)
        else:
            a,=re.findall("([\u4e00-\u9fa5]+)", temp)
            b="/item/"+quote(a)
            his.append(b)
    else:
        # no valid sub link found
        his.pop()
