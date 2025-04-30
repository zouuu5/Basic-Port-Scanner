import socket
import sys

def scan_ports(target_ip, start_port, end_port):
    print(f"\n[*] Scanning {target_ip} from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user.")
            sys.exit()
        except socket.gaierror:
            print("[!] Hostname could not be resolved.")
            sys.exit()
        except socket.error:
            print("[!] Couldn't connect to server.")
            sys.exit()

    if not open_ports:
        print("[-] No open ports found.")
    else:
        print(f"\n[✓] Scan completed. Open ports: {open_ports}")

def validate_input(ip, start, end):
    try:
        socket.inet_aton(ip)
        start = int(start)
        end = int(end)
        if start < 0 or end > 65535 or start > end:
            raise ValueError
        return ip, start, end
    except:
        print("\n[!] Invalid IP or port range. Example: 192.168.1.1 20 100")
        sys.exit()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python port_scanner.py <IP> <start_port> <end_port>")
        print("Example: python port_scanner.py 127.0.0.1 20 100")
        sys.exit()

    ip, start_port, end_port = validate_input(sys.argv[1], sys.argv[2], sys.argv[3])
    scan_ports(ip, start_port, end_port)
