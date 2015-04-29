## Webb - Web Scrapper and Crawler
An all-in-one Python library to scrap, parse and crawl web pages

### Gist
This is a light-weight, dynamic and featured Python library crawl, download, index, parse, scrap analyze web pages in a systematic manner.

### Compatability
This library is compatible with both Python 2 (2.x) as well as Python 3 (3.x) versions. It is a download-import-and-run program with no or little changes as required by users.

### Dependencies
There are no dependencies to this project. It functions entirely of the standard in-build library support. It does not need any external support or installations. Just download and run!!!

## Usage
1. Download `webb.py`
2. Create a new file in the same folder and give it any name like `main.py`
3. Import the webb library by writing `import webb` in the `main.py` file
4. Once this is done, use any of the following commands:

* Download entire HTML page:  `print (webb.download_page("your-web-page-url"))`
* Print the page title:  `webb.title("your-web-page-url")`
* Print all the links in a pirticular web page:  `print (webb.find_all_links("your-web-page-url"))`
* Crawl web pages in breathe-first manner:  `webb.web_crawl("your-web-page-url")
* Crawl web pages with delay of 2 seconds after every page crawled:  `webb.web_crawl("your-web-page-url",2)`


### Status
This is a small script which is ready-to-run, but still under development. Many more features will be added to it shortly.


## Disclaimer
The crawler function lets you download  and crawl tons of web pages. Please do not download and crawl any pages of a domain without reading about the robot.txt file of that domain. It is inappropriate to violate the robot.txt file. This may even lead to the domain completely blocking your crawler and thus blacklisting it. It is also not appropriate to crawl pages at high rate as it may put a lot of pressure on the server.
