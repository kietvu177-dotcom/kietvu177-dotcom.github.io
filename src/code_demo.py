import csv
import json
import time
import datetime
import os

# ==============================================================================
# HỆ THỐNG MÔ PHỎNG BOTNET IOT (LOCAL SIMULATION) - RED TEAM
# Lưu ý: Script này chỉ giả lập quá trình lây nhiễm trên Localhost.
# ==============================================================================

DATASET_PATH = 'data/dataset_gia_lap.csv'
OUTPUT_CSV_PATH = 'results/output.csv'
BOT_CONFIG_PATH = 'configs/bot_config.json'
PAYLOAD_PATH = 'data/payload_mau.json'

class BotnetSimulator:
    def __init__(self):
        self.target_devices = []
        self.infected_bots = []
        self.bot_config = self.load_json(BOT_CONFIG_PATH)
        
    def load_json(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}

    def step_1_load_targets(self):
        print("\n[+] BƯỚC 1: TẢI DANH SÁCH THIẾT BỊ IOT MỤC TIÊU...")
        time.sleep(1)
        
        if not os.path.exists(DATASET_PATH):
            print(f"[!] Lỗi: Không tìm thấy file dữ liệu tại {DATASET_PATH}")
            print("    Hãy kiểm tra lại xem file đã được đặt đúng trong thư mục 'data/' chưa.")
            return False

        with open(DATASET_PATH, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.target_devices.append(row)
        print(f"    -> Đã tải thành công {len(self.target_devices)} thiết bị từ mạng giả lập.")
        return True

    def step_2_scan_and_infect(self):
        print("\n[+] BƯỚC 2: RÀ QUÉT & BRUTE-FORCE MẬT KHẨU MẶC ĐỊNH (MÔ PHỎNG)...")
        # Từ điển mật khẩu yếu phổ biến của mã độc Mirai
        dictionary = [("admin", "admin"), ("root", "xc3511"), ("root", "12345"), ("guest", "guest")]
        
        for device in self.target_devices:
            ip = device.get('IP_Address', 'Unknown_IP')
            device_type = device.get('Device_Type', 'Unknown_Device')
            print(f"    [*] Đang kiểm tra Port 23 (Telnet) tại {ip} [{device_type}]...")
            time.sleep(0.5) # Giả lập độ trễ mạng
            
            # Chỉ tấn công các thiết bị có trạng thái Vulnerable
            if device.get('Status') == 'Vulnerable':
                target_user = device.get('Default_Username')
                target_pass = device.get('Default_Password')
                
                # Kiểm tra xem mật khẩu có nằm trong từ điển không
                if (target_user, target_pass) in dictionary:
                    print(f"        -> [BÁO ĐỘNG] Chiếm quyền THÀNH CÔNG! Đã rà trúng mật khẩu: {target_user}:{target_pass}")
                    # Chèn thêm thời gian lây nhiễm và trạng thái mới
                    device['Infection_Time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    device['Bot_Status'] = 'Active_Zombie'
                    self.infected_bots.append(device)
                else:
                    print(f"        -> [-] Thất bại. Mật khẩu không nằm trong từ điển của Hacker.")
            else:
                print(f"        -> [V] Thiết bị an toàn. Đã chặn kết nối Telnet hoặc Đổi mật khẩu mạnh.")

    def step_3_command_and_control(self):
        print("\n[+] BƯỚC 3: THIẾT LẬP KẾT NỐI VỀ C&C SERVER...")
        time.sleep(1)
        payload = self.load_json(PAYLOAD_PATH)
        action_name = payload.get('action', 'register_to_cc_server')
        
        for bot in self.infected_bots:
            print(f"    [C&C] Đã nhận tín hiệu báo danh từ Zombie: {bot['IP_Address']}")
            print(f"          Payload mẫu nhận được: Action={action_name}")
            time.sleep(0.3)
        print(f"\n=> TỔNG KẾT: Có {len(self.infected_bots)}/{len(self.target_devices)} thiết bị đã bị biến thành Botnet.")

    def step_4_export_results(self):
        print("\n[+] BƯỚC 4: XUẤT NHẬT KÝ LÂY NHIỄM RA OUTPUT.CSV...")
        # Đảm bảo thư mục results tồn tại
        os.makedirs('results', exist_ok=True)
        
        if len(self.infected_bots) == 0:
            print("    -> Không có thiết bị nào bị nhiễm, bỏ qua bước ghi log.")
            return

        with open(OUTPUT_CSV_PATH, mode='w', encoding='utf-8', newline='') as f:
            # Lọc các trường dữ liệu cần thiết để ghi log
            fieldnames = ['IP_Address', 'Device_Type', 'Default_Username', 'Default_Password', 'Infection_Time', 'Bot_Status']
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            for bot in self.infected_bots:
                writer.writerow(bot)
                
        print(f"    -> Đã ghi file log lây nhiễm thành công tại: {OUTPUT_CSV_PATH}")
        print("\n[V] HOÀN TẤT QUÁ TRÌNH MÔ PHỎNG TẤN CÔNG AN TOÀN.")

if __name__ == "__main__":
    print("="*60)
    print(" IoT BOTNET SIMULATOR - RED TEAM DEMO SCRIPT ".center(60))
    print("="*60)
    
    simulator = BotnetSimulator()
    if simulator.step_1_load_targets():
        simulator.step_2_scan_and_infect()
        simulator.step_3_command_and_control()
        simulator.step_4_export_results()
