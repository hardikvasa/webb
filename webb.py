#!/usr/bin/env python
#Version 0.8 [Upgraded the URL parser to remove unwanted fragments, queries and non web documents as links]
#@Hardik Vasa

#Import Libraries
import time     #For Delay
import sys    #for system related information

# This is the first page from where the crawler starts crawling
reference_seed_page = "http://www.zseries.in"     #Defining the seed URL (should be with a prefix, netloc and scheme and without path)


#Downloading entire Web Document (Raw Page Content)
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib.request    #urllib library for Extracting web pages
        opener = urllib.request.FancyURLopener({})
        try:
            open_url = opener.open(url)
            page = str(open_url.read()).replace('\\n', '')
            return page
        except Exception as e:
                print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page    
        except:
            return"Page Not found"


#Finding 'Next Link' on a given web page
def get_next_link(s):
    start_link = s.find("<a href")
    if start_link == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_quote = s.find('"', start_link)
        end_quote = s.find('"',start_quote+1)
        link = str(s[start_quote+1:end_quote])
        return link, end_quote
          

#Getting all links with the help of 'get_next_links'
def get_all_links(page):
    links = []
    while True:
        link, end_link = get_next_link(page)
        if link == "no_links":
            break
        else:
            links.append(link)      #Append all the links in the list named 'Links'
            #time.sleep(0.1)
            page = page[end_link:]
    return links 


#Check for URL extension so crawler does not crawl images and text files
def extension_scan(url):
    a = ['.png','.jpg','.jpeg','.gif','.tif','.txt']
    j = 0
    while j < (len(a)):
        if a[j] in url:
            #print("There!")
            flag2 = 1
            break
        else:
            #print("Not There!")
            flag2 = 0
            j = j+1
    #print(flag2)
    return flag2


#URL parsing for incomplete or duplicate URLs
def url_parse(url):
    try:
        from urllib.parse import urlparse
    except ImportError:
        from urlparse import urlparse
    url = url.lower()    #Make it lower case
    s = urlparse(url)       #parse the given url
    seed_page = reference_seed_page.lower()       #Make it lower case
    t = urlparse(seed_page)     #parse the seed page (reference page)
    i = 0
    while i<=7:
        if url == "/":
            url = seed_page
            flag = 0  
        elif not s.scheme:
            url = "http://" + url
            flag = 0
        elif "#" in url:
            url = url[:url.find("#")]
        elif "?" in url:
            url = url[:url.find("?")]
        elif s.netloc == "":
            url = seed_page + s.path
            flag = 0
        elif "www" not in url:
            url = "www."[:7] + url[7:]
            flag = 0
            
        elif url[len(url)-1] == "/":
            url = url[:-1]
            flag = 0
        elif s.netloc != t.netloc:
            url = url
            flag = 1
            break        
        else:
            url = url
            flag = 0
            break
        
        i = i+1
        s = urlparse(url)   #Parse after every loop to update the values of url parameters
    return(url, flag)


     
t0 = time.time()
#Main Crawl function that calls all the above function and crawls the entire site sequentially
def web_crawl():
    
    to_crawl = [reference_seed_page]      #Define list name 'Seed Page'
    crawled=[]      #Define list name 'Seed Page'
    
    i=0;        #Initiate Variable to count No. of Iterations
    while to_crawl:     #Continue Looping till the 'to_crawl' list is not empty
        urll = to_crawl.pop(0)      #If there are elements in to_crawl then pop out the first element
        urll,flag = url_parse(urll)
        flag2 = extension_scan(urll)
        
        #If flag = 1, then the URL is outside the seed domain URL
        if flag == 1 or flag2 == 1:
            pass        #Do Nothing
            
        else:       
            if urll in crawled:     #Else check if the URL is already crawled
                pass        #Do Nothing
            else:       #If the URL is not already crawled, then crawl i and extract all the links from it
                print(urll)
                print(download_page(urll))
                to_crawl = to_crawl + get_all_links(download_page(urll))
                crawled.append(urll)
                
                #Remove duplicated from to_crawl
                n = 1
                j = 0
                #k = 0
                while j < (len(to_crawl)-n):
                    if to_crawl[j] in to_crawl[j+1:(len(to_crawl)-1)]:
                        to_crawl.pop(j)
                        n = n+1
                    else:
                        pass     #Do Nothing
                    j = j+1
            i=i+1
            
            print(to_crawl)
            print("Iteration No. = " + str(i))
            print("To Crawl = " + str(len(to_crawl)))
            print("Crawled = " + str(len(crawled)))
    return to_crawl, crawled

crawl_data = web_crawl()
print (crawl_data)
t1 = time.time()
total_time = t1-t0
print(total_time)
