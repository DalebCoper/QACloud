import requests
from jsonschema import validate


class Api:
    def __init__(self, url):
        self.url = url

    method = "/posts"
    id = "/1"

    def get_request(self, schema: dict):
        response = requests.get(f"{self.url}{self.method}")
        validate(instance=response.json(), schema=schema)
        return response

    def post_request(self, body: dict, schema: dict):
        response = requests.post(f"{self.url}{self.method}", json=body)
        validate(instance=response.json(), schema=schema)
        return response

    def delete_request(self):
        response = requests.delete(f"{self.url}{self.method}{self.id}")

        return response
