# Requests a API de GitHub

import requests

class API():
    # ///---- Request data ----///
    def requestGet(user):
        response = requests.get(f'https://api.github.com/users/{user}')
        return response

    # ///---- Print JSON ----///
    def jsonPrint(obj):
        getData = [obj['avatar_url'], obj['login'], obj['bio'], obj['blog'], obj['public_repos']]
        return getData

# response = API.requestGet('JaviCeRodriguez')
# if response.status_code != 200:
#     print('GET {}'.format(response.status_code))
# else:
#     API.jsonPrint(response.json())