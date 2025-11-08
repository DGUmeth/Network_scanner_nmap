#!/usr/bin/env python3
"""
Simple Network Scanner
Usage: python3 simple_scanner.py 192.168.1.0/24
"""

import subprocess
import sys

def scan_network(network_range):
    """Run nmap scan and save results"""
    
    print(f"Scanning {network_range}...")
    print("This may take a few minutes...\n")
    
    # Run nmap stealth scan
    cmd = ['nmap', '-sS', '-T4', network_range]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        output = result.stdout
        
        # Save to file
        with open('scan_results.txt', 'w') as f:
            f.write(output)
        
        print(output)
        print("\n✓ Results saved to scan_results.txt")
        
    except FileNotFoundError:
        print("Error: nmap is not installed")
        print("Install it with: sudo apt-get install nmap")
    except subprocess.TimeoutExpired:
        print("Error: Scan timed out")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    print("\n⚠️  Only scan networks you own or have permission to scan!\n")
    print(r"""
██████╗░░██████╗░  ██╗░░░██╗███╗░░░███╗███████╗████████╗██╗░░██╗
██╔══██╗██╔════╝░  ██║░░░██║████╗░████║██╔════╝╚══██╔══╝██║░░██║
██║░░██║██║░░██╗░  ██║░░░██║██╔████╔██║█████╗░░░░░██║░░░███████║
██║░░██║██║░░╚██╗  ██║░░░██║██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║
██████╔╝╚██████╔╝  ╚██████╔╝██║░╚═╝░██║███████╗░░░██║░░░██║░░██║
╚═════╝░░╚═════╝░  ░╚═════╝░╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝""")
    print("\Copyright of Umeth Mahanama,2025")
    
    network = input("Enter network range (e.g., 192.168.1.0/24): ")
    
    scan_network(network)
