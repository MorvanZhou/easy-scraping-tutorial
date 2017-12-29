from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)


import re
res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])
# Page title is:  Scraping tutorial 1 | 莫烦Python


res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
print("\nPage paragraph is: ", res[0])
# Page paragraph is:
#     这是一个在 <a href="https://morvanzhou.github.io/">莫烦Python</a>
#     <a href="https://morvanzhou.github.io/tutorials/scraping">爬虫教程</a> 中的简单测试.


res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)
# All links:  ['https://morvanzhou.github.io/static/img/description/tab_icon.png', 'https://morvanzhou.github.io/', 'https://morvanzhou.github.io/tutorials/scraping']