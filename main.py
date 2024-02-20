import time
from datetime import datetime as dt

hosts_path = "/etc/hosts"
hosts_test = "hosts"
redirect_ip = "127.0.0.1"
blocking_website_list = ["www.facebook.com", "facebook. com", "instagram.com","www.instagram.com"]
while True:
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month,dt.now().day, 18):
            print("Working hours...")
            with open(hosts_test,"r+") as file:
                content = file.read()
                print(content)
                for website in blocking_website_list: 
                     if website in content:
                        pass 
                     else:
                        file.write(redirect_ip+" "+ website+"\n")
        else:
            print("Fun hours...")
        time.sleep(5)
