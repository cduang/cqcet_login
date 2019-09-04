#encoding=utf8
import socket
import requests

def isNetOK(testserver):
    s=socket.socket()
    s.settimeout(3)
    try:
        status = s.connect_ex(testserver)
        if status == 0:
            s.close()
            return True
        else:
            return False
    except Exception as e:
        return False

def isNetChainOK(testserver=('www.baidu.com',443)):
    isOK = isNetOK(testserver)
    return isOK

def login():
	hostname=socket.gethostname()  #获取计算机名
	ip=socket.gethostbyname(hostname) #获取IP地址
	#file_ini
	filename = "user.ini"
	file = open(filename,'r+')
	login_user = file.readline().split("\n")[0]
	login_pass = file.readline().split("\n")[0]
	file.close()
	acname = "ME60A"
	acip = "172.31.254.25"
	i = 0
	while i < 2 :
		url = "http://172.16.255.11:801/eportal/"
		get = {
		"c"				:"Portal",
		"a"				:"login",
		"callback"      : "dr1567473661721",
		"login_method"  : "1",
		"user_account"  : login_user,
		"user_password" : login_pass,
		"wlan_user_ip"  : ip,
		"wlan_user_mac" : "000000000000",
		"wlan_ac_ip"    : acip,
		"wlan_ac_name"  : acname,
		"jsVersion"     : "3.1",
		"_" : "1567473656196"
		}
		url_get = requests.get(url=url,params=get)	
		if isNetChainOK() == False:
			acname = "ME60B"
			acip = "172.31.254.35"
		else:
			break
		i=i+1

if __name__ == '__main__':
	print("第一次需要设置登录用户名和密码，打开或者新建一个user.ini的文件")
	print("然后第一行输入用户名，第二行输入密码")
	print("输入完成之后按下任意键继续")
	p = input(">>> 按下 Enter 继续")
	login()
