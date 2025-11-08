# Network_scanner_nmap

A straightforward Python script that scans a network range using Nmap and saves the results.

## ⚠️ Legal Warning

**Only scan networks you own or have explicit permission to scan.**  
Unauthorized scanning is illegal.

## Requirements

- Python 3
- Nmap installed on your system

### Install Nmap

```bash
# Ubuntu/Debian
sudo apt-get install nmap

# MacOS
brew install nmap

# Fedora
sudo dnf install nmap
```

## How to Use

1. Run the script:
```bash
sudo python3 simple_scanner.py
```

2. Enter the network range when prompted:
```
Enter network range (e.g., 192.168.1.0/24): 192.168.1.0/24
```

3. Wait for the scan to complete

4. Results are displayed on screen and saved to `scan_results.txt`

## Example Output

```
Scanning 192.168.1.0/24...
This may take a few minutes...

Starting Nmap scan...
Nmap scan report for 192.168.1.1
Host is up (0.0010s latency).
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
443/tcp  open  https

Nmap scan report for 192.168.1.10
Host is up (0.0012s latency).
PORT     STATE SERVICE
3306/tcp open  mysql

✓ Results saved to scan_results.txt
```

## Notes

- The script uses a stealth SYN scan (`-sS`) which requires root privileges (sudo)
- Scan timeout is set to 5 minutes
- Results show active hosts and their open ports

## Troubleshooting

**"nmap is not installed"**  
→ Install nmap using the commands above

**"Permission denied"**  
→ Run with sudo: `sudo python3 simple_scanner.py`

**Scan takes too long**  
→ Try a smaller network range (e.g., `/28` instead of `/24`)
