import allure
import pytest 
import selenium
import unittest
from unittest import result
from login import LoginPage
from list_user import listUser
from single_user import SingleUser
from sign_up import SignUpPage
from post_user import PostUser
from update_user import UpdateUser
from delay import Delay
@allure.severity(allure.severity_level.NORMAL)

class Test(unittest.TestCase):

    def test_loginValidation(self):
        self.login=LoginPage()
        self.login.loginValidation()
    
    #empty mail
    def test_EmptyMail(self):
        self.empty=LoginPage()
        self.empty.EmptyMail()
    
    #empty password
    def test_EmptyPassword(self):
        self.empty=LoginPage()
        self.empty.EmptyPassword()

    #Invalid Mail
    def test_InvalidMail(self):
        self.empty=LoginPage()
        self.empty.InvalidMail()

   # invalid password

    def test_Invalid_Password(self):
        self.invalid_password=LoginPage()
        self.invalid_password.InvalidPassword()


    
    #list user

    def test_UserList(self):
        self.list=listUser()
        self.list.UserList()
    
    #single user

    def test_UserSingle(self):
        self.single=SingleUser()
        self.single.UserSingle()


############# signup  validation start 

    def test_SignUpValidation(self):
        self.signup=SignUpPage()
        self.signup.SignUpValidation()

    def test_SignUpInvalidMail(self):
        self.invalid_mail=SignUpPage()
        self.invalid_mail.SignUpInvalidMail()

    def test_SignUpInvalidPassword(self):
        self.invalid_password=SignUpPage()
        self.invalid_password.SignUpInvalidPassword()

    def test_SignUpEmptyPassword(self):
        self.empty_password=SignUpPage()
        self.empty_password.SignUpEmptyPassword()

    ##### post user data 
    def test_UserPost(self):
        self.data=PostUser()
        self.data.UserPost()
    
    def test_UserPost(self):
        self.data=UpdateUser()
        self.data.UserUpdate()
    
    def test_DelayTime(self):
        self.delay=Delay()
        self.delay.DelayTime()