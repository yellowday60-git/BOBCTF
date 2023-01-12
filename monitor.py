import auto_ex
import flag_manager as fm
import flag_shooter as fs
import time
import os

ip_list = ["10.10.1.0","10.10.1.1","10.10.1.2","10.10.1.3","10.10.1.4","10.10.1.5",
           "10.10.1.6","10.10.1.7","10.10.1.8","10.10.1.9","10.10.1.10","10.10.1.11",
           "10.10.1.12","10.10.1.13","10.10.1.14","10.10.1.15","10.10.1.16"]

# flag 인증 사이트
flag_url = ""
flag_session = ""

flag_format = "flag{"
flag_len = 32
flag = ""

service_count = 6

attack_url = ""
payload = ""
method = "GET"

def init():
    fm.make_tempelet(ip_list)

def pop_unauth(list, ip):
    list.remove(ip)

def manual_set_flag(serivce, round, ip, flag):
    if fm.is_roundfile(service,round) == False:
        fm.make_roundfile(service, round)
    
    fm.flag_manager(service, round, ip, flag)

def monitoring():
    global service_count
    unauth = []
    for i in range(service_count):
        unauth.append(ip_list)
    
    while(True):
        try:
            for service in range(service_count):
                round = fm.get_round()
                os.system('clear')
                print(f"\033[91mround : {round} \t service : {service}".center(30))
                
                if fm.is_roundfile(service,round) == False:
                    for i in range(service_count):
                        fm.make_roundfile(i, round)
                        unauth.append(ip_list)
                    
                for ip in ip_list:
                    flag = fm.get_flag(service, round, ip)
                    
                    if fm.check_flag_vaild(flag):
                        print(f"\033[94m{ip}:{flag}")
                    else:
                        print(f"\033[95m{ip}:NONE!!")
                
                # print(unauth)
                
                for ip in ip_list:
                    auto_ex.auto_ex(attack_url, payload, service, method)
                    
                fs.shoot_all(service,unauth[service])
                time.sleep(1)
        except KeyboardInterrupt:
            exit()
        # except:
        #     continue

def main():
    init()
    monitoring()

if __name__ == "__main__":
    main()