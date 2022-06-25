import requests


def test():
    user_id = "250"
    user_name='roni'
    return user_name,user_id

x=test()
user_id=x[1]
user_name=x[0]
url='http://127.0.0.1:5500/user/'

res = requests.post(url+user_id, json={"user_name":""+ user_name + "" })
if res.ok:
    print(res.json())


xx=url+user_id
res = requests.get(xx)
if res.ok:
    print(res.json())
else:
    print('Error')



# #
# res = requests.put('http://127.0.0.1:5000/user/' + user_id + '')
# if res.ok:
#     print(res.json())
#
# res = requests.delete('http://127.0.0.1:5000/user/' + user_id + '')
# if res.ok:
#     print(res.json())
