#ATTENTION ON GOOGLE STANDARD USAGE LIMITS: 
#  2,500 free requests per day, calculated as the sum of client-side and server-side queries.
#  512 locations per request.
#  50 requests per second, calculated as the sum of client-side and server-side queries. 
#  more information see https://developers.google.com/maps/documentation/elevation/usage-limits
#THE CODE BELOW OPENS ONE REQUEST PER COORDINATE!

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import time

longitudes = 	[
				-46.761025,
				-46.760485,
				-46.759945,
				-46.759405] #Insert longitudes (Ex.:-46.761025,-46.760485,-46.759945,-46.759405) 

latitudes = [
				-23.220104,
				-23.219924,
				-23.219834,
				-23.219744,
				-23.213804] #Insert latitudes (Ex.: -23.220104,-23.219924,-23.219834,-23.219744,-23.213804) 

key = "" #your Google API Key
dados = []
i = 0

for latitude in latitudes:
	for longitude in longitudes:
		time.sleep(0.05)
		coordinate = str(latitude) + ',' + str(longitude)
		html = urlopen("https://maps.googleapis.com/maps/api/elevation/json?locations=" + coordinate + "&key=" + key) #OPENS ONE REQUEST PER COORDINATE!
		data = json.loads(html.read().decode())
		elevation = data["results"][0]["elevation"]
		resolution = data["results"][0]["resolution"]
		dados.append('lat:' + str(latitude) + ',' + 'lng:' + str(longitude) + ',' + 'elevation:' + str(elevation) + ',' + 'resolution:' + str(resolution))
		print('Coordinate ' + str(i) + ' of ' + str(len(latitudes)*len(longitudes)))
		i+=1

for line in dados:
	print(line)

