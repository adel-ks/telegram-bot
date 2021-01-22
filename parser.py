from bs4 import BeautifulSoup
from urllib import request

url = 'https://bishkek.kinoafisha.info/movies/?liststyle=list'

with request.urlopen(url) as page:
	html = page.read().decode()
	# print(html)

	soup = BeautifulSoup(html, 'html.parser')
	film = list(map(lambda a: a.find(class_='link-filmShort').text, soup.find_all(class_='filmShort')))
	# print(film)


	annotation_title = soup.find('div', class_='filmInfo_descTitle')
	# annotation_title = list(map(lambda div: div.find(class_='filmInfo_descTitle').text, soup.find_all(class_='filmInfo_desc layer-nested outer-mobile gamma-main')))
	print(annotation_title)

	# film_links = soup.find_all('a')
	# annotation_title = list(map(lambda h: h.find(class_='hat_title').text, soup.find_all(class_='hat_content')))
	# for link in film_links:
		# if 'movies' in link.get('href') and 'video' not in link.get('href') and 'archive' not in link.get('href') and 'liststyle' not in link.get('href'):
		# 	annotation_link = link.get('href')
		# 	# print(annotation_link)
		# 	annotation = request.urlopen(annotation_link)
		# 	annotation_html = annotation.read().decode()

		# 	soup_annotation = BeautifulSoup(annotation_html, 'html.parser')

		# 	annotation_title = list(map(lambda h: h.find(class_='hat_title').text, soup.find_all(class_='hat_content')))
			

			# annotation = soup.find('div', class_="filmInfo_descEditor visualEditorInsertion").find_all('p')
			# annotation_text = list(map(lambda p: p.find('p').text, soup.find_all(class_="filmInfo_descEditor visualEditorInsertion")))
			# annotation_text = list(map(lambda p: p.find(class_="filmInfo_descEditor visualEditorInsertion").text, soup.find_all(class_="filmInfo")))
			# print(annotation_text)
			# annotation_id = annotation_link.split('/')[-2].replace('movies','').replace('video','').replace('archive','')  
			# # print(annotation_id)
			# annotation = soup.find('h3', class_="subMenu_name")
			# print(annotation)
			# title_annotation = annotation.get_text()
			# f_annotation = open(f'afisha\\{annotation_id}.txt','w', encoding='utf-8')

			# f_annotation.

		
		