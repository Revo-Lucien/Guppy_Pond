#Raspi 4 model B/2GB
self.site_of_interest = "https://www.pishop.us/product/raspberry-pi-4-model-b-2gb/"

wd.get(self.site_of_interest)

wd.implicitly_wait(10)

try:
    wd.find_element(By.XPATH, '//*[@id="backInStock-container"]')
    print("Sold Out :(")
except excep.NoSuchElementException:
    print("In Stock")
    self.inStockBool = True
