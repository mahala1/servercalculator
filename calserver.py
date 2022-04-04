import socket		 	 # Import socket module

s = socket.socket() 	  		 # Create a socket object

host = 192.168.100.4                    # Get local machine name
port = 12000


s.bind((host, port)) 			 # Bind to the port
s.listen(5) 			         # Now wait for client connection.

print("Server is up and running")

while True:
     c, addr = s.accept() 		# Establish connection with client.
     print('Got connection from', addr)

     while True:
          try:
               equation=c.recv(1024).decode()
               if equation == "Q" or equation == "q" or equation == "Quit" or equation == "quit" or equation == "quit()":
                    c.send("Quit".encode())
                    break
               else:
                    print("You gave me the equation:", equation)
                    result = eval(equation)
                    c.send(str(result).encode())
          except (ZeroDivisionError):
               c.send("ZeroDiv".encode())
          except (ArithmeticError):
               c.send("MathError".encode())
          except (SyntaxError):
               c.send("SyntaxError".encode())
          except (NameError):
               c.send("NameError".encode())

     c.close() 	
