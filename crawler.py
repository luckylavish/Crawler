page = '<a href="www.google.com" > </a> <a href="www.facebook..com"> </a> <a href = "www.gmail.com"> </a> <a href="www.aryacollege.in" ></a>'
def get_next_link(page):
	start_link = page.find('<a href')
	if start_link==-1:
		return None, 0
	start_quotes = page.find('"',start_link)
	end_quotes = page.find('"',start_quotes+1)
	url = page[start_quotes+1:end_quotes]
	return url,end_quotes

def print_all_links(page):
	while True:
		url,end_quotes = get_next_link(page)
		if not url==None:
			print url
			page = page[end_quotes:]
		else:
			break
print_all_links(page)
