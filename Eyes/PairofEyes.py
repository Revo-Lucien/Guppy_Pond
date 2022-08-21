#!/usr/bin/env python3

"""PairofEyes allows you to scout out avaliable products

"""

import selenium.common.exceptions as excep
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options #For opening the browser headlessly
import time
import os
import sys
from docopt import docopt

service = Service(ChromeDriverManager().install())
wd = wd.Chrome(service=service)

wd.implicitly_wait(10)

class Eyes:
    '''Only meant to provide recon on products'''
    def __init__(self, inStockBool=False, siteOfInterest=""):
        self.inStockBool = inStockBool
        self.siteOfInterest = siteOfInterest

    def single_product(self, item, animation=True):
        storesInStock = [] #Empty string, will be filled with the files where it is open
        documented_sites = '../Website_Instructions/{}'.format(str(item)) #Looks at all the sites for a specific product
        for site in os.listdir(documented_sites):
            self.inStockBool = False #Assumes the product is not in stock
            exec(open(os.path.join(documented_sites, site)).read())
            if self.inStockBool: #If the product is in stock
                storesInStock.append(self.site_of_interest) #The url will be added to the array, declared in the site.py file so hopefully it works
            wd.close()
        return storesInStock

    def current_products(self):
        return os.listdir('/Users/roberson/Desktop/tech_stuff/Python/guppy_pond/project/Website_Instructions')

    def scan_for_key_products(self):
        products_of_interest = os.listdir('project/Website_Instructions')
        for product in products_of_interest:
            self.single_product(product)

instance = Eyes()
wd.close()
# print(instance.current_products())
# instance.scan_for_key_products("hello", "everybody", "here")
# ava = instance.single_product("TestProducts")
# print(ava)

# def testing():
#     print("ASDADFSHDFHDFSHGDFGADFSg")
#     arguments = docopt(__doc__)
#     print('\n\n\n')
#     # print(type(arguments))
#     print('\n\n\n')
#
#     if arguments["--hello"] is not None:
#         print("--hello isn't here")
#
# if __name__ == "__main__":
#     testing()
#







#To incorporate the looking eyes I need to use multiple threads
# print(inStockBool)
#
# from looking_animation import looking
# import threading
#
# t1 = threading.Thread(target=instance.single_product, args=("TestProducts",))
# t2 = threading.Thread(target=looking)
#
# t1.start()
# t2.start()