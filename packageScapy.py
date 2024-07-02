from scapy.all import sniff, IP

def packet_callback(packet):
    # 检查数据包是否是 IP 数据包，并且目标 IP 地址是指定的 IP
    if IP in packet and packet[IP].dst == target_ip:
        print(f"Captured packet: {packet.summary()}")
        # 打印完整的数据包内容
        packet.show()

if __name__ == "__main__":
    target_ip = "192.168.1.1"  # 替换为你要捕捉数据包的目标 IP 地址
    print(f"Starting packet capture for IP: {target_ip}")
    # 开始捕捉数据包
    sniff(prn=packet_callback, filter=f"ip dst {target_ip}", store=0)
