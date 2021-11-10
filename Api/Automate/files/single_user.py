from base import *
class SingleUser():
    def UserSingle(self):
        url='https://reqres.in/api/users/2'
        response=requests.get(url)
        print(response)
        json_parse_data=json.loads(response.text)
        pages=jsonpath.jsonpath(json_parse_data,'data')
        print(pages)