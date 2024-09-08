# The api package is apparently built in somehow? I don't understand the
# package management in this. I have no idea if you can use conda, venv, etc.

def api_post_test(x):
    api.post(str(x))

def api_out_test(x):
    api.out(f"{x}")

def api_send(x, y):
    api.send(x, y)

def api_dict_out():
    api.out({'a': [1, 2, 'a'], 'b': 1.3, 'c': 100, 'd': 'e'})

