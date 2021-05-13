from socket import *
import sys
import datetime
string = "hello"

host = sys.argv[1]
port = int(sys.argv[2])

UDPClientSocket = socket(AF_INET, SOCK_DGRAM)

for x in range(1,101):
	a = datetime.datetime.now()
	
	UDPClientSocket.sendto("ping "+str(x)+" ",(host, port));
	print("ping "+str(x)+" has sent, time is "+str(a))
	
	string,address= UDPClientSocket.recvfrom(1024)
	
	while(string[0:4]=="lost"):
		
		
		print("PACKET "+str(x) +" IS LOST, and now is retransmiting")
		print("\n")
		UDPClientSocket.sendto("ping "+str(x),address);
		string,address= UDPClientSocket.recvfrom(1024)
		
		
	b = datetime.datetime.now()
	string = string.upper()
	print(string+"         the RTT time is "+str(b-a))
	print("\n")
	
UDPClientSocket.close();






