import scrapy
from scrapy.http import Request

class lyricsFetch(scrapy.Spider):
	name = "lyricsFetch"
	allowed_domains = ["www.lyricsmode.com/lyrics"]
	
	print "\nEnter the name of the ARTIST of the song for which you want the lyrics for. Minimise the spelling mistakes, if possible."
	artist_name = raw_input('>')
	
	print "\nNow comes the main part. Enter the NAME of the song itself now. Again, try not to have any spelling mistakes."
	song_name = raw_input('>')
	
	
	artist_name = artist_name.replace(" ", "_")
	song_name = song_name.replace(" ","_")
	first_letter = artist_name[0]
	print artist_name
	print song_name
	
	start_urls = ["http://www.lyricsmode.com/lyrics/"+first_letter+"/"+artist_name+"/"+song_name+".html" ]
	
	print "\nParsing this link\t "+ str(start_urls)
	handle_httpstatus_list = [404]
	
	# def start_requests(self):
		# yield Request(str(self.start_urls))	
		
	#def make_requests_from_url(self,start_urls):
		#return Request(str("http://www.lyricsmode.com/lyrics/"+artist_name[0]+"/"+artist_name+"/"+song_name+".html"))
		
		
	def parse(self, response):
		
		lyrics = response.xpath('//p[@id="lyrics_text"]/text()').extract()
		
		with open ("lyrics.txt",'wb') as lyr:
			lyr.write(str(lyrics))
		
		#yield lyrics
		
		print lyrics