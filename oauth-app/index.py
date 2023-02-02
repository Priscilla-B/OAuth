import os
import requests
import json
from dotenv import load_dotenv


load_dotenv()

def api_request(url, post=False, headers={}):
    default_headers = {
        'Accept': 'application/vnd.github.v3+json, application/json',
        'User-Agent': 'https://example-app.com/'
    }

    if 'access_token' in headers:
        default_headers['Authorization'] = 'Bearer ' + headers['access_token']
    headers = default_headers

    if post:
        response = requests.post(url, headers=headers, data=json.dumps(post))
    else:
        response = requests.get(url, headers=headers)

    return response.json()

url = "http://localhost:5000/"

github_client_id = os.environ.get('GITHUB_CLIENT_ID')
github_client_secret = os.environ.get('GITHUB_CLIENT_SECRET')
print(github_client_secret)

#  url to get a user's authorization
authorize_url = 'https://github.com/login/oauth/authorize'

# endpoint to request an access token
token_url = 'https://github.com/login/oauth/access_token'

# github base url for api requests
api_url_base = 'https://api.github.com/'

# url for this script, used as the redirect url
base_url = 'https://' + os.environ.get('HOST_NAME', 'localhost') + '/'

# start a session so we have a place to store things between redirects
session = requests.Session()