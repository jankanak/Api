from base import *

url = 'https://reqres.in/api/users?delay=3'

class Delay():

    def DelayTime(self):

        post_user = requests.get(url)
        print(post_user)
        parse_invalid_post_data=json.loads(post_user.text)
        print(parse_invalid_post_data)
    
