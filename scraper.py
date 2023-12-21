from requests_html import HTMLSession
# from requests_html import AsyncHTMLSession
import base64





class Scraper:
	s = HTMLSession()

	def homeThumbnail(self,page):
		print('page in scrap',page)
		url = f'https://www.discudemy.com/language/english/{page}'
		r = self.s.get(url)
		try:
			container = r.html.find(' article.cards',first=True)
			items = container.find('section.card')
			thumbData=[]
			for x in items:
				data = {}
				try:
					data['link'] = x.find('div.header > a',first=True).attrs['href']
					data['title'] = x.find('div.header > a',first=True).text
					data['poster'] = x.find('div.image > amp-img',first=True).attrs['src']
						
					thumbData.append(data)
				except Exception as e:
					continue
			
			

			pagination = r.html.find('body > div.ui.grid > div > div > ul.pagination3 > li')

			# for x in pagination:
			# 	try:
			# 		print(x.text)
			# 	except Exception  as e:
			# 		continue
			hasMore = True if pagination[-1].text.splitlines()[0] == '»' else False 
			# hasMore = isdigit(pagination[-1].text.splitlines()[0])
			return {'courses':thumbData,'page':page,'totalPages':pagination[-2].text if hasMore else pagination[-1].text, 'hasMore':hasMore}
			# print(thumbData)
			# return thumbData
			# return 'gg'


			

		except Exception as e:
			raise e


	def itemDetails(self,path):
		
		r = self.s.get(f'https://www.discudemy.com/go/{path}')
		try:
			url = r.html.find(' div.ui.segment > a',first=True).attrs['href']
		
			return url
		except Exception as e:
			raise


	def item(self,item):
		
		r = self.s.get(f'https://wat32.tv/watch/{item}.html')
		try:
			videoInfo = r.html.find(' div.marginPage',first=True)
			script = videoInfo.find('div.movieBlock > div.tabCont > script',first=True).text
			coded_string = script.split('"')[1]
			rawIframe = base64.b64decode(coded_string).decode('ascii')
			iframe = rawIframe.split(" ")[7].split("=")[1].replace('"',"")
			
		

			return iframe
		except Exception as e:
			raise
		


	def searchResult(self,term,page):

		r =  self.s.get(f'https://asianembed.io/search.html?keyword={term}&page={page}')
		ul =r.html.find('.listing',first=True)

		resultInfo=[]
		for i in ul.find('.video-block'):
			data={}
			data['link']=i.find('a',first=True).attrs['href'].split('videos')[1].replace('/','')
			data['img'] = i.find('.picture',first=True).find('img',first=True).attrs['src']
			data['name'] = i.find('.name',first=True).text.strip()
			# data['meta'] = i.find('.meta',first=True).text.strip()
			resultInfo.append(data)
		pagination = r.html.find('.pagination',first=True)
		hasMore = True if pagination.find('.next') else False
		
		print({'results':resultInfo,'page':page,'hasMore':hasMore})
		return {'results':resultInfo,'page':page,'hasMore':hasMore}






# s = Scraper()

# s.homeThumbnail()
# s.itemDetails('avataro-sentai-donbrothers-2022-episode-24')



# iframes = []	
# for link in links:
# 	r2 = s.get('https://asianembed.io/videos/avataro-sentai-donbrothers-2022-episode-24')
# 	f = r2.html.find('.play-video',first=True)
# 	iframes.append(f.find('iframe',first=True).attrs['src'])

# print(iframes)



