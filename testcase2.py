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
     time.sleep(3)

     with browser.get_iframe('snap-midtrans') as iframe:
     	third = iframe.find_by_xpath("//a[@href='#/select-payment']")
     	third.first.click()
     	time.sleep(3)
     	fourth = iframe.find_link_by_href("#/credit-card").first.click()
     	time.sleep(3)
     	iframe.fill("cardnumber","4811111111111114")
     	iframe.find_by_xpath("//input[@placeholder='MM / YY']").fill("0123")
     	iframe.find_by_xpath("//input[@placeholder='123']").fill("123")
     	fifth = iframe.find_by_xpath("//a[@href='#/']").click()
     	time.sleep(3)

     	with browser.get_iframe(2) as iframe2:
     		iframe2.fill("PaRes","112233")
     		iframe2.find_by_name("ok").first.click()
     		time.sleep(5)
     		if iframe2.is_text_present('Transaction Successful'):
     	        	print("Yes , Transaction SUCCESS")