import requests
import os
import client
import queries

appended_url = '/raw/master/package.json'

def get_package_json(url):
    url = url + appended_url
    print(url)
    try:
        response = requests.get(url, headers=client.get_headers())
        print(response.json())
    except:
        print(e)
        print(response.headers)

# test = {
#     'data': {
#         'search' : {
#             'edges' : [
#                 { 'node' : 'url'},
#                 { 'node' : 'banana'},
#                 { 'node' : 'foo'},
#                 { 'node' : 'girl'},
#             ]
#         }
#     }
# }

def destructure_data(data):
    return list(x['node'] for x in data['data']['search']['edges'])

def format_urls(data):
    return list("{}{}".format(x['url'], appended_url) for x in data)

data = client.run_query(queries.get_100_githubs)
destructured = destructure_data(data)
urls = format_urls(destructured)
print(urls)
