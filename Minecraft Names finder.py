# Ceci est un script pour fait par BlobIsBack (github)
# Ce script peut contenir des erreurs, si c'est le cas faite une issue et/ou un pull request

import requests
import time
error = 0
var = 0
doublons = 0
list = []
used = []
for i in range(1500):
	sleep_time = 0.5
	url = requests.get('https://random-word-form.herokuapp.com/random/noun/')
	
	response = str(url.json()).replace('"', '').replace("'", "").replace('[',"").replace(']',"").replace('-',"").replace('-',"").replace('.',"").replace(' ', "")
	if response not in used and int(len(response)) >= 3 and int(len(response)) <= 16:
		used.append(response)
		apimojang = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{response}')
		if apimojang.status_code == 404:
				print(response + " est un pseudo disponible")
				list.append(response)
				var = var + 1
		elif apimojang.status_code == 429:
			print("trop de requetes, 5 secondes de pause")
			time.sleep(5)
			apimojang = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{response}')
			if apimojang.status_code == 404:
					print(response + " est un pseudo disponible")
					list.append(response)
					var = var + 1
			else:
					print("le pseudo " + response + " n'est pas disponible ou une erreur est survenue. (code 200 = pseudo indisponible)" + " code " + str(apimojang.status_code))
		else:
			print(response + " est un pseudo indisponible")
	else:
		print(f"le pseudo {response} a deja ete testé ou est invalide")
		doublons = doublons + 1
		print(doublons)
		sleep_time = 0
	time.sleep(sleep_time)
print('')
print("recherche finie, " + str(var) + " pseudos on été trouvés")
print("")
print("pseudo disponible ou bientot disponible (sauf exeptions) : " + str(set(list)).replace('{', "").replace('}', "").replace("'", "")) # en cas de liste vide, set() est affiché


# Random words lists
# https://random-word-api.herokuapp.com/word?lang=en
# https://random-word-form.herokuapp.com/random/noun/
