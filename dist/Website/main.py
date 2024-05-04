import json
import requests
#from bs4 import BeautifulSoup
a=input()
indicators={
    a
}
url='https://www.virustotal.com/vtapi/v2/url/report'

api='b780c8dd0551e47e19c0be0f0cedcc819e8322beea6d6380c8ee2c48de354d37'

for site in indicators:
    
    params={'apikey':api,'resource':indicators}
    page= requests.get(url, params=params)
    response= json.loads(page.content)

    print(response['positives'])
    print(response['total'])
    