self.site_of_interest = "https://www.adafruit.com/product/3055"

wd.get(self.site_of_interest)

wd.implicitly_wait(10)

try:
    wd.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div[1]/div/div[1]/div/div')
    print("Sold Out :(")
except excep.NoSuchElementException:
    print("In Stock")
    self.in_stock_bool = True

