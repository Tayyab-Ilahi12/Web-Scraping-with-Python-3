import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/p/pl?Submit=ENE&N=100007709%2050001312%2050001314%2050001315%2050001402%2050001419%2050001471%2050001561%2050001944%2050012150%204814%20601201888%20601204369%20601301599%20601296379%20601296377%2050001669%20601321570%20601321572%20601323902%20601328427%20601331000%20601331379%20600419577%20600536666%20601341679&IsNodeId=1&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_1"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")
filename = "products.csv"
f = open(filename,"w")
headers = "Brand, Product_name, Price, shipping\n"
f.write(headers)

containers = page_soup.findAll("div",{"class":"item-container"})
for container in containers:
    
    brand = container.find("div","item-info").a.img["title"]
    title_container = container.findAll("a",{"class":"item-title"})
    shipping_container = container.findAll("li",{"class":"price-ship"})
    price_container = container.findAll("li",{"class":"price-current"})
    
    product_price = price_container[0].strong.text.strip()
    product_name = title_container[0].text.strip()
    shipping = shipping_container[0].text.strip()
    f.write(brand + "," + product_name.replace(",","|") + "," + "$" + product_price + "," + shipping + "\n")
    
f.close()
