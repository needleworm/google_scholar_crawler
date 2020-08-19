"""
Author : Byunghyun Ban
Last Modification : 2020.08.19.
https://github.com/needleworm
halfbottle@sangsang.farm
"""

from scholarly import scholarly as S
from fp.fp import FreeProxy
import time

def _set_new_proxy():
    while True:
        proxy = FreeProxy(rand=True, timeout=1, country_id=["US", "CA"]).get()
        proxy_works = S.use_proxy(http=proxy, https=proxy)
        if proxy_works:
            break
    print("Working proxy:", proxy)
    return proxy


def crawl_abstracts(keyword, outfile=None, max_iter=1000):
    _set_new_proxy()
    while True:
        try:
            search_query = S.search_pubs(keyword)
            time.sleep(5)
        except Exception as e:
            print("Trying new proxy on query base")
            _set_new_proxy()

    print("Crawling Started with keyword <" + keyword + ">.\n")

    if not outfile:
        outfile = "[Crwaling Results]" + keyword + ".csv"
    o_file = open(outfile, 'w')

    header = "Index, Year, Author, Title, journal, cites, url, abstract\n"

    o_file.write(header)

    idx = 0

    for i in range(max_iter):
        while True:
            try:
                time.sleep(5)
                article = next(search_query).bib
            except Exception as e:
                print("Trying new proxy on article read")
                _set_new_proxy()

        try:
            title = article["title"]
        except KeyError:
            print("Error on Title Info")
            continue

        try:
            abstract = article["abstract"]
            if abstract.startswith("Skip to main content"):
                continue
        except KeyError:
            print("Error on Abstract")
            continue

        try:
            year = article["year"]
        except KeyError:
            print("Error on year")
            continue

        try:
            author = article["author"]
        except KeyError:
            print("Error on author")
            continue

        try:
            journal = article["journal"]
        except KeyError:
            print("Error on journal")
            continue

        try:
            url = article["url"]
        except KeyError:
            print("Error on url")
            continue

        try:
            cites = article["cites"]
        except KeyError:
            print("Error on cites")
            continue

        idx += 1

        citation_form = author + '. "' + title + '." ' + journal + ". " + year
        print("\n" + citation_form)
        "Index, Year, Author, Title, journal, cites, url, abstract\n"
        o_file.write(str(idx) + ", ")
        o_file.write(year + ", ")
        o_file.write(author + ", ")
        o_file.write(title + ", ")
        o_file.write(journal + ", ")
        o_file.write(cites + ", ")
        o_file.write(url + ", ")
        o_file.write(abstract + "\n")

    o_file.close()

    print("\n\nProcess Done!")
    print("Total " + str(idx) + " articles are crawled.")
    print("Results are saved in <" + outfile + ">.")
