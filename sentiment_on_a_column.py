import requests
import pandas as pd

#your text analysis azure key
subscription_key = ""

assert subscription_key
text_analytics_base_url = "https://westeurope.api.cognitive.microsoft.com/text/analytics/v2.0/"
language_api_url = text_analytics_base_url + "languages"
#print(language_api_url)

sentiment_api_url = text_analytics_base_url + "sentiment"
#print(sentiment_api_url)

#REPLACE WITH DOCUMENT NAME
df1 = pd.read_csv("reviews.csv")


#REPLACE WITH COLUMN NAMES
columns = ["review from client", "review from reseller"]
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}


for name in columns:
	#reset documents for formatting
	documents = {'documents':[]}
	#get all the responses from the name
	for i,count in enumerate(df1[name]):
		#create request structure for sentiment api
	  	documents['documents'].append({'id' : i+1, 'language' : "en", "text": count})
	
	#documents #the column we want to score

	#call to sentiment Api
	response  = requests.post(sentiment_api_url, headers=headers, json=documents)
	sentiments = response.json()

	#sentiments #the scores

	sentiments_list = []
	#convert the sentiment score to categories
	for i in sentiments['documents']:
		if (i['score']>0.5) :
			sentiments_list.append("positive")
		elif (i['score']<0.5) :
			sentiments_list.append("negative")
		elif (i['score']==0.5) :
			sentiments_list.append("neutral")


	#sentiments_list	#the resulting categories

	df1[name + "_sentiment"] = sentiments_list

#NAME TO SAVE AS

df1.to_csv("reviews_withsentiment.csv")



