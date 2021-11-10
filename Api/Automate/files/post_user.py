from base import *

url = 'https://reqres.in/api/users'

class PostUser():

    def UserPost(self):
       
        post_data={
            "name": "morpheus",
            "job": "leader"
        }

        post_user = requests.post(url, data = post_data)
        print(post_user)
        parse_invalid_post_data=json.loads(post_user.text)
        print(parse_invalid_post_data)
    
