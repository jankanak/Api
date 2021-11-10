from base import *
class listUser():
    def UserList(self):
        url='https://reqres.in/api/users?page=2'
        response=requests.get(url)
        print(response)
        json_parse_data=json.loads(response.text)
        pages=jsonpath.jsonpath(json_parse_data,'data')
        print(pages)