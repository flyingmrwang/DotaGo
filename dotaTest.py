#python2.7
import dota2api
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test_database
match_collection = db.matches

api = dota2api.Initialise("B672E808C9F51AF938E1A461C65542E2")
#hist = api.get_match_history(account_id=76482434)
match = api.get_match_details(match_id=1000193456)
match['radiant_win']

start_match_id = None

#while True:
for i in range(0, 3):
	gmh = api.get_match_history(start_at_match_id=start_match_id,
                                    skill=3,  # high and very high
                                    game_mode=2,
                                    min_players=10)
	matches = gmh['matches']
	for match in matches:
		match_id = match['match_id']

		#print("%d" % matches)
		print("%d" % match_id)
		gmd = api.get_match_details(match_id)
		match_collection.insert(gmd)
	

	last_match_id = matches[-1]['match_id'] # retrieve next batch of match
	start_match_id = last_match_id - 1
	i += 1	

#print(matches)
#f = open('workfile', 'w')
#f.write(str(matches))

