import vk 

token = 'c26ebd52f29cf8450378ac51887e23625f868fe115d7ba35dc4dda3a60eedbf4f2469455f8f0ab1bfffbd'
v = '5.95'

session = vk.Session(access_token= token)
vk_api = vk.API(session, v=v)

friends = vk_api.friends.get(id=321522398)

print(friends)

id4 = [321522398, 181083164, 593280872, 216838251]
def getfriends(id):
  friends = vk_api.friends.get(id=id)["items"]
  return friends
print(getfriends(id4))