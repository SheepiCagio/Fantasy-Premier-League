
import requests
import json
import time

entry_id = 2691214
gw_array = []
""" Retrieve the summary/history data for a specific entry/team

Args:
	entry_id (int) : ID of the team whose data is to be retrieved
"""
base_url = "https://fantasy.premierleague.com/api/entry/"
full_url = base_url + str(entry_id) + "/history/"
response = ''
while response == '':
	try:
		response = requests.get(full_url)
	except:
		time.sleep(5)
if response.status_code != 200:
	raise Exception("Response was code " + str(response.status_code))
data = json.loads(response.text)

for x in data['current']:
	gw_array.append(x['event'])

print(gw_array)

