from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto_name = "TCP" if packet.haslayer(TCP) else "UDP" if packet.haslayer(UDP) else "ICMP" if packet.haslayer(ICMP) else "Other"
        print(f"[+] Packet: {ip_src} -> {ip_dst} | Protocol: {proto_name}")

print("[*] Starting network sniffer... Press Ctrl+C to stop.")
sniff(filter="ip", prn=packet_callback, store=0)
