import allure
from selenium import webdriver


class Test_001:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

    def test_002(self):
        print('\n test_002')

    @allure.step('第一步')
    def test_001(self):
        self.test_002()
        allure.attach(self.driver.get_screenshot_as_png(), '截图', allure.attachment_type.PNG)
        print('\n test_001')


