import requests
#from pprint import pprint

class wea:
	def __init__(self,city):
		self.city1 =city
	def find_data(self):
		url = "http://api.weatherstack.com/current?access_key=725802fc461e09fb760b6f70b90e0534&query={}".format(self.city1)
		data = requests.get(url).json()
		#print(data)
		temp= data["current"]["temperature"]
		humid=data["current"]["humidity"]
		if(data["current"]["is_day"]=='yes'):
			is_day="Day"
		else:
			is_day="Night" 
		pressure =data["current"]["pressure"]
		wind_dir =data["current"]["wind_dir"]
		wind_mph =data["current"]["wind_speed"]
		wind_deg=data["current"]["wind_degree"]
		# News ones
		local_time= data["location"]["localtime"]# Edited 
		precipitation= data["current"]["precip"]
		cloud_cover= data["current"]["cloudcover"]
		img= data["current"]["weather_icons"]
		uv_index= data["current"]["uv_index"]
		#gust_kph =data["current"]["gust_kph"]# Edited
		observation_time= data["current"]["observation_time"] 
		lat=data["location"]["lat"]
		lon =data["location"]["lon"]
		count=data["location"]["country"]
		return({"temp":temp,"humidity":humid,"is_day":is_day,"pressure":pressure,
			"wind_dir":wind_dir,"local_time":local_time,"wind_speed":wind_mph,
			"wind_deg":wind_deg,"wind_dir":wind_dir,"local_time":local_time,"precipitation":precipitation,"cloud_cover":cloud_cover,"image": img,
			"uv_index":uv_index, "observation_time": observation_time,"is_day":is_day,"lat":lat,"lon":lon,"count":count})