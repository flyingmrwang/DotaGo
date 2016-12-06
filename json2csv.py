#python2.7
import dota2api
import json


api = dota2api.Initialise("B672E808C9F51AF938E1A461C65542E2")
#hist = api.get_match_history(account_id=76482434)
#match = api.get_match_details(match_id=1000193456)
#match['radiant_win']

start_match_id = None


#while True:
with open('test1.csv', 'w') as f:
	for i in range(0, 1):    # number of matches: 10 * 100
		gmh = api.get_match_history(start_at_match_id=start_match_id,
                                    skill=3,  # high and very high
                                    game_mode=2,
                                    min_players=10,                                 
                                    )
		matches = gmh['matches']
		for match in matches:
			match_id = match['match_id']
			radiant_win = api.get_match_details(match_id=match_id)['radiant_win']
			win = int(radiant_win);
			print("%d" % match_id)		
			
			json.dump(win, f)
			f.write(",")
			players = match['players']
			for player in players:
				hero_id = player['hero_id']
				#print("	%d" % hero_id)
				json.dump(hero_id, f)
				f.write(",")
				print("%d" % hero_id)
			f.write("\n")


		
	last_match_id = matches[-1]['match_id'] # retrieve next batch of match
	start_match_id = last_match_id - 1
	i += 1	

#print(matches)
#f = open('csvMatches', 'w')
#f.write(str(matches))


#save json file
#with open('data.txt', 'w') as outfile:
 #   json.dump(data, outfile)
#create table1 test (match_id int,hero1 int, hero2 int, hero3 int, hero4 int, hero5 int, hero6 int, hero7 int, hero8 int, hero9 int, hero10 int,primary key(m
#atch_id) );
