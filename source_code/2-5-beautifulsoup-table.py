from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')

soup = BeautifulSoup(html, features='lxml')

# print with title
for item in soup.find("table", {"id": "course-list"}).children:
    print(item)

print("-------------------------")
# print without title
for item in soup.find("table", {"id": "course-list"}).tr.next_siblings:
    print(item)

print("-------------------------")
# navigate using next_sibling/previous_sibling
print(soup.find("img", {"src": "https://morvanzhou.github.io/static/img/course_cover/scraping.jpg"}
                ).parent.previous_sibling.get_text())

