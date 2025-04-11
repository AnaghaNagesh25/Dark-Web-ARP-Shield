# 🛡️ Dark Web ARP Shield

This project detects ARP spoofing attempts and checks if the attacker's IP is on a dark web threat list. The Streamlit dashboard shows all alerts and known blacklisted IPs.

## 🚀 How It Works

- Add a `dark_web_threat_list.txt` with suspicious IPs.
- Your local system runs `arp_defense.py` to monitor ARP traffic (run manually with `sudo`).
- Any matches will be logged to `alerts.log`.
- The Streamlit dashboard (`streamlit_app.py`) displays alerts in real time.

## 📦 Files

- `streamlit_app.py`: Streamlit dashboard to monitor alerts and threat list
- `alerts.log`: Auto-generated log from ARP detector
- `dark_web_threat_list.txt`: List of known attacker IPs
- `requirements.txt`: Streamlit dependency

## 📡 Deploy Now

1. Fork this repo or upload it to GitHub.
2. Visit [https://streamlit.io/cloud](https://streamlit.io/cloud).
3. Deploy your app by selecting `streamlit_app.py` as the main file.
4. Enjoy your real-time cyber threat dashboard! 🎯

## ⚠️ ARP Detection Script (Manual, Optional)

Run this manually on your local Linux system:

```bash
sudo python3 arp_defense.py
