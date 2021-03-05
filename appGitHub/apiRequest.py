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