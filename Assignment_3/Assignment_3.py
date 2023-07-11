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

# Finding the search bar and entering text
search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("apple watch")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "apple watch" in driver.title

# Selecting apple watch from the search results
watch_link = driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/div/div/div[1]/span/a/div/img")
watch_link.click()


# Waiting for the apple watch details page to load
time.sleep(5)

# Clicking on buy now button
buy_now_button = driver.find_element("id","buy-now-button")
buy_now_button.click()

# Waiting for the page to load
time.sleep(5)

# Clicking on change address button
shipping_address_change = driver.find_element("id", "addressChangeLinkId")
shipping_address_change.click()
time.sleep(2)


# Closing the webdriver
driver.close()
