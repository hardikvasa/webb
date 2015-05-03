# Version 0.9
# Under Apache License Version 2.0
# @Hardik Vasa

#Import Libraries
import time     #For Delay calculations
import sys    #for system related information
from subprocess import Popen, PIPE
import re
import socket
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


###### Web Site Information ######   
#Get IP of a website from the URL
def get_ip(url):
    ip = socket.gethostbyname(url)
    print(ip)
    
    
#Traceroute to a website
def traceroute(url):
    while True:
        if 'http' not in url:
            url = "http://" + url
        elif "www" not in url:
            url = "www."[:7] + url[7:]
        else:
            url = url
            break
    url = urlparse(url) 
    url = url.netloc
    print(url)        
    p = Popen(['tracert', url], stdout=PIPE)
    while True:
        line = p.stdout.readline()
        line2 = str(line).replace('\\r','').replace('\\n','')
        print(line2)
        if not line:
            break
        

###### Download HTML Page Main Function ######                
#Downloading entire Web Document (Raw Page Content) for the crawler
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib.request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
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



#Extract the title tag
def title(url):
    page = download_page(url)
    start_title = page.find("<title")
    end_start_title = page.find(">",start_title+1)
    stop_title = page.find("</title>", end_start_title + 1)
    title = page[end_start_title + 1 : stop_title]
    print (title)


 

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


###### URL Normalizer for the Users ######
#URL parsing for incomplete or duplicate URLs for users
def url_normalize(url,seed_page):
    url = url.lower()    #Make it lower case
    s = urlparse(url)       #parse the given url
    seed_page = seed_page.lower()       #Make it lower case
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
    if flag == 0:
        return url
    else:
        return "Invalid URL"


###### Find all the links function for users ######
#Finding 'Next Link' on a given web page for users
def find_next_link(s):
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
          

#Getting all links as list with the help of 'get_next_links' for users
def find_all_links_as_list(url):
    page = download_page(url)
    links = []
    while True:
        link, end_link = find_next_link(page)
        if link == "no_links":
            break
        else:
            links.append(link)      #Append all the links in the list named 'Links'
            #time.sleep(0.1)
            page = page[end_link:]
    return links 



#Get all the links from the find_all_links_as_list function and print it in order for users
def find_all_links(*arg):
    url = arg[0]
    s = urlparse(url)
    if not s.scheme:
        url = "http://" + url
    t = urlparse(url)
    seed_page = t.scheme+'://'+t.netloc
    print(seed_page)
    lists = find_all_links_as_list(url)
    if len(arg)>1:
        if arg[1] == "absolute":
            for i in lists:
                i = url_normalize(i,seed_page)
                print(i)
        else:
            print("Invalid Second Argument")
    else:    
        for i in lists:
            print(i)     




###### Web Crawler Functions ######
#Finding 'Next Link' on a given web page for crawler
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
          

#Getting all links with the help of 'get_next_links' for crawler
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



#URL parsing for incomplete or duplicate URLs for crawler
def url_parse(url,seed_page):
    url = url.lower().replace(' ','%20')    #Make it lower case
    s = urlparse(url)       #parse the given url
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



#Main function that crawls the entire web (out of domain) in breath first order
def web_crawl(*arg):
    
    to_crawl = [arg[0]]      #Define list name 'Seed Page'
    crawled=[]      #Define list name 'Seed Page'
    
    a = urlparse(arg[0])
    seed_page = a.scheme+"://"+a.netloc

    i=0;        #Initiate Variable to count No. of Iterations
    while to_crawl:     #Continue Looping till the 'to_crawl' list is not empty
        urll = to_crawl.pop(0)      #If there are elements in to_crawl then pop out the first element
        
        urll,flag = url_parse(urll,seed_page)
        flag2 = extension_scan(urll)
        
        #If flag = 1, then the URL is outside the seed domain URL
        if flag2 == 1:
            pass        #Do Nothing
            
        else:       
            if urll in crawled:     #Else check if the URL is already crawled
                pass        #Do Nothing
            else:       #If the URL is not already crawled, then crawl i and extract all the links from it
                print("\n"+urll)
                if len(arg)>1:
                    delay = arg[1]
                    time.sleep(delay)
                #print(download_page(urll))
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
            i=i+1    #Iteration Counter
            
            #print(to_crawl)
            print("Iteration No. = " + str(i))
            print("Pages to Crawl = " + str(len(to_crawl)))
            print("Pages Crawled = " + str(len(crawled)))
            
            if len(arg)>1:
                if arg[2]=="write_log":
                    file = open('log.txt', 'a')        #Open the text file called database.txt
                    file.write("URL: " + urll + "\n")         #Write the title of the page
                    file.write("Iteration No. = " + str(i) + "\n")
                    file.write("Pages to Crawl = " + str(len(to_crawl)) + "\n")
                    file.write("Pages Crawled = " + str(len(crawled)) + "\n\n")
                    file.close()                            #Close the file
    return ''




#Main function crawls the entire site (in-domain) in breath first order
def web_crawl_in_domain(*arg):
    
    to_crawl = [arg[0]]      #Define list name 'Seed Page'
    crawled=[]      #Define list name 'Seed Page'
    
    a = urlparse(arg[0])
    seed_page = a.scheme+"://"+a.netloc

    i=0;        #Initiate Variable to count No. of Iterations
    while to_crawl:     #Continue Looping till the 'to_crawl' list is not empty
        urll = to_crawl.pop(0)      #If there are elements in to_crawl then pop out the first element
        
        urll,flag = url_parse(urll,seed_page)
        flag2 = extension_scan(urll)
        
        #If flag = 1, then the URL is outside the seed domain URL
        if flag == 1 or flag2 == 1:
            pass        #Do Nothing
            
        else:       
            if urll in crawled:     #Else check if the URL is already crawled
                pass        #Do Nothing
            else:       #If the URL is not already crawled, then crawl i and extract all the links from it
                print("\n"+urll)
                if len(arg)>1:
                    delay = arg[1]
                    time.sleep(delay)
                #print(download_page(urll))
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
            i=i+1    #Iteration Counter
            
            #print(to_crawl)
            print("Iteration No. = " + str(i))
            print("Pages to Crawl = " + str(len(to_crawl)))
            print("Pages Crawled = " + str(len(crawled)))
            
            if len(arg)>1:
                if arg[2]=="write_log":
                    file = open('log.txt', 'a')        #Open the text file called database.txt
                    file.write("URL: " + urll + "\n")         #Write the title of the page
                    file.write("Iteration No. = " + str(i) + "\n")
                    file.write("Pages to Crawl = " + str(len(to_crawl)) + "\n")
                    file.write("Pages Crawled = " + str(len(crawled)) + "\n\n")
                    file.close()                            #Close the file
    return ''


#Removing HTML tags from the content
def pure_text(page):
    pure_text = (re.sub(r'<.+?>', '', page))       #From '<' to the next '>'
    return pure_text




###### Extract Headings ######
#Finding 'Next Heading' on a given web page for users
def get_next_heading(s,heading_type):
    start_link = s.find("<"+heading_type)
    if start_link == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_headings"
        return link, end_quote
    else:
        start_quote = s.find('>', start_link+1)
        end_quote = s.find('</'+heading_type+'>',start_quote+1)
        link = str(s[start_quote+1:end_quote])
        return link, end_quote
          

#Getting all headings with the help of 'get_next_headings' for users
def get_all_headings_as_list(url,heading_type):
    links = []
    page = download_page(url)
    while True:
        link, end_link = get_next_heading(page,heading_type)
        link = link.replace('\n',' ')
        link = re.sub(r'<.+?>', '', link)
        if link == "no_headings":
            break
        else:
            links.append(link)      #Append all the links in the list named 'Links'
            #time.sleep(0.1)
            page = page[end_link:]
    return links 


# Get all the headings from get_all_headings_as_list
def get_all_headings(*arg):
    url = arg[0]
    lists = get_all_headings_as_list(url,arg[1])
    if len(arg)>2:
        if arg[2] == 'list':
            print(lists)     #Display all headings as list
    else:
        for i in lists:    #Display all headings one below the other
            print(i)




###### Extract Paragraphs ######
#Finding 'Next Paragraph' on a given web page for users
def get_next_paragraph(s):
    start_link = s.find("<p")
    if start_link == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_quote = s.find('>', start_link+1)
        end_quote = s.find('</p>',start_quote+1)
        link = str(s[start_quote+1:end_quote])
        return link, end_quote

          

#Getting all paragraphs with the help of 'get_next_paragraph_as_list' for users
def get_all_paragraphs_as_list(url):
    links = []
    page = download_page(url)
    while True:
        link, end_link = get_next_paragraph(page)
        link = link.replace('\n',' ')
        link = re.sub(r'<.+?>', '', link)
        if link == "no_links":
            break
        else:
            links.append(link)      #Append all the links in the list named 'Links'
            #time.sleep(0.1)
            page = page[end_link:]
    return links 

#Get all the paragraphs one below the other with the help of get_all_paragraphs_as_list for users
def get_all_paragraphs(url):
    lists = get_all_paragraphs_as_list(url)
    for i in lists:
        print(i)
        



######### Download Images From a Web Page and store it on hard drive #########        
#Finding 'Next Image Link' for get_all_images
def get_next_images_link(s):
    start_line = s.find("<img")
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_link = s.find('src=', start_line)
        end_link = s.find('"',start_link+5)
        link = str(s[start_link+5:end_link])
        return link, end_link
          


#Getting all image links with the help of 'get_next_links' for get_all_images
def get_all_images_links(url):
    page = download_page(url)
    links = []
    while True:
        link, end_link = get_next_images_link(page)
        if link == "no_links":
            break
        else:
            links.append(link)      #Append all the links in the list named 'Links'
            page = page[end_link:]
    return links 



#Download all images in hard disk
def get_all_images(*arg):
    url = arg[0]
    import urllib
    links = get_all_images_links(url)
    print(links)
    if len(arg)>1 and arg[1] == "download":
        s = urlparse(url)
        seed_page = s.scheme+'://'+s.netloc
        i = 0
        while i<len(links):
            link,flag = url_parse(links[i],seed_page)
            print("downloading --> "+link)
            try:
                file = urllib.URLopener()
                file.retrieve(link, str("img "+str(i)+".jpg"))
            except:
                pass
            i = i+1
    else:
        pass
    



############## Download Google Images ############
#Finding 'Next Image' from the given raw page for users (image search)
def get_next_image_link(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_images"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_di"')
        start_content = s.find('imgurl=',start_line+1)
        end_content = s.find('&amp;',start_content+1)
        content_raw = str(s[start_content+7:end_content])
        return content_raw, end_content
          

#Getting all links with the help of 'get_next_image_link'
def get_all_image_links(page):
    items = []
    while True:
        item, end_content = get_next_image_link(page)
        if item == "no_images":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            #time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items



#Download Image Links
def download_google_images(*arg):
    import urllib
    search_keyword = arg[0]
    result = (str(type(search_keyword)))
    if 'list' in result:
        i= 0
        while i<len(search_keyword):
            items = []
            iteration = "Item no.: " + str(i+1) + " -->" + " Item name = " + str(search_keyword[i])
            print (iteration)
            search_keywords = search_keyword[i]
            search = search_keywords.replace(' ','%20')
            
            url = 'https://www.google.com/search?q=' + search +  '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
            raw_html =  (download_page(url))
            items = items + (get_all_image_links(raw_html))
                
            print ("Image Links = "+str(items))
            print ("Total Image Links = "+str(len(items)))
            print ("\n")
            i = i+1
                
            info = open('output.txt', 'a')        #Open the text file called database.txt
            info.write(str(i) + ': ' + str(search_keyword[i-1]) + ": " + str(items) + "\n\n\n")     #Write the title of the page
            info.close()                            #Close the file      
    else:
        items = []
        iteration = "Item name = " + str(search_keyword)
        print (iteration)
        search = search_keyword.replace(' ','%20')
        
        url = 'https://www.google.com/search?q=' + search +  '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
        raw_html =  (download_page(url))
        items = items + (get_all_image_links(raw_html))
            
        print ("Image Links = "+str(items))
        print ("Total Image Links = "+str(len(items)))
        print ("\n")
            
        info = open('output.txt', 'a')        #Open the text file called database.txt
        info.write(str(search_keyword) + ": " + str(items) + "\n\n\n")         #Write the title of the page
        info.close()                            #Close the file


        if len(arg)>1 and arg[1] == "download":
            i = 0
            while i<len(items):
                link = items[i]
                try:
                    file = urllib.URLopener()
                    file.retrieve(link, str("img "+str(i)+".jpg"))
                    print("downloaded --> "+ link)
                except:
                    pass
                i = i+1
        else:
            pass


########## End ##########
