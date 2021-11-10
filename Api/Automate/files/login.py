
from base import *

url = 'https://reqres.in/api/login'
class LoginPage():
    # def __init__(self,driver):
    #     self.driver=driver

    def loginValidation(self):
       
        login_email={
            "email": "eve.holt@reqres.in",  
            "password": "pistol"
        }
        invalid_email_post = requests.post(url, data = login_email)
        print(invalid_email_post)
        parse_invalid_email_post=json.loads(invalid_email_post.text)
        print(parse_invalid_email_post)


    #Empty Mail
    def EmptyMail(self):
        empty_email={
            "email": "",  
            "password": "pistol"
        }
        invalid_email_post = requests.post(url, data = empty_email)
        print(invalid_email_post)
        parse_invalid_email_post=json.loads(invalid_email_post.text)
        print(parse_invalid_email_post)
    
    #Empty Password
    def EmptyPassword(self):
        empty_password={
            "email": "eve.holt@reqres.in",  
            "password": ""
        }
        invalid_email_post = requests.post(url, data = empty_password)
        print(invalid_email_post)
        parse_invalid_email_post=json.loads(invalid_email_post.text)
        print(parse_invalid_email_post)

    #invalid email
    def InvalidMail(self):
        #invalid email
        error_email={
            "email": "eve.hoes.in",  
            "password": "pistol"
        }
        invalid_email_post = requests.post(url, data = error_email)
        print(invalid_email_post)
        parse_invalid_email_post=json.loads(invalid_email_post.text)
        print(parse_invalid_email_post)
    
    #invalid password
    def InvalidPassword(self):
        #invalid email
        error_password={
            "email": "eve.hoes.in",  
            "password": "45"
        }
        invalid_email_post = requests.post(url, data = error_password)
        print(invalid_email_post)
        parse_invalid_email_post=json.loads(invalid_email_post.text)
        print(parse_invalid_email_post)
    
  

