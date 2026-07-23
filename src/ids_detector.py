import csv
import time
import os

# ==============================================================================
# HỆ THỐNG PHÁT HIỆN XÂM NHẬP (IDS SIMULATOR) - BLUE TEAM
# Mục đích: Phân tích Log lây nhiễm để phát hiện hành vi Botnet và cảnh báo.
# ==============================================================================

LOG_FILE = 'results/output.csv'

class BotnetDetector:
    def __init__(self):
        self.threat_count = 0

    def analyze_logs(self):
        print("\n" + "="*60)
        print(" KHỞI ĐỘNG HỆ THỐNG IDS (BLUE TEAM) - KIỂM TRA BẢO MẬT ".center(60))
        print("="*60)
        time.sleep(1)
        
        if not os.path.exists(LOG_FILE):
            print(f"[-] Hệ thống an toàn. Chưa phát hiện file log lây nhiễm ({LOG_FILE}).")
            print("    Hãy chạy script 'code_demo.py' trước để mô phỏng Tấn công.")
            return

        print("[*] Đang phân tích hành vi mạng từ file log tập trung...")
        time.sleep(1.5)

        with open(LOG_FILE, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                ip = row.get('IP_Address', 'Unknown')
                status = row.get('Bot_Status', '')
                password = row.get('Default_Password', '')
                device_type = row.get('Device_Type', 'IoT Device')

                # Luật phát hiện 1: Bị đổi trạng thái thành Zombie
                if status == 'Active_Zombie':
                    print(f"\n[CẢNH BÁO ĐỎ] Thiết bị {device_type} tại {ip} đang có hành vi kết nối đến C&C Server!")
                    self.threat_count += 1
                
                # Luật phát hiện 2: Lộ mật khẩu mặc định nguy hiểm (Dấu hiệu của mã độc Mirai)
                if password in ['xc3511', '12345', 'admin', 'guest']:
                    print(f"   -> [Lỗ hổng nghiêm trọng] Phát hiện sử dụng mật khẩu yếu '{password}'.")
                    print(f"   -> Đề nghị đổi mật khẩu và cô lập thiết bị {ip} ngay lập tức!")
                    time.sleep(0.5)

        print("\n" + "-" * 60)
        if self.threat_count > 0:
            print(f"[!!!] BÁO ĐỘNG: PHÁT HIỆN TỔNG CỘNG {self.threat_count} THIẾT BỊ ĐÃ TRỞ THÀNH BOTNET.")
            print("[*] Đề xuất hành động ứng phó khẩn cấp:")
            print("    1. Đẩy rule chặn Port 23 vào Router (Xem file configs/firewall_rules.acl).")
            print("    2. Cách ly vùng mạng VLAN 20 (Mạng IoT) ra khỏi mạng nội bộ.")
        else:
            print("[V] Mạng nội bộ hiện tại an toàn. Không phát hiện dấu hiệu Botnet.")

if __name__ == "__main__":
    ids = BotnetDetector()
    ids.analyze_logs()
