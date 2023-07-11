# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca/")
time.sleep(3)
g
# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("apple watch")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "apple watch" in driver.title

# Selecting a laptop from the search results
# laptop_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/span/a/div/img")
watch_link = driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/div/div/div[1]/span/a/div/img")
# laptop_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
watch_link.click()


# Waiting for the laptop details page to load
time.sleep(5)

# Adding the laptop to the cart
buy_now_button = driver.find_element("id","buy-now-button")
buy_now_button.click()

# Waiting for the cart to update
time.sleep(5)

# Clicking on no thanks button
#no_thanks_button= driver.find_element("xpath","/html/body/div[9]/div[3]/div[1]/div/div/div[2]/div[2]/div/div/div[3]/div/span[2]/span/input")
#no_thanks_button.click()
#time.sleep(2)
shipping_address_change = driver.find_element("id", "addressChangeLinkId")
shipping_address_change.click()
time.sleep(2)

# proceed_to_checkout= driver.find_element("xpath","/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div/form/span/span/span/input")
# proceed_to_checkout.click()
# time.sleep(2)

# Verifying that the laptop has been added to the cart
# cart_count = driver.find_element("id","nav-cart-count")
# assert cart_count.text == "1"
# cart_count.click()

# Closing the webdriver
driver.close()
