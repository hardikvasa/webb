import webb

page = webb.download_page("http://www.zseries.in")
print(page)
clean_page = webb.clean_html_tags(page)
print('Clean Page: '+ clean_page)
