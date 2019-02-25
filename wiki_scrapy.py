# Setup and params
import requests
import bs4

prefix="https://en.wikipedia.org/wiki/"
title='sample'
suffix=title.replace(" ","_")
url = prefix + suffix



def wiki_scrape(article_list=['My Chemical Romance'], char=['Genres'],outfile='wiki_scrape'):
	
	""" A function to scrape basic wikipedia data quickly

	Arguments:
	article_list -- A list of strings of article titles
	char -- A list of the characteristics you want to scrape. These are categories in the box on the right hand side 
	outfile -- The name of the file stem for the output and error log.
	"""

	open(outfile+'.csv','w').close()
	open(outfile+'_errors.log','w').close()

	
for article in article_list:
		char_count= [0]*len(char)
		suffix=article.replace(" ","_")
		url = prefix + suffix

		soup=bs4.BeautifulSoup(requests.get(url).text, 'lxml')
		
		# Find the info table
		table= soup.find('table')
		wiki_dict={}

		rows=table.find_all('tr')
		for row in rows:
			row_title=row.find('th')
			try:
				if row_title.text in char:
					wiki_dict[row.find('th').text]=row.find('td').text
					char_count[char.index(row_title.text)]=1

			except:
				pass

		with open(outfile+'.csv', "a") as wfile:
			article_output= '"'  + article + '","' + url + '","' + str(wiki_dict) + '"'
			wfile.write(str(article_output)+ "\n")

		if char_count != [1]*len(char):
			with open(outfile+'_errors.log', "a") as wfile:
				for count in char_count:
					if count == 0:
						wfile.write("Error: Couldn't find " + \
									"'" + char[char_count.index(count)] + "'"+ \
									" for " + "'" + article + "'" + "\n")