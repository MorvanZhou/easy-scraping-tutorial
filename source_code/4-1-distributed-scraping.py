from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import multiprocessing as mp
import re
import time


def crawl(url):
    response = urlopen(url)
    time.sleep(0.1)             # slightly delay for downloading
    return response.read().decode()


def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    urls = soup.find_all('a', {"href": re.compile('^/.+?/$')})
    title = soup.find('h1').get_text().strip()
    page_urls = set([urljoin(base_url, url['href']) for url in urls])
    url = soup.find('meta', {'property': "og:url"})['content']
    return title, page_urls, url


if __name__ == '__main__':
    base_url = 'https://morvanzhou.github.io/'
    # base_url = "http://127.0.0.1:4000/"
    unseen = set([base_url,])
    seen = set()

    pool = mp.Pool(4)                       # number strongly affected
    count, t1 = 1, time.time()
    while len(unseen) != 0:                 # still get some url to visit
        print('\nDistributed Crawling...')
        crawl_jobs = [pool.apply_async(crawl, args=(url,)) for url in unseen]
        htmls = [j.get() for j in crawl_jobs]                                       # request connection
        htmls = [h for h in htmls if h is not None]     # remove None

        print('\nDistributed Parsing...')
        parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
        results = [j.get() for j in parse_jobs]                                     # parse html

        print('\nAnalysing...')
        seen.update(unseen)
        unseen.clear()

        for res in results:
            if res is not None:
                title, page_urls, url = res
                print(count, title, url)
                count += 1
                unseen.update(page_urls - seen)

    print('Total time: %.1f s' % (time.time()-t1, ))

