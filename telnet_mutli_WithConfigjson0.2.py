import telnetlib
import datetime,time
import os,sys,json

now = datetime.datetime.now()
path = os.path.dirname(os.path.abspath(__file__)) 


config_file = path + "//telnet.json"
with open(config_file) as json_file:
    config = json.load(json_file)
con = config['telnethosts']


def login():
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(pw.encode('ascii') + b"\n")
    tn.write(b"terminal length 0\n")
    time.sleep(1)
    tn.write(b"sh ru\n")
    time.sleep(1)
    tn.write(b"exit\n")
    result=tn.read_very_eager().decode('ascii')
    filename = path +  "//%s_%.2i-%.2i-%i_%.2i-%.2i-%.2i" % (host,now.month,now.day,now.year,now.hour,now.minute,now.second)
    ff = open(filename, 'a')
    ff.write(result)
    ff.close()

if __name__ == '__main__':
    for i in range(0,len(con)):
        host = config['telnethosts'][i]['HOSTIP']
        user = config['telnethosts'][i]['Username']
        pw = config['telnethosts'][i]['Password']
        tn = telnetlib.Telnet(host)
        login()
        print(host,user,pw)