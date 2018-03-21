import time
from splinter import Browser

with Browser('chrome') as browser:
     # Visit url
     url = "https://demo.midtrans.com/"
     browser.visit(url)

     first_button = browser.find_by_text("BUY NOW").click()
     browser.is_element_present_by_text("CHECKOUT", wait_time = 10)
     second = browser.find_by_text("CHECKOUT").value
     second_button = browser.find_by_text("CHECKOUT").click()
     print(second)
     
     browser.is_element_present_by_xpath("//a[@href='#/select-payment']",wait_time = 5)
     #third_button = 
     assert browser.find_by_xpath("//a[@href='#/select-payment']").visible
     print(third_button)