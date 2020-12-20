import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again')
    return res


def read_res(response):
    print(response.text)

# check pw if it exists in API response


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5chars, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5chars)
    print(response)
    return read_res(response)


pwned_api_check('123')
