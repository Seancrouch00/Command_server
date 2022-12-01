import socket
import logging

 #logging 
logging.basicConfig(filename="cammandserver.log",format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

#server
s = socket.socket()
host = socket.gethostname()
port = 9001
s.bind((host, port))
print("Server running on", host, port)
logging.info("Server running on port localhost on port 9001")
try:
	s.listen(5)
	print("Listening for connection..")
	logging.info("Listening for connections")
except:
	print("Unable to listen for connection")
	logging.exception("Unable to listen for connection")
while True:
   c, addr = s.accept()
   print('Got connection from', addr)
   logging.info(addr, "Connected")
   try:
   	c.send('Thank you for connecting')
   	logging.info("[MSG SENT] - Thank you for connecting")
   except:
   	print("Message failed to send")
   	logging.exception("Message failed to send")
   c.close()
   logging.info("Connection ended")