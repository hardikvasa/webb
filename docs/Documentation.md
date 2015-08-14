# Webb Documentation
This is a official documentation of the **webb** library in Python

## **Step 1.** Download/Install the Library

`pip install webb`

**or**

Download the complete zip file from github, unzip it and then inside the directory type the following command from your command prompt or terminal
`python install setup.py`

**or**

1. Download `webb.py`
2. Create a new file in the same folder and give it any name like `main.py`
3. Import the webb library by writing `import webb` in the `main.py` file
4. Once this is done, use any of the following commands


## **Step 2.** Import the Library in your code
The library needs to be imported into the Python code. You can import the library by typing in the following command at the top of your codde:

`from webb import webb`

## **Step 3.** Use Commands
### Web Site Information
* Traceroute a URL:  
`webb.traceroute("your-web-page-url")`

* Traceroute a URL and store the result (log) in the text file:  
`webb.traceroute("your-web-page-url",'file-name.txt')`

* Get IP address of a webpage:  
`print(webb.get_ip("your-web-page-url"))`

* Or Save the IP address into a variable (for later usage):  
`ip = webb.get_ip("your-web-page-url")`

* Get the Whois data of a website :  
`print(webb.get_whois_data("your-web-page-url"))`

* Ping a website (ICMP Ping):  
`print(webb.ping('your-web-page-url'))`

### Downloading HTML Web Page
* Download entire HTML page and print it:  
`print(webb.download_page("your-web-page-url"))`

* Download entire HTML page and store it in a variable for further use:  
`page = webb.download_page("your-web-page-url")`

* Download entire HTML page and save it in a text file:  
`print(webb.download_page("your-web-page-url","file-name.txt"))`

### Clean/Prettify a Web Page
* Clean an HTML page by removing all the HTML tags:  
`print(webb.remove_html_tags("your-web-page"))`

* Remove/Clean All HTML tags from a Web Page (Also deletes everything between the 'script' tagg, including the tags):  
`print(webb.clean_page("your-web-page"))`

### Normalize Web Page URL
* Normalize URL (Convert Relative URL to absolute URL):  
`print(webb.url_normalize("your-relative-url","your-seed-page-url"))`

### Extracting Page Title
* Print the page title:  
`webb.page_title("your-web-page-url")`

### Extracting Links (hyperlinks)
* Find all the links in a web page and print it one below the other (by passing in URL as input):  
`webb.find_all_links('your-web-page-url')`

* Find all the links in a web page and print it one below the other (by passing in Page Content as input): 
`webb.find_all_links('page-content')`

### Extracting Headings tags from a web page
* Get all the headings (h1 or h2 or ... h6) from a given web page and print it one below the other:  
`get_all_headings("your-web-page-url","h1")`

* Get all the headings (h1 or h2 or ... h6) from a given web page and print it as list:  
`get_all_headings("your-web-page-url","h2","list")`

### Extracting Paragraphs from a web page
* Get all paragraphs of a given web page one below the other:  
`webb.get_all_paragraphs("your-web-page-url")`

* Get all paragraphs of a given web page one below the other:  
`print(webb.get_all_paragraphs_as_list("your-web-page-url"))`

### Downloading all images from a web page
* Get links of all the images in a given web page:  
`webb.get_all_images("your-web-page-url")`

* Get links of all the images in a given web page and download all those images on local disk (computer):  
`webb.get_all_images("your-web-page-url","download")`

### Crawling the Web
* Crawl web pages in breathe-first manner (Out-of-domain mode):  
`webb.web_crawl("your-web-page-url")`

* Crawl web pages with delay of 2 seconds after every page crawled (Out-of-domain mode):  
`webb.web_crawl("your-web-page-url",2)`

* Crawl an entire website with no (0 seconds) delay while writing the crawl data into a log file (Out-of-domain mode):  
`webb.web_crawl("your-web-page-url",0,"write_log")`

----------

* Crawl web pages in breathe-first manner (In-domain mode):  
`webb.web_crawl_in_domain("your-web-page-url")`

* Crawl web pages with delay of 2 seconds after every page crawled (In-domain mode):  
`webb.web_crawl_in_domain("your-web-page-url",2)`

* Crawl an entire website with no (0 seconds) delay while writing the crawl data into a log file (In-domain mode):  
`webb.web_crawl_in_domain("your-web-page-url",0,"write_log")`

### Download Google Images
* Download Google Images from keywords or list, as a list output:  
`webb.download_google_images("keyword")`  or `webb.download_google_images(['keyword 1','keyword 2','keyword 3'])`

* Download Google Images from keywords to local hard drive:  
`webb.download_google_images('keyword','download')`

### Save Wikipedia Articles
* Extract only the 'text' from a Wikipedia article and display it:  
`print(webb.save_wikipedia_article("wikipedia-article-link"))`

* Extract only the 'text' from a Wikipedia article and save it in a Text file:  
`print(webb.save_wikipedia_article("wikipedia-article-link",'file-name.txt'))`

### Wikipedia Crawler
* Crawl Wikipedia Pages by giving the starting page and number of articles (pages) to crawl as arguments:  
`print(webb.wikipedia_crawl('starting-wikipedia-page-link',number-of-pages-to-crawl))`

* Crawl Wikipedia Pages and save it to a file by giving the starting page, number of articles (pages) to crawl and file name as arguments:  
`print(webb.wikipedia_crawl('starting-wikipedia-page-link',number-of-pages-to-crawl,'file-name.txt'))`

### Google Search
* Google Search using Python and get the results with the URLs (links):  
`webb.google_search('search-query')`