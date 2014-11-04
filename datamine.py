import urllib.request
import time
import sys
import os
 
# based on code found here: http://digitalpbk.com/stock/google-finance-get-stock-quote-realtime 
class GoogleFinanceAPI:
	def __init__(self):
		self.prefix = "http://finance.google.com/finance/info?client=ig&q="
	
	def get(self,symbol,exchange):
		url = self.prefix+"%s:%s"%(exchange,symbol)
		u = urllib.request.urlopen(url)
		content = u.read()
		content = content.decode()
		content = content.split()
		content = content[16]
		content = content.strip('"')
		return content
		
		
if __name__ == "__main__":
	#this takes amrket abreviations as arguments
	arr = sys.argv[1:]
	for str in arr:
		if not os.path.exists(str):
			os.makedirs(str)
	while 1:
		#wait till market opens if nescessary
		if(int(float(time.strftime("%H")))<14):
			h=int(float(time.strftime("%H")))
			m=int(float(time.strftime("%M")))
			time.sleep((14-h-1)*60*60+(60-m)*60)
			
		c = GoogleFinanceAPI()
		file=[]
		date = time.strftime("%d-%m-%y")
		
		#at start of new day create a new file for the data
		for i in range(len(arr)):
			phile=open(arr[i]+"/"+arr[i]+date, "w")
			file.append(phile)
		
		#get data and save it to file till market closes
		while 21>int(float(time.strftime("%H"))):
			for i in range(len(file)):
				quote = c.get(arr[i],"NASDAQ")
				print(arr[i] +": " +quote)
				file[i].write(quote+'\n')
			time.sleep(60)
			
		#at end of day close all files
		for i in range(len(arr)):
			file[i].close()
		#sleep till tomorrow
		time.sleep(60*60*9)