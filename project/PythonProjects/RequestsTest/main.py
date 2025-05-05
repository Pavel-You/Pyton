import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='3db108ff38f9f42b65804b727614206d'
HEADER = {'Content-Type' : 'application/json','trainer_token':TOKEN}
body_registr = {
    "trainer_token": TOKEN,
    "email": "zimin2004@bk.ru",
    "password": "19072001Pz"
}
'''response=requests.post(url= f'{URL}/trainers/reg', headers=HEADER, json=body_registr )
print(response.text)'''


body_create={
    "name": "Бульбазавр",
    "photo_id": 1
}
body_confirmation={"trainer_token": TOKEN}
response=requests.post(url= f'{URL}/trainers/reg', headers=HEADER, json=body_create )
print(response.text)

body_izmenit={
    "pokemon_id": "307038",
    "name": "Бильбо",
    "photo_id": 2
}
response_create=requests.put(url=f'{URL}/pokemons', headers=HEADER, json= body_izmenit)
print(response_create.text)

body_poymat={
   "pokemon_id": "307038"
}
response_create=requests.post(url=f'{URL}/pokemons', headers=HEADER, json= body_poymat)
print(response_create.text)