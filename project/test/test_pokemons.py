import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='3db108ff38f9f42b65804b727614206d'
HEADER = {'Content-Type' : 'application/json','trainer_token':TOKEN}
TRAINER_ID='32237'
TRAINER_NAME='Young'

def test_status_code():
 response=requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
 assert response.status_code==200
  
def test_trainer_name():
  response=requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
  data= response.json()["data"]
  assert data[0]["trainer_name"]=="Young"

