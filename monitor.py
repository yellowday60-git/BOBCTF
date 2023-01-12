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

def init():
    fm.make_tempelet(ip_list)

def pop_unauth(list, ip):
    list.remove(ip)

def monitoring():
    unauth = []
    unauth = ip_list
    while(True):
        try:
            round = fm.get_round()
            os.system('clear')
            print(f"\033[91mround : {round}".center(20))
            
            if fm.is_roundfile(round) == False:
                fm.make_roundfile(round)
                unauth = ip_list
                
            for ip in ip_list:
                flag = fm.get_flag(fm.get_round(), ip)
                
                if fm.check_flag_vaild(flag):
                    print(f"\033[94m{ip}:{flag}")
                else:
                    print(f"\033[95m{ip}:NONE!!")
            
            # print(unauth)
            
            fs.shoot_all(unauth)
            time.sleep(5)
        except KeyboardInterrupt:
            exit()
        except:
            continue

def main():
    init()
    monitoring()

if __name__ == "__main__":
    main()