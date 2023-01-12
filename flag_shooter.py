import requests
import os
import flag_manager
import monitor

def auth(url, flag, session):
    cookies = {
        'session': session,
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'session=eyJ0ZWFtX2lkeCI6MX0.Y7_-KQ.-HgRrXK0SVI-UwIjSBWIi5yqPG8',
        'Origin': url,
        'Referer': url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = 'flag='+flag

    response = requests.post(url + '/api/auth', cookies=cookies, headers=headers, data=data, verify=False)
    
    return response

def shoot_all(ip_list):
    for ip in ip_list:
        round = flag_manager.get_round()
        for service in range(monitor.service_count):
            flag = flag_manager.get_flag(service, round, ip)
            if flag_manager.check_flag_vaild(flag):
                url = monitor.flag_url
                if len(url) >= 1:
                    res = auth(url, flag, monitor.flag_session)
                
                    if ":(" in res:
                        print(f"{ip}: incorrect!!!!")
                        flag_manager.remove_flag(service, round, ip)
                    else:
                        monitor.pop_unauth(ip_list, ip)

def main():
    #print(flag_manager.get_flag(12, "10.0.0.4"))
    shoot_all(monitor.ip_list)
    
if __name__ == "__main__":
    main()