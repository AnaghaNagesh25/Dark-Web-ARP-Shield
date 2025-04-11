
---

### 🛡️ Optional: `arp_defense.py` (Run on your system, not deployed)

If you want to detect threats for real (not just dashboard), create this file **locally** on your system:

```python
import scapy.all as scapy
import time

def load_threats():
    try:
        with open("dark_web_threat_list.txt", "r") as f:
            return set(line.strip() for line in f if line.strip())
    except:
        return set()

def log_alert(ip, mac):
    with open("alerts.log", "a") as log:
        log.write(f"[{time.ctime()}] 🚨 Detected ARP spoof - IP: {ip}, MAC: {mac}\n")

def sniff(pkt):
    if pkt.haslayer(scapy.ARP) and pkt[scapy.ARP].op == 2:
        ip = pkt[scapy.ARP].psrc
        mac = pkt[scapy.ARP].hwsrc
        if ip in load_threats():
            print(f"[ALERT] {ip} is in the threat list!")
            log_alert(ip, mac)

print("[*] Monitoring ARP packets...")
scapy.sniff(store=False, prn=sniff)
