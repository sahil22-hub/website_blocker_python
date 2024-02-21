import time
from datetime import datetime as dt

hosts_path = "/etc/hosts"
hosts_test = "hosts"
redirect_ip = "127.0.0.1"
blocking_website_list = ["www.facebook.com", "facebook. com", "instagram.com","www.instagram.com"]
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month,dt.now().day, 16):
        print("Working hours...")
        with open(hosts_path,"r+") as file:
            content = file.read()
            print(content)
            for website in blocking_website_list: 
                 if website in content:
                    pass 
                 else:
                    file.write(redirect_ip+" "+ website+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in blocking_website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
