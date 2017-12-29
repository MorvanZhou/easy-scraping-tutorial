import requests


def get():
    print('\nget')
    param = {"wd": "莫烦Python"}
    r = requests.get('http://www.baidu.com/s', params=param)
    print(r.url)
    print(r.text)


def post_name():
    print('\npost name')
    # http://pythonscraping.com/pages/files/form.html
    data = {'firstname': '莫烦', 'lastname': '周'}
    r = requests.post('http://pythonscraping.com/files/processing.php', data=data)
    print(r.text)


def post_image():
    print('\npost image')
    # http://pythonscraping.com/files/form2.html
    file = {'uploadFile': open('./image.png', 'rb')}
    r = requests.post('http://pythonscraping.com/files/processing2.php', files=file)
    print(r.text)


def post_login():
    print('\npost login')
    # http://pythonscraping.com/pages/cookies/login.html
    payload = {'username': 'Morvan', 'password': 'password'}
    r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
    print(r.cookies)
    # http://pythonscraping.com/pages/cookies/profile.php
    r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
    print(r.text)


def session_login():
    print('\nsession login')
    # http://pythonscraping.com/pages/cookies/login.html
    sess = requests.Session()
    payload = {'username': 'Morvan', 'password': 'password'}

    s = sess.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
    print(s.cookies.get_dict())
    s = sess.get("http://pythonscraping.com/pages/cookies/profile.php")
    print(s.text)


get()
post_name()
post_image()
post_login()
session_login()