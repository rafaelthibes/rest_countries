import requests
import json
import pyautogui as pd
import subprocess
#API restcountries
#https://restcountries.com/v3.1/all

#Capturando informação sobre um país específico pelo nome
#countrie_name = input('Digite o nome do país: ')
pais = pd.prompt('Insira o nome do país: ')
requisicao = requests.get('https://restcountries.com/v3.1/name/{}'.format(pais))#.format(countrie_name))
countrie_list = requisicao.json()#Temos uma lista de dicionarios
#print(countrie_list[0]['name']) #Puxando informação isolada

#Verificando nome das chaves do dicionario
for key in countrie_list:
    list_of_keys = key.keys()
#print (list_of_keys)

#Após analisado a lista list_of_keys, foi colocado as chaves relevantes em uma nova lista
list_keys_final = ['name','currencies','capital','altSpellings','region','subregion','languages','borders','area','maps','population','timezones','flags','coatOfArms']

#looping para adicionar as chaves da lista e seus valores 
i = 1
list_values_final = []
while i < 14:
    list_values_final.append(countrie_list[0][list_keys_final[i]])
    i = i + 1

#Criação do arquivo final
i = 0
for i, list in enumerate(list_values_final):
    list = str(list)
    list_str = ('{}\n'.format(list))
    with open('informacoes_paises.txt','a') as informacoes_paises:
        informacoes_paises.write(list_str)

subprocess.run(['notepad.exe','informacoes_paises.txt'])