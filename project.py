# user input
# dynamic URL 
# Fetch Data 
# print json()
# convert JSON to dictionary
# print Data

import requests 

while True : 
    user = str(input('Please Enter Name :'));
    data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{user}')
    if(data.status_code == 200) :
        pokemon = data.json()
        print(pokemon['forms'])
    else : 
        print('Please Enter a Valid Name')