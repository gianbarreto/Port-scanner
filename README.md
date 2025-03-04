# Port Scanner

## Objective  
The **Port Scanner** project was developed to identify open ports on a target system by scanning a range of ports and detecting active services. This tool helps security professionals and network administrators assess potential vulnerabilities in their network infrastructure. The scanner provides detailed information about each port, including its status (open or closed), the service running on it, and even detects the operating system of the target machine.

## Features
- **Port Scanning**: Scan a range of ports on a given IP address to determine if they are open or closed.
- **Service Detection**: Identify the service running on each open port by retrieving the service banner (if available).
- **Operating System Detection**: Detect the target machine's operating system by analyzing port 80's status.
- **Multi-threaded Scanning**: Perform port scanning faster by using multi-threading for simultaneous port checks.
- **Graphical User Interface**: A simple GUI with Tkinter that allows users to easily input the IP address and port range, view results in real-time, and detect services and operating systems.

## Skills Learned  
- Understanding of **network ports** and their role in communication.  
- Working with **Python's socket library** for network scanning.  
- Identifying **open, closed, and filtered ports**.  
- Implementing **multi-threading** for faster scanning.  
- Detecting **services and banners** for better network insight.
- **Operating system detection** based on open ports.
- Developing a **Graphical User Interface (GUI)** with **Tkinter**.
- Enhancing **cybersecurity awareness** by recognizing exposed services and open ports.

## Tools Used  
- **Python** – Core language.  
- **Socket Library** – Used for establishing network connections and performing port scans.  
- **Tkinter** – Used for building the graphical user interface.

## How to Use  

1. When the GUI opens, you'll see fields for entering the IP address, Start Port, and End Port.

For example, use the following values:

IP Address: 8.8.8.8 (Google DNS IP)
Start Port: 80 (HTTP port)
End Port: 90 (to scan a range of ports)

2. After filling in the fields, click the "Start Scan" button. The program will begin scanning the ports in the specified range (in this case, from port 80 to 90).
