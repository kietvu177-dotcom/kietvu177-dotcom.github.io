[stride_analysis.md](https://github.com/user-attachments/files/30301438/stride_analysis.md)
# **PHÂN TÍCH RỦI RO BẢO MẬT THEO MÔ HÌNH STRIDE**

*Đề tài 26: Phân tích mã độc Botnet IoT & Thiết bị cấu hình kém* **Sinh viên thực hiện:** Vũ Nguyễn Anh Kiệt

Mô hình **STRIDE** (được phát triển bởi Microsoft) là phương pháp phân loại các mối đe dọa bảo mật. Dưới đây là bảng áp dụng mô hình STRIDE vào hệ thống mạng thiết bị IoT và kịch bản Botnet Mirai:

| Mối đe dọa (Threat) | Phân loại STRIDE | Mô tả lỗ hổng trong môi trường IoT | Hậu quả thực tế | Giải pháp phòng thủ / Khắc phục (Mitigation) |
| :---- | :---- | :---- | :---- | :---- |
| **S** | **Spoofing** *(Mạo danh)* | Kẻ tấn công giả mạo danh tính của máy chủ C\&C hoặc thiết bị IoT để gửi lệnh giả mạo. | Thiết bị IoT chấp nhận các gói tin không rõ nguồn gốc, tham gia vào mạng Botnet mà chủ nhân không hay biết. | Sử dụng cơ chế xác thực hai chiều (Mutual TLS / Certificate-based Authentication) giữa thiết bị và Cloud. |
| **T** | **Tampering** *(Sửa đổi dữ liệu)* | Gói dữ liệu truyền tải giữa thiết bị IoT và máy chủ không được mã hóa (Plaintext qua Telnet/HTTP). | Hacker chèn mã độc hoặc thay đổi thông số cấu hình firmware ngay trên đường truyền mạng. | Bắt buộc mã hóa toàn bộ dữ liệu qua giao thức HTTPS / TLS, chặn tuyệt đối các kết nối dạng văn bản thuần (Telnet, HTTP). |
| **R** | **Repudiation** *(Chối bỏ trách nhiệm)* | Hệ thống thiết bị IoT giá rẻ không lưu giữ nhật ký hoạt động (System Audit Logs). | Khi xảy ra tấn công DDoS từ mạng nội bộ, quản trị viên không thể truy vết thiết bị nào đã bị nhiễm mã độc. | Triển khai hệ thống ghi log tập trung (Syslog/SIEM server) để lưu trữ vết chân số (Digital Footprint) của mọi thiết bị. |
| **I** | **Information Disclosure** *(Tiết lộ thông tin)* | Sử dụng tên đăng nhập và mật khẩu mặc định mã hóa cứng (Hardcoded credentials như admin/admin, root/xc3511). | Bất kỳ ai cũng có thể dò quét và đọc được thông tin cấu hình nhạy cảm của thiết bị qua cổng mạng công khai. | Buộc người dùng thay đổi mật khẩu mặc định trong lần khởi động đầu tiên (Force Password Change). |
| **D** | **Denial of Service** *(Từ chối dịch vụ)* | Thiết bị IoT bị mã độc kiểm soát và huy động tham gia bắn lưu lượng rác (UDP/HTTP Flood) ra ngoài Internet. | Làm nghẽn băng thông đường truyền quốc tế, sập hệ thống mục tiêu và làm kiệt quệ tài nguyên phần cứng của chính thiết bị (Brick device). | Thiết lập Tường lửa / Access Control List (ACL) tại Gateway để giới hạn tốc độ (Rate Limiting) và chặn hướng Outbound của các port rác. |
| **E** | **Elevation of Privilege** *(Leo thang đặc quyền)* | Lỗ hổng dịch vụ Telnet/SSH mở công khai cho phép đăng nhập trực tiếp với quyền cao nhất (root). | Kẻ tấn công chiếm quyền kiểm soát toàn bộ hệ điều hành nhúng (Embedded OS) của Camera hoặc Router. | Vô hiệu hóa hoàn toàn các dịch vụ quản trị từ xa không cần thiết; áp dụng nguyên tắc đặc quyền tối thiểu (Least Privilege). |

## **Kết luận đánh giá**

Thông qua việc phân tích theo mô hình STRIDE, ta thấy rằng hầu hết các cuộc tấn công Botnet IoT không khai thác các lỗi phần mềm siêu việt (0-day), mà chủ yếu lợi dụng sự lỏng lẻo trong khâu **cấu hình mặc định** và **thiếu phân vùng mạng**. Do đó, các giải pháp phòng thủ cốt lõi được đề xuất trong đồ án (như chia VLAN, cấu hình Cisco ACL và Hardening thiết bị) hoàn toàn giải quyết triệt để các nguy cơ này.
