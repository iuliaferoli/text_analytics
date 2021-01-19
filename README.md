# Text Analytics Notebook going over a few examples of using Azure Cognitive Services with python
The modules used are tanslator (language detections, translation) and text analytics (sentiment analysis, key phrase extractoin).

This noteboook is used in a blog for a bigger solution here: https://iuliaferoli.medium.com/saving-santas-it-architecture-with-ai-and-cognitive-services-d001ac6027dd?source=friends_link&sk=9f3515334056e719eca8dd7ee8d62c62


# The sentiment on a column modlue 
This program presents a solution for running sesntiment analysis on columns of a csv file / dataframe and creating sentiment binary results from free text columns. Can be used to get a quick overview of text fileds in a more processing-friendly way or to use for visualization. Threshold can be adjusted or the raw sentiment score can be used - the positive/negative threshold is just used for a quick example. See review.csv for example of csv format required
