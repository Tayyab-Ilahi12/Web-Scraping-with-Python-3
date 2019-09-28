import csv
from selenium import webdriver
max_page = 5
max_digit = 3

with open('results.csv','w') as f:
    f.write("Buyers, Price \n")
    
driver = webdriver.Chrome()

for i in range(1,max_page + 1):
    page_num = (max_digit - len(str(i))) * "0" + str(i)
    url = "http://econpy.pythonanywhere.com/ex/" + page_num + ".html"
    driver.get(url)
    
    buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
    prices = driver.find_elements_by_xpath('//span[@class="item-price"]')
    
    page_items = len(buyers)
    with open('results.csv','a') as f:
        for i in range(page_items):
            f.write(buyers[i].text + "," + prices[i].text + "\n")
            
driver.close()            
            
            