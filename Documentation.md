## Webb Documentation
This is a official documentation of the **webb** library in Python

### Download and Install
1. Download `webb.py`
2. Create a new file in the same folder and give it any name like `main.py`
3. Import the webb library by writing `import webb` in the `main.py` file
4. Once this is done, use any of the following commands

### Web Site Information
* Traceroute a URL:  
`webb.traceroute("your-web-page-url")`

* Get IP address of a webpage:  
`webb.get_ip("your-web-page-url")`

### Downloading HTML Web Page
* Download entire HTML page:  
`print(webb.download_page("your-web-page-url"))`

### Normalize Web Page
* Normalize URL (Convert Relative URL to absolute URL):  
`print(webb.url_normalize("your-relative-url","your-seed-page-url"))`

### Extracting Page Title
* Print the page title:  
`webb.title("your-web-page-url")`

### Extracting Links (hyperlinks)
* Find all the links in a web page and print it one below the other (by passing in URL as input):  
`webb.find_all_links('your-web-page-url','link')`

* Find all the links in a pirticular web page and print it as a list (by passing in URL as input):  
`print(webb.find_all_links('your-web-page-url','link','list'))`

* Find all the URLs in a page and convert them into absolute URLs and print it (by passing in URL as input):  
`webb.find_all_links('your-web-page-url','link','absolute')`

* Find all the URLs in a page and convert them into absolute URLs and print it as a list (by passing in URL as input):  
`print(webb.find_all_links('www.zseries.in','link','absolute','list'))`

----------

* Find all the links in a web page and print it one below the other (by passing in Page Content as input): 
`webb.find_all_links(page,'content')`

* Find all the links in a pirticular web page and print it as a list (by passing in Page Content as input):  
`print(webb.find_all_links(page,'content','list'))`

* Find all the URLs in a page and convert them into absolute URLs and print it (by passing in page content as input):  
`webb.find_all_links('page-content','link','absolute','base-url')`

* Find all the URLs in a page and convert them into absolute URLs and print it as a list (by passing in Page Content as input):  
`print(webb.find_all_links(page,'content','absolute',url,'list'))`

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

### Removing all HTML tags from a web page
* Clean an HTML page by removing all the HTML tags:  
`print(webb.pure_text("your-web-page"))`

### Crawl Web pages in a systematic manner
* Crawl web pages in breathe-first manner (Out-of-domain mode):  
`webb.web_crawl("your-web-page-url")`

* Crawl web pages with delay of 2 seconds after every page crawled (Out-of-domain mode):  
`webb.web_crawl("your-web-page-url",2)`

* Crawl an entire website with no (0 seconds) delay while writing the crawl data into a log file (Out-of-domain mode):  
`webb.web_crawl("your-web-page-url",0,"write_log")`

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
