import requests
import pymongo

# Finds the strings between two substrings
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

# Use requests to get the page source
url = "https://electronic.vegas/vegas-edm-event-calendar/"
response = requests.get(url)


event_title = []
event_date = []
#Only look for particular lines
for line in response.content.split('\n'):
	if 'wideeventDate' in line:
		event_date.append("".join(find_between(line,"'wideeventDate'>"," at ").split()[1:]))
	if 'wideeventTitle' in line:
		event_title.append("".join(find_between(line,"itemprop='name'>","</span>")))

min_val = 0
max_val = len(event_date)

# Consolidate the event titles and event dates
mongo_document = {}
while (min_val < max_val):
	if event_date[min_val] not in mongo_document:
		mongo_document[event_date[min_val]] = []
	mongo_document[event_date[min_val]].append(event_title[min_val])
	min_val = min_val +1

# Connect to mongo
mongo = pymongo.MongoClient()
event_collection = mongo['event_db']['event_collection']

# Maps 3 letter months to a numeric number
month_mapping = {
	"Jan":1,
	"Feb":2,
	"Mar":3,
	"Apr":4,
	"May":5,
	"Jun":6,
	"Jul":7,
	"Aug":8,
	"Sep":9,
	"Oct":10,
	"Nov":11,
	"Dec":12
}

# Mongo Insertion
for document in mongo_document:
	date_split = document.split('.')[0]
	numeric_month = month_mapping[date_split]
	full_date = document.replace(date_split,str(numeric_month)).replace('.','-').replace(',','-')
	event_collection.update({'_id':full_date},{'events':mongo_document[document]},upsert=True)


