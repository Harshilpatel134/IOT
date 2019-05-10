#!/usr/bin/python3
import time
import requests
from Adafruit_IO import Client

aio = Client('harshil134','10b24a41527946d9aa40eb69770493b5')

while True:
	
	r = requests.get('https://api.thingspeak.com/channels/777903/feeds.json?api_key=KPCH666RAF9ZPY3U&results=2')
	for row in r.json()['feeds']:
		feed = aio.feeds('pressure')
		aio.send_data(feed.key, float(row['field1']))
		time.sleep(2)
		feed = aio.feeds('altitude')
		aio.send_data(feed.key, float(row['field2']))
		time.sleep(2)
		feed = aio.feeds('concentration')
		aio.send_data(feed.key, float(row['field3']))
		time.sleep(2)
		feed = aio.feeds('light')
		aio.send_data(feed.key, float(row['field4']))
		time.sleep(2)
		feed = aio.feeds('humidity')
		aio.send_data(feed.key, float(row['field5']))
		time.sleep(2)
		feed = aio.feeds('temp')
		aio.send_data(feed.key, float(row['field6']))
		time.sleep(2)
		feed = aio.feeds('vsig')
		aio.send_data(feed.key, float(row['field7']))
		time.sleep(2)
		feed = aio.feeds('bpm')
		aio.send_data(feed.key, float(row['field8']))
		time.sleep(2)
	
	time.sleep(60)
