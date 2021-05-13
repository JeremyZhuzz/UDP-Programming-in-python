# We will need the following module to generate randomized lost packets
import random
from socket import *
import sys
# Create a UDP socket 

UDPServerSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
host = sys.argv[1]
port = int(sys.argv[2])

UDPServerSocket.bind((host, port))

print("UDP server up and now is listening")

count =0;
while True:
	
	# Receive the client packet along with the address it is coming from 
	data, address= UDPServerSocket.recvfrom(1024);
	data = data.upper();


	# Generate random number in the range of 1 to 10 and if rand is less is than 4, we consider the packet lost and tell the client to retransmit
	rand = random.randint(1, 10)    
	if rand < 4:
		
		
		
		print("packet "+str(count)+" lost,need to be retransmitted\n")
		print(" ")
		UDPServerSocket.sendto("lost",address)
		
		continue;
		
	
	
	# Capitalize the message from the client and send the capilized version to the client
	else:
		count=count+1
		
		UDPServerSocket.sendto("received "+data,address)
		print("packet "+str(count)+" received\n")
		


UDPServerSocket.close()
	
	


	
	
	
