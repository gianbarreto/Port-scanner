import socket

ip = input("Enter the IP address: ")

for port in range(0, 65536):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    result = s.connect_ex((ip, port))

    if result == 0:
        print(f"Port {port} is open.")
        s.close()
    else:
        print(f"Port {port} is closed.")

# This program will try to connect to every port on the given IP address. If the connection is successful, it will print that the port is open.
# The connect_ex() method is used to connect to the port. If the connection is successful, it returns 0, otherwise it returns an error code.