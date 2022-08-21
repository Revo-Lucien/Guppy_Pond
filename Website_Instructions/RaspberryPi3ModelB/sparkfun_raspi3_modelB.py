self.site_of_interest = "https://www.sparkfun.com/products/14643"

wd.get(self.site_of_interest)

wd.implicitly_wait(10)

try:
    wd.find_element(By.XPATH, '//*[@id="airlock"]/div/div[2]/div[1]/div[3]/div[1]/div[4]/div/form/div[2]/p[1]/button')
    print("Sold Out :(")
except excep.NoSuchElementException:
    print("In Stock")
    self.in_stock_bool = True

