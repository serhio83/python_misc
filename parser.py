#!/usr/bin/env python3
import requests

req = requests.post(
	"http://localhost:8000/api/v0/token-auth/",
	json={
		'username': 'username',
		'password': 'password2017'
	})

offers = requests.get(
	"http://localhost:8000/api/v0/requests/",
	headers={'Authorization': "JWT "+req.json()['token']}
)

print()
print('JSON response first result:')
print(offers.json()['results'][0])
print()

print('Requests list:')
for i in offers.json()['results']:
	print('\t{}'.format(i['title']))

print()
print('Comments list:')
for i in offers.json()['results']:
	print('\t{}'.format(i['comment'][0:100]))
