##Part 1

1)docker pull infracloudio/csvserver:latest
2)docker image ls
3)docker image history infracloudio/csvserver:latest
4)docker container run -t --name Infra infracloudio/csvserver
5)docker container ls
6)docker container ls -a
7)docker container inspect Infra
8)docker container run -dt --name Infra infracloudio/csvserver /bin/bash
9)docker container exec -it Infra bash
10)pwd
11)ls -a
12)vi gencsv.py
13)dnf install python3
14)alternatives --set python /usr/bin/python3
15)python --version
16)python gencsv.py
17)ls -a
18)cat inputdata
19)chmod 755 inputdata
19)docker container exec -it Infra /csvserver/csvserver
20)netstat -ntlp
21)docker container stop Infra
22)docker container rm Infra
23)docker container run -dt --name Infra --env CSVSERVER_BORDER="Orange" -p 9393:9300 8cb989ef80b5 /bin/bash
24)docker container exec -it Infra bash
24)vi gencsv.py
25)dnf install python3
26)alternatives --set python /usr/bin/python3
27)python gencsv.py
28)ls -a
29)cat inputdata
30)echo $CSVSERVER_BORDER
31)exit
32)docker container exec -it Infra /csvserver/csvserver
33)curl http://localhost:9393

