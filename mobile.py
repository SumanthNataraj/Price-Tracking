import requests
from bs4 import BeautifulSoup


#URL = "https://www.snapdeal.com/product/indus-valley-disposable-face-mask/638539148385"

product_details=[
    {"url": "https://www.snapdeal.com/product/stay-healthy-silicone-heel-protector/682622706581", "name": "Foot Protector", "targetPrice": 100},
    {"url": "https://www.snapdeal.com/product/indus-valley-disposable-face-mask/638539148385", "name": "Disposable Face Mask", "targetPrice": 450},
    {"url": "https://www.snapdeal.com/product/portronics-toad-8-bluetooth-mouse/6917529706432941571", "name": "Portronics Toad 8 Bluetooth Mouse", "targetPrice": 550},
    {"url": "https://www.snapdeal.com/product/archer-tech-lab-recurve700-wireless/649222416982#bcrumbLabelId:151", "name": "Archer Tech Lab RECURVE700 Wireless Mouse", "targetPrice":800},
    {"url": "https://www.snapdeal.com/product/portronics-por1682-wireless-mouse/636532626421#bcrumbLabelId:151", "name": "Portronics - POR-1682 Wireless Mouse", "targetPrice":550}
]
def get_product_price(URL):
    headers={
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.106"}

    page= requests.get(URL, headers=headers)

    soup=BeautifulSoup(page.text, 'html.parser')

    price3 = soup.find("span", {"class": "payBlkBig"})
    return price3.string
    
result_file=open('result_file', 'w')

try:
    for product in product_details:
        price3=get_product_price(product['url'])
        print(f"Product Name: {product['name']},\t Target Price: {product['targetPrice']}, \tCurrent Price: {price3}")
    
        if int(price3) < product["targetPrice"]:
            print("Price is below target. Consider buying!")
            result_file.write("Product Name:" + str(product["name"])+",\t\tTarget Price:" + str(product["targetPrice"]) + ",\t\tCurrent Price:" +str(price3)+"\n"+"Price is below target. Consider buying!"+"\n"+"--------------------------\n")
            print("--------------------------------")
        
        else:
            print("Price is above target. Keep an eye out for the sale!")
            result_file.write("Product Name:" + str(product["name"])+",\t\tTarget Price:" + str(product["targetPrice"]) + ",\t\tCurrent Price:" +str(price3)+"\n"+"Price is above target. Keep an eye out for the sale!"+"\n"+"--------------------------\n")
            print("--------------------------------")
        
finally:
    result_file.close()

