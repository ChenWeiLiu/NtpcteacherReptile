import requests
import os
import re
import urllib3

class Ntpcteacher():
    def __init__(self):
        self.Target_URL = 'http://ntpcteacher.eduweb.tw/Module/Act/Upload/'

    def Start(self):
        for num in range(1500000000,1600000000):
            Target_JPG_URL = self.Target_URL+ str(num) +'.jpg'
            # print ( Target_JPG_URL )
            rs = requests.get(Target_JPG_URL)
            if rs.status_code == 200:
                print (rs.status_code)
                with open('./Download/'+str(num)+'.jpg', 'wb') as f:
                    for chunk in rs:
                        f.write(chunk)

if __name__ == "__main__":
    obj = Ntpcteacher()