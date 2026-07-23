Đề tài 26: Phân tích mã độc Botnet IoT & Thiết bị cấu hình kém

Học phần: Bảo mật IoT (INT570)
Sinh viên thực hiện: Vũ Nguyễn Anh Kiệt
Cảnh báo an toàn (Disclaimer): Mã nguồn trong kho lưu trữ này là Bản Mô Phỏng Cục Bộ (Local Simulation) dành riêng cho mục đích giáo dục và nghiên cứu học thuật. Tuyệt đối không chứa mã khai thác thực tế (exploits) và không rà quét/tấn công bất kỳ hệ thống mạng nào bên ngoài môi trường Localhost (127.0.0.1).

1. Giới thiệu dự án

Dự án mô phỏng vòng đời lây nhiễm của mạng máy tính ma (Botnet) nhắm vào các thiết bị IoT yếu kém (như Camera IP, Router) sử dụng mật khẩu mặc định hoặc bị lỗi cấu hình (Telnet/SSH mở công khai).
Bên cạnh việc mô phỏng quá trình lây nhiễm, dự án cung cấp các cấu hình Tường lửa (ACL) và chính sách quản trị rủi ro để cô lập mã độc, bảo vệ mạng cục bộ.

2. Kiến trúc và Luồng hoạt động của Code Demo

File src/code_demo.py thực hiện 3 luồng tác vụ chính:

Scanner & Brute-forcer: Đọc danh sách thiết bị IoT từ data/dataset_gia_lap.csv, mô phỏng việc quét Port 23 (Telnet) và dò mật khẩu.

C&C Server (Command & Control): Quản lý danh sách các thiết bị IoT đã biến thành "Zombie" thông qua data/payload_mau.json.

DDoS Simulator: Phát lệnh tấn công giả lập từ C&C Server xuống các Bot, ghi nhận trạng thái vào results/output.csv.

3. Hướng dẫn chạy Demo

Yêu cầu: Máy tính cài đặt Python 3.x.

Mở Terminal / Command Prompt.

Di chuyển vào thư mục gốc của dự án.

Chạy lệnh: python src/code_demo.py

Kiểm tra file log được sinh ra tại results/output.csv để xem danh sách các thiết bị đã bị chiếm quyền điều khiển.

4. Giải pháp phòng thủ đề xuất

Xem cấu hình Access Control List (ACL) khóa chặt Botnet tại: configs/firewall_rules.acl.
