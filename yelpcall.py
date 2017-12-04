import requests

app_id = 'S2UiFyeTpuc7JjxjbUe3Mw'
app_secret = 'xiA1qJv3t7vzPBjUPlhAekrVvcnzZ3ey00BViO6i5aj7Sxli3zS3r9TLNNhHvicC'
data = {'grant_type': 'client_credentials',
        'client_id': app_id,
        'client_secret': app_secret}
token = requests.post('https://api.yelp.com/oauth2/token', data=data)
access_token = token.json()['access_token']
url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': 'bearer %s' % access_token}
params = {'location': 'San Bruno',
          'term': 'Japanese Restaurant',
          'pricing_filter': '1, 2',
          'sort_by': 'rating'
         }

resp = requests.get(url=url, params=params, headers=headers)

import pprint
pprint.pprint(resp.json()['businesses'])
