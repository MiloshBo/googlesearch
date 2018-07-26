#! python3
# lucky1.py - Opens several Google search results.
  
import webbrowser
import bs4 
import requests
import sys
 
def my_func(search_str):
    print('Googling...') # display text while downloading the Google page
    url = 'http://google.com/search?q=' + ' '.join(search_str)
    print(f'url: {url}')
    res = requests.get(url)
    print(res.status_code)
  
    # Retreive top search result links.
    soup = bs4.BeautifulSoup(res.text, "html.parser")
  
    # Open a browser tab for each result
    linkElems = soup.select('.r a')
    for link in linkElems:
        print(f'link: {link}')
    numOpen = min(5, len(linkElems))
    for i in range(numOpen):
        webbrowser.open('http://google.com' + linkElems[i].get('href'))
 
def test_it(args):
    print(args[1:])
    my_func(args[1:])
  
if __name__ == '__main__':
    test_it(sys.argv)