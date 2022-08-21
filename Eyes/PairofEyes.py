#!/usr/bin/env python3

"""
PairofEyes allows you to scout out available products
AS OF RN CAN ONLY RUN FROM THE CLI IN THE /project directory
"""

import selenium.common.exceptions as excep
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options  # For opening the browser headlessly
import time
import os
import sys
from docopt import docopt

service = Service(ChromeDriverManager().install())
wd = wd.Chrome(service=service)


class Eyes:
    '''
    Only meant to provide recon on products
    '''
    def __init__(self, in_stock_bool=False, site_of_interest=""):
        self.in_stock_bool = in_stock_bool
        self.site_of_interest = site_of_interest
        self.website_instructions = os.getcwd() + '/Website_Instructions'
        self.available_products = os.listdir(self.website_instructions)

    def single_product(self, item, animation=True):
        stores_in_stock = []  # Empty string, will be filled with the files where it is open
        documented_sites = self.website_instructions + '/{}'.format(str(item))
        for site in os.listdir(documented_sites):
            self.in_stock_bool = False  # Assumes the product is not in stock
            exec(open(os.path.join(documented_sites, site)).read())
            if self.in_stock_bool:  # If the product is in stock
                stores_in_stock.append(self.site_of_interest)  # The url will be added to the array
        return stores_in_stock

    def single_item(self, item_path):
        self.in_stock_bool = False
        exec(open(item_path).read())

    def scan_for_key_products(self):
        for product in self.available_products:
            self.single_product(product)

if __name__ == "__main__":
    instance = Eyes()
    instance.single_item('Website_Instructions/RaspberryPi3ModelB/adafruit_servo_hat.py')
    wd.close()
