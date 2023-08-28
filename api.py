import requests

# url = 'https://api-customer-038j.onrender.com/customer'

# response = requests.get(url)
# print(response.json())
# print(response.json()[0]['name'])

url = 'https://api-customer-038j.onrender.com/customer/'

# response = requests.post(url, json={'name': 'Mark','age': 24, 'order': 'Food'})
# print(response.status_code)

# response = requests.get(url)
# print(response.status_code)
# print(response.json())

# to change a name from the data in the json:
# url = 'https://api-customer-038j.onrender.com/customer/7/'
# response = requests.put(url, json={'name': 'Aisha', 'age': '19', 'order': 'Mango smoothie'})
# print(response.status_code)

# PUT(you don't have to change all the fields like PUT)
# url = 'https://api-customer-038j.onrender.com/customer/3/'

# response = requests.patch(url, json={'name':'John'})

# print(response.status_code)

# DELETE
# url = 'https://api-customer-038j.onrender.com/customer/12/'

# response = requests.delete(url)

# print(response.status_code)

response = requests.post(url, json={'name': 'Yusrah','age': 25, 'order': 'Rice'})
print(response.status_code)
