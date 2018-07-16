import requests
import os
# constants
token = os.environ.get('token')

# get headers for requests to github.com
def get_headers():
    return {
    "Authorization" : "token {}".format(token)
    }

headers = get_headers()

# run a graphql query
def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
