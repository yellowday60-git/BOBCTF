import requests
import monitor
import flag_manager
import prob1
import prob2

flag = ""
# web hacking - get
cookies = {
    'session': 'eyJ1aWQiOiIwZjNjMWVjMy1iYjQyLTQ1MDgtODc3Zi04YWE2MjU4NzEzOGUiLCJ1c2VyIjoiYWRtaW4ifQ.Y8ConQ.pD2jmvZcy-GAyUBtAgNKVgfQf20',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

def get_ex(_url, _payload):
    response = requests.get(_url+_payload, cookies=cookies, headers=headers)
    return response

def post_ex(_url, _param):
    response = requests.post(_url, cookies=cookies, headers=headers, data=_param , verify=False)
    return response

def auto_ex(_location, payload, serivce, _method):
    
    
    if serivce == 0:
        
        return
    if serivce == 1:
        prob1.attack()
        return
    if serivce == 2:
        prob2.attack()
        return
    if serivce == 3:
        
        return
    if serivce == 4:
        return
    if serivce == 5:
        return
    if serivce == 6:
        return
    
    if serivce == 7:
        return
    
    
    
    if _method.upper() == "GET":
        for ip in monitor.ip_list:
            #url = "https://" + ip + _location
            url = _location
            res = get_ex(url, payload)
            # print(res.text)
            if monitor.flag_format in res.text:
                flag_pos = res.text.find(monitor.flag_format)
                flag = res.text[flag_pos : flag_pos+monitor.flag_len]
                print(f"{ip}'s flag is {flag}")
                flag_manager.flag_manager(serivce, flag_manager.get_round(), ip, flag)
                
    elif _method.upper() == "POST":
        for ip in ip_list:
            #url = "https://" + ip + _location
            url = _location
            res = post_ex(url, payload)
            #print(res.text)
            if monitor.flag_format in res.text:
                flag_pos = res.text.find(monitor.flag_format)
                flag = res.text[flag_pos : flag_pos+monitor.flag_len]
                print(f"{ip}'s flag is {flag}")
                flag_manager.flag_manager(serivce, flag_manager.get_round(), ip, flag)            

def main():
    auto_ex("https://webhacking.kr/rank.php", "", 3, "POST")

if __name__ == "__main__":
    main()
