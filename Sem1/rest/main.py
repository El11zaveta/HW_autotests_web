import requests
import yaml

with open("confing.yaml") as f:
    data = yaml.safe_load(f)

def login():
    response = requests.post(data['website1'], data={'username': data['username'], 'password': data['password']})
    if response.status_code == 200:
        return response.json()['token']


def get_post(token):
    response = requests.get(data['website2'], headers={'X-Auth-Token': token}, params={"owner": "notMe"})
    if response.status_code == 200:
        return response.json()


if __name__ == '__main__':
    print(get_post(login()))