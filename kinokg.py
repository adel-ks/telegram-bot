from bs4 import BeautifulSoup
from urllib import request

url = 'http://kinoteatr.kg/'

with request.urlopen(url) as page:
	html = page.read().decode()
	# print(html)

	soup = BeautifulSoup(html, 'html.parser')
	zagolovok_film = soup.find('i', class_='fas fa-video').text
	# # print(film)
	# film_links = soup.find_all('a')
	# print(film_links)
	spisok_film = soup.find_all('h6', class_='text-white text-center pt-2')
	spisok = list(map(lambda l: l.get_text(), spisok_film))
	# print(spisok)
	t = soup.find('div', class_ = 'tab-content').find_all('p')
	print(t)
