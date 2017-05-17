from __future__ import absolute_import, print_function
import pyowm 
import tweepy
import time

def tweetWeather():
	# Search for current weather in Mississauga (My hometown)
	observation = owm.weather_at_place('Mississauga,Ca')
	w = observation.get_weather()

	# Weather details
	print ("The status of the sky is:",w.get_status() ) #If it cloudy/rainy/etc..
	wstatus = "Sky status: " + w.get_status()

	print ("The wind speed is:",w.get_wind().get('speed') )#Interested just in the speed of the wind!
	wind =  "Wind speed: " + str(w.get_wind().get('speed'))

	print ("The humidity is:",w.get_humidity() )#Interested in the humidity
	humidity = "Humidity: " + str(w.get_humidity() )

	print ("The temperature is currently:",w.get_temperature('celsius').get('temp') ) #Just interested in the current temperature
	temp = "Current Temp: " + str(w.get_temperature('celsius').get('temp') )
	
	nl = str('\n')
	final = wstatus + nl + wind + nl + humidity + nl + temp #add up all the strings we wanna tweet! 
	# If the application settings are set for "Read and Write" then
	# this line should tweet out the message to your account's
	# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
	api.update_status(status=final)
	time.sleep(3600) #Runs this function every hour! 

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="CU7WQWPVfgrPR8KXUH7Gv5ZP9"
consumer_secret="7wD9ZEoJVVmbsvN8GfKpSf79yS6VFIETm9rKe9EP4gdIfG0rV9"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="813887388938338304-Wc1FCeP0wTg5YsoO0GlK5r1HV60YSzk"
access_token_secret="MtcLIdi4XVL22nvXXd2EbWIgRBMnv55c53VDfQLLfpdkJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#My API key for the weather
API_key = 'dc41de15402a02c510319c594b612419'
owm = pyowm.OWM(API_key)
api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)


while True:
	tweetWeather()