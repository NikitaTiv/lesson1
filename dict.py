dict = {"city": "Москва", "temperature": 20}
print(dict['city'])
dict["temperature"] -= 5
print(dict)
print(dict.get('country'))
print(dict.get('country', 'Russia'))
dict['date'] = '27.05.2019'
print(len(dict))