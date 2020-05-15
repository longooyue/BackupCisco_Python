import telnetlib
import datetime,time
import os
import sys

now = datetime.datetime.now()
path = os.path.dirname(os.path.abspath(__file__)) 
user = "cisco"
password = "cisco"
cmd = ["terminal length 0", "sh ru"]
hosts = ['172.21.37.249', '172.21.1.254']


def login():
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    tn.write(b"terminal length 0\n")
    tn.write(b"sh ru\n")
    tn.write(b"exit\n")
    result=tn.read_all().decode('ascii')
    filename = path +  "//%s_%.2i-%.2i-%i_%.2i-%.2i-%.2i" % (host,now.month,now.day,now.year,now.hour,now.minute,now.second)
    ff = open(filename, 'a')
    ff.write(result)
    ff.close()


if __name__ == '__main__':
    # host = sys.argv[1]
    # cmd = sys.argv[2]
    #host_file = path + "//cisco_hosts.txt"
    #for hosts in open(host_file):
    for host in hosts:
        print(host)
        tn = telnetlib.Telnet(host)
        login()