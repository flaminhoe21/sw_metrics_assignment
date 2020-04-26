# -*- coding: utf-8 -*-
import unittest, re
from selenium import webdriver
import json
import time
from json import loads

class assertTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('E:\Flaminhoe\VUM\SE Metrics\MetricsB\chromedriver.exe')
        self.base_url="https://en.wikipedia.org/wiki/Software_metric"
        self.accept_next_alert = True

    def test_metrics(self):
        driver = self.driver
        total = {}

        for result in range(10):
            driver.get(self.base_url)
            result = driver.execute_script('return window.performance.getEntries()')

            for test in result:
                url = test['name']
                total.setdefault(url,[]).append(test['duration']) 

                for key, value in total.items():
                    numbers_val = len(total)
                    print(numbers_val)
                    sumValue = sum([item for item in value if item])
                    duration_average = sumValue/numbers_val

                with open('averageTest1.csv','a') as csv_file:
                    csv_file.write(f'name: {url}, duration: {duration_average}\n')

            print(total.values())
            
        with open('output3.txt', 'w') as json_file:
            json_file.write(f'{result}')

        with open("output3.txt") as text_file:
            myfile = text_file.read()
            myfile = myfile.replace('\'', '"')

        with open('jsonoutput.json', 'w') as pretty_json:
            result = driver.execute_script('return window.performance.getEntries()')
            for res in result:
                pretty_json .write(json.dumps(res, indent=2))
                #base_url = res["name"]

    def tearDown(self):
        self.driver.quit()
        pass

if __name__ == "__main__":
    unittest.main()

