print('Read api')

import requests 

paginaresults = requests.get('https://catfacts.ninja/facts')
feitjes = paginaresults.json()
print(feitjes)
print(fetjes["data"][0])