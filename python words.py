# friend= open('thebeginning.py')
# counts= dict()
# for line in friend:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 2

# lst = list()
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup) 

# lst = sorted(lst,reverse=True)
# for val, key in lst[:10] :
#     print(key, val)

# import re
# x = 'my 2 favorite numbers are 19 and 42'
# y =re.findall('[0-9]+',x)
# print(y)

# import socket

# mysock= socket (socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd= 'GET http://pr4e.org/romeo.txt Http/1.0/n/n'.emcode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()

# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://www.byui/account')
# for line in fhand:
#     print(line.decode().strip())


