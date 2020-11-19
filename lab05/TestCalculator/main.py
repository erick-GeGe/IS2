from selenium import webdriver
import unittest

class TestPercentageCalculator(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://www.calculator.net/')
        self.driver.find_element_by_xpath('//*[@id="contentout"]/table/tbody/tr/td[3]/div[1]/a/img').click()
        self.driver.find_element_by_xpath('//*[@id="content"]/table[2]/tbody/tr/td/div[3]/a').click()

    def test_normal(self):
        self.driver.find_element_by_name('cpar1').send_keys('10')
        self.driver.find_element_by_name('cpar2').send_keys('50')
        self.driver.find_element_by_xpath('//*[@id="content"]/table[1]/tbody/tr[2]/td/input[2]').click()
        result = self.driver.find_element_by_xpath('//*[@id="content"]/p[2]/font/b').text
        self.assertEqual(result, '5')

    def test_decimal(self):
        self.driver.find_element_by_name('cpar1').send_keys('10.10')
        self.driver.find_element_by_name('cpar2').send_keys('10')
        self.driver.find_element_by_xpath('//*[@id="content"]/table[1]/tbody/tr[2]/td/input[2]').click()
        result = self.driver.find_element_by_xpath('//*[@id="content"]/p[2]/font/b').text
        self.assertEqual(result, '1.01')

    def test_alfanumerico(self):
        self.driver.find_element_by_name('cpar1').send_keys('10')
        self.driver.find_element_by_name('cpar2').send_keys('A')
        self.driver.find_element_by_xpath('//*[@id="content"]/table[1]/tbody/tr[2]/td/input[2]').click()
        result = self.driver.find_element_by_xpath('//*[@id="content"]/p[2]/font').text
        self.assertEqual(result, 'Please provide two numeric values in any fields below.')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
