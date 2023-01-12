import time
import os
import math
import shutil

now = time

def get_hour():
    return now.localtime().tm_hour

def get_min():
    return now.localtime().tm_min

def get_sec():
    return now.localtime().tm_sec

def get_round():
    start_time = 1673568000 # 2023-01-13-09:00:00
    start_time = 1673542800 # 2023-01-13-02:00:00 for testing
    now_round =  math.floor((abs(start_time - now.time()) / 60 / 5)) + 1
    
    return now_round

def make_tempelet(ips):
    cur_path = os.getcwd()
    file_path = cur_path + "/flag_file/temp.txt"
    
    if os.path.isdir(cur_path + "/flag_file") == False:
        os.mkdir(cur_path + "/flag_file")
    
    if os.path.isfile(file_path) == False:
        f = open(file_path, 'w')
        f.close()
        
    f = open(file_path, 'w')
    for ip in ips:
        f.write(f"{ip}:\n")
    f.close()

def flag_manager(round, ip, flag):
    cur_path = os.getcwd()
    file_path = cur_path + "/flag_file/round" + str(round).rjust(3,"0") + ".txt"
    tempelet_path = cur_path + "/flag_file/temp.txt"
    
    if os.path.isdir(cur_path + "/flag_file") == False:
        os.mkdir(cur_path + "/flag_file")
    
    if os.path.isfile(file_path) == False:
        f = open(file_path, "w")
        f.close()
    
    f = open(tempelet_path, 'r')
    lines = f.readlines()
    f.close()
    msg = ""
    
    check = False
    past_ip = "0.0.0.0"
    for line in lines:
        ip_pos = line.find(":")
        now_ip = line[:ip_pos]
        #now_ip[now_ip.rfind(".") + 1]
        
        # print(past_ip[past_ip.rfind(".") + 1 : ])
        # print(now_ip[now_ip.rfind(".") + 1 : ])
        # print(ip[ip.rfind(".") + 1 : ])

        if int(ip[ip.rfind(".") + 1:]) == int(now_ip[now_ip.rfind(".") + 1:]):
            msg += f'{ip}:{flag}\n'
        else:
            msg += line

    
    print(msg)
    f = open(file_path, 'w')
    f.writelines(msg)
    f.close()

def get_flag(round, ip):
    cur_path = os.getcwd()
    file_path = cur_path + "/flag_file/round" + str(round).rjust(3,"0") + ".txt"
    if os.path.isfile(file_path) == False:
        print("There's no file !!")
        return -1
    
    f = open(file_path, "r")
    lines = f.readlines()
    for line in lines:
        ip_pos = line.find(":")
        now_ip = line[:ip_pos]
        if ip == now_ip:
            f.close()
            return line[ip_pos+1:]
    
    print("no info!!")
    f.close()
    return -1
    
def main():
    # print(get_round())
    #ips = ["10.0.0.1","10.0.0.2","10.0.0.3","10.0.0.4","10.0.0.5","10.0.0.6","10.0.0.7","10.0.0.8"]
    #make_tempelet(ips)
    # flag_manager(12, "10.0.0.4", "flag")
    print(get_flag(12, "10.0.0.5"))

if __name__ == "__main__":
    main()
    