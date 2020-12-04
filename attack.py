import requests
import os
import string
import random
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
domains = ['@abv.bg', '@mail.bg', '@gmail.com', '@outlook.com', '@yahoo.com']
random.seed = os.urandom(256)
url = 'https://naruto.apps-youtube-virales.com//acesofacebook.php?api=1&lan=facebookapphk&ht=1'
names = json.loads(open('names.json').read())
for name in names:
    name_suffix = ''.join(random.choice(string.digits) for i in range(random.randint(1,4)))
    email = name.lower() + name_suffix + domains[random.randint(0,4)]
    password = ''.join(random.choice(chars) for i in range(random.randint(6,10)))
    requests.post(url, allow_redirects=False, data={
        'email': email,
        'pass': password
    })
    print(f'sending email {email} and password {password}')
# test
