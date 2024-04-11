# Ceci est un script pour fait par BlobIsBack (github)

import requests
import time
print("recherche de pseudo disponible parmis 100 mots aleatoire (doublons possible lors du choix des mots)")
var = 0
list = []
for i in range(100):
	url = requests.get('https://random-word-form.herokuapp.com/random/noun/')
	response = str(url.json()).replace('"', '').replace("'", "").replace('[',"").replace(']',"").replace('-',"").replace('-',"")
	apimojang = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{response}')
	if apimojang.status_code == 404:
		print(response + " est un pseudo disponible")
		list.append(response)
		var = var + 1
	elif apimojang.status_code == 429:
		print("trop de requetes, 10 secondes de pause")
		time.sleep(10)
	else:
		print(response + " est un pseudo indisponible")
	time.sleep(0.2)
print('')
print("recherche finie, " + str(var) + " pseudos on été trouvés")
print("")
print("pseudo disponible ou bientot disponible (sauf exeptions) : " + str(set(list))) # en cas de liste vide, set() est affiché


# Random words lists
# https://random-word-api.herokuapp.com/word?lang=en
# https://random-word-form.herokuapp.com/random/noun/
