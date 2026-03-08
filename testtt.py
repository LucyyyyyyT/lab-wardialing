import requests

try:
    r = requests.get('http://175.45.176.10', timeout=5)
    print('r.status_code=', r.status_code)

except requests.exceptions.ConnectTimeout:
    print('Connection timed out')