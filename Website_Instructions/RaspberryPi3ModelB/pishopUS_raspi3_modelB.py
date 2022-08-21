self.site_of_interest = "https://www.pishop.us/product/raspberry-pi-3-model-b-armv8-with-1g-ram/"

wd.get(self.site_of_interest)

wd.implicitly_wait(10)

try:
    wd.find_element(By.XPATH, '//*[@id="backInStock-container"]')
    print("Sold Out :(")
except excep.NoSuchElementException:
    print("In Stock")
    self.in_stock_bool = True

