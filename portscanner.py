import socket
import threading
from tkinter import *
from tkinter import messagebox

# Function to detect the operating system
def detect_os(ip):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        result = s.connect_ex((ip, 80))  # Attempt to connect to port 80 (http)
        s.close()
        if result == 0:
            return "Linux/Unix-based OS"  # Assuming if port 80 is open, it's a Unix-based OS
        else:
            return "Windows OS"
    except socket.error:
        return "Unable to detect OS"

# Function to detect services (banners)
def detect_service(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        s.close()
        if banner:
            return banner
        else:
            return "Service detected but no banner available"
    except socket.error:
        return None

# Function to scan a range of ports
def scan_ports(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        print(f"Scanning port {port}...")  # Indicate which port is being scanned
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)  # Set timeout to 5 seconds for better response handling
        result = s.connect_ex((ip, port))
        
        if result == 0:
            service = detect_service(ip, port)
            open_ports.append((port, service))
            print(f"Port {port} is open.")
            if service:
                print(f"Service: {service}")
            else:
                print(f"Service: Unknown service")
        else:
            print(f"Port {port} is closed.")
        s.close()
    
    return open_ports

# Function to handle the scanning in multithreaded mode
def thread_scan(ip, start_port, end_port, update_func):
    open_ports = scan_ports(ip, start_port, end_port)
    update_func(open_ports)

# Function to update the results in the GUI
def update_results(open_ports):
    for port, service in open_ports:
        result_listbox.insert(END, f"Port {port} is open. Service: {service}")

# Function to start scanning when the button is pressed
def start_scan():
    ip = ip_entry.get()
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())
    
    if not ip:
        messagebox.showerror("Input Error", "Please enter a valid IP address.")
        return
    
    # Clear previous results
    result_listbox.delete(0, END)
    
    # Start a new thread for scanning ports
    threading.Thread(target=thread_scan, args=(ip, start_port, end_port, update_results)).start()

# Graphical User Interface with tkinter
root = Tk()
root.title("Port Scanner")

# Create input fields for IP and ports
Label(root, text="Enter IP address:").pack(pady=5)
ip_entry = Entry(root, width=30)
ip_entry.pack(pady=5)

Label(root, text="Start Port:").pack(pady=5)
start_port_entry = Entry(root, width=30)
start_port_entry.pack(pady=5)

Label(root, text="End Port:").pack(pady=5)
end_port_entry = Entry(root, width=30)
end_port_entry.pack(pady=5)

# Create a button to start the scan
scan_button = Button(root, text="Start Scan", command=start_scan)
scan_button.pack(pady=10)

# Create a Listbox to display the results
result_listbox = Listbox(root, width=50, height=15)
result_listbox.pack(pady=10)

# Add OS detection at the beginning
ip = "8.8.8.8"  # Google DNS as an example
os_detected = detect_os(ip)
Label(root, text=f"Detected OS: {os_detected}").pack(pady=5)

root.mainloop()