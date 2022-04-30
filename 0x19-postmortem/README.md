# 0x19. Postmortem
In this project, I learned about postmortem report and practiced writing one:

## 1982_Web_01 Server’s Nginx installation failure to listen on port 80 incident report

### Issue Summary
From 9:32 AM to 10:02 AM GMT, Nginx installation on 1982_web_01 server rejected all packets directed at its port — 80/TCP. The server responded to all received HTTP requests with the error: (7) Failed to connect to 0 port 80: Connection refused. At its peak, the issue affected 60% of all traffic to this server as users could not view web pages. The root cause of the server’s rejection on this port was an undone configuration of the server’s firewall.

### Timeline (all times Greenwich Mean Time)
- 9:18 AM: Ngnix was installed on the server
- 9:32 AM: The server began to receive traffic
- 9:32 AM: Pagers alerted on-call Software Engineer, Chigozirim Igweamaka
- 9:40 AM: Cause of the server’s rejection on port 80 probed.
- 9:42 AM: Successful configuration to allow port 80 on the server
- 9:45 AM: Server restart begin
- 10:02 AM: 100% of traffic back online

### Root Cause
At 9:18 AM GMT Ngnix was installed on the server and was configured manually. The team forgot to give firewall permission to requests coming on port 80 to the server. Hence the firewall allowed requests from other specified ports except from port 80, which is essential to the provision of service by the server.

### Resolution
At 9:32 AM GMT, the monitoring systems alerted the engineer on-call, Chigozirim Igweamaka, who probed the issue and proceeded to solve it.
AT 9:42 AM GMT, Chigozirim configured the server’s firewall — giving permission to port 80/TCP.

### Corrective and Preventative Measures
To prevent and incident like this from happening in the future, the team should:
- use Server Control Management tools, Puppet for example, to configure servers
- run series of tests before a server is opened to traffic
  
Sincerely,  
Server Administering Team
