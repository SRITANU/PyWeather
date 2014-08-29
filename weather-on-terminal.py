#!/usr/bin/env python

#Copyright - Sritanu Chakraborty -- sritanu25@gmail.com

import sys
import requests


def get_ip():
	"""
	Reads the ip address of the machine from the above url and stores into data as a string
	"""
	
	url = "http://bot.whatismyipaddress.com/"
	data = requests.get(url)
	link = data.text	
	return link
	
def api_key():
	"""
	Reads the key from the file and stores it in a variable
	"""
	fobj = open('./key.txt')
	api_key = fobj.readline().strip('\n')
	fobj.close()
	return api_key

def get_weather(ip_address):
	"""
	The weather forecast details will be collected from worldweatheronline.com
	"""
	key = api_key()
	end_point = "http://api.worldweatheronline.com/free/v1/weather.ashx?" 
	#query=ip-address of the machine,format=json,number of days=0,key = individual account key
	query = "q=" + str(ip_address) + "&format=json&num_of_days=0&key=" +key
	#The entire call consists of the end-point and query
	url = end_point + query
	r = requests.get(url)#data is the dictionary to which the retrieved dictionary is assigned
	data = r.json()
	current_weather = data['data']['current_condition'][0]#fetches just the current condition from the dictionary
	return current_weather


def print_weather(weather):
	print """
	Weather : %s
	Temperature : %s Celsius
	Wind : %s Kmph 
	Wind Direction : %s
	Humidity : %s
	Precipitation : %s MM
	""" % (weather['weatherDesc'][0]['value'], weather['temp_C'], weather['windspeedKmph'], weather['winddir16Point'], weather['humidity'], weather['precipMM'])



result = get_ip()
weather = get_weather(result)
#print weather
print "The weather is as follows:"
print_weather(weather)


