# Developed By Sachin_K
# 03/12/21

import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL='https://www.amazon.in/Apple-iPad-Pro-11-inch-27-96-Wi-Fi/dp/B0932R4QBR/ref=sr_1_3?keywords=ipad+pro&qid=1638545667&sr=8-3'

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()


    price = price[1:8]
    i_price = price.translate({ord(i): None for i in ','})
    i_price = float(i_price)

    if (i_price < 50000):
        send_mail()

        print(i_price)
        print(title.strip())

        if((i_price > 60000)):
            send_mail()



def send_mail():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('#Your Email Here', '#Your Password here')

        subject = 'Alert Amazon'
        body = 'The price is down!! , click on this link Now!! : https://www.amazon.in/Apple-iPad-Pro-11-inch-27-96-Wi-Fi/dp/B0932R4QBR/ref=sr_1_3?keywords=ipad+pro&qid=1638545667&sr=8-3'

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail('ssachinkumar1997@gmail.com',
                        'ssachink.915@gmail.com',
                        msg)

        print("Email sent successfully")
        server.quit()


    except:
        print("Somethings wrong ! ")



check_price()

# Incase you want to keep track of the price for an entire day, use the below given while loop

#while (True):
#   check_price()
#   time.sleep(60 * 60)


