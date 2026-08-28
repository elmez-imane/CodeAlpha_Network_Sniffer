# CodeAlpha - Task 1: Basic Network Sniffer

A Python-based network packet sniffer developed during the CodeAlpha Cybersecurity Internship. The tool captures and analyzes live IP traffic using the `Scapy` library in Kali Linux.

## Features
- Real-time IPv4 packet interception.
- Protocol identification for **ICMP**, **TCP**, and **UDP**.
- Extraction of Source and Destination IP addresses.

## Prerequisites
- **OS**: Kali Linux
- **Python**: 3.x
- **Dependency**: Scapy (`pip install scapy`)

## Usage
Run the script with superuser privileges to enable socket capturing:

```bash
sudo python3 sniffer.py

## Screenshots:
Sniffer Code:
<img width="667" height="387" alt="sniffer_1" src="https://github.com/user-attachments/assets/8924f936-1014-428a-bed1-3e7ec1e19bc9" />

Testing :
<img width="602" height="441" alt="sniffer_2" src="https://github.com/user-attachments/assets/0a34dab8-6f2c-41d4-90f5-28188f8ef2ef" />

The packet:
<img width="700" height="247" alt="sniffer_3" src="https://github.com/user-attachments/assets/4ae536ec-3b96-4c52-a69f-4ffcb116a4ba" />



 
```bash
sudo python3 sniffer.p
