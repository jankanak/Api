
import unittest


class BaseTest(unittest.TestCase): 
    @classmethod
    def setUpClass(cls):
        cls.driver=driver
       

    def tearDown(self):
        self.driver.close()

