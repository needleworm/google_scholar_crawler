# google_scholar_crawler
Google Scholar Crawler.

## Usage
> import gscrawler as g
>
>
> g.crawl_abstracts(\<keyword>, outfile=None, max_iter=1000)
>

outfile is the name of output file. default value is \[Crawling Result]_<keyword>.txt. 
If you want to provide custome filename, please specify the file extension. ".csv" type is recommended.

max_iter is the number of articles you want to crawl.

## Requirements
> pip install scholarly
