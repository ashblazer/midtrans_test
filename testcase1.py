from splinter import Browser

with Browser('chrome') as browser:
    # Visit URL
    url = "https://google.com/"
    browser.visit(url)
    browser.fill('q', 'midtrans')
    # Find and click the 'search' button
    button = browser.find_by_name('btnK').click()
    
    if browser.is_text_present('midtrans'):
        print("Yes, website was found!")
    else:
        print("No, it wasn't found")