# PHÙNG XUÂN QUÝ THÀNH

**LẬP TRÌNH VIÊN BACKEND .NET · SQL SERVER**

0975 748 203 · phungxuanquythanh@gmail.com · [github.com/Xuanthanh-dzz](https://github.com/Xuanthanh-dzz) · Hà Nội

---

## Tóm tắt chuyên môn

Lập trình viên Backend .NET với 3 năm kinh nghiệm thực tế, bao gồm giai đoạn thực tập, tập trung vào C#/ASP.NET Core Web API, SQL Server và xử lý logic nghiệp vụ. Có kinh nghiệm với Repository Pattern, Dapper, Stored Procedure, tối ưu xử lý dữ liệu và thiết kế chi tiết API/database ở mức module. Từng tham gia bảo trì và phát triển chức năng Bizzone cho khách hàng Yamaha. Thế mạnh là các luồng nghiệp vụ sử dụng nhiều SQL, phát triển API và tối ưu hiệu năng backend.

---

## Kỹ năng chuyên môn

- **CƠ SỞ DỮ LIỆU:** SQL Server, T-SQL, Thiết kế CSDL, Tối ưu hóa truy vấn, Stored Procedure
- **BACKEND .NET:** C#, ASP.NET Core Web API, OOP, Dapper, Entity Framework
- **KIẾN TRÚC & TÍCH HỢP:** RESTful API, Repository Pattern, Shared Libraries, FlexCel, Keycloak
- **QUY TRÌNH & CÔNG CỤ:** Git, GitLab, CI/CD, Database Migration, Docker, Postman

---

## Kinh nghiệm làm việc

**UniCloud — Enterprise Software & Cloud Solutions**  
*Q4/2023 – 04/10/2026 | Hà Nội*  

**Lộ trình:** Q4/2023 – 04/2024: thực tập Backend .NET (3 tháng), sau đó thử việc → 05/2024 – 04/10/2026: Backend .NET & SQL Developer

**Dự án:** làm song song 3 dự án Resident, UniHRM và Bizzone (05/2024 – 04/10/2026).

### Project: Resident — Hệ thống Quản lý Cư dân & Đô thị thông minh
*05/2024 – 04/10/2026 | Hà Nội*  
**Role:** Backend .NET & SQL Developer | **Team size:** 8 thành viên  
**Tech:** C#, ASP.NET Core, SQL Server, Repository Pattern  

- Thiết kế giải pháp bulk import phương tiện: xử lý hơn 1.000 bản ghi/lần từ file Excel, rút ngắn thời gian xử lý từ 2 phút xuống dưới 3 giây và loại bỏ 95% round-trip giữa API và Database nhờ cơ chế kiểm soát dữ liệu 2 lớp tại tầng SQL.
- Tham gia phân tích nghiệp vụ và thiết kế chi tiết ở mức module: xác định đầu vào/đầu ra API, luồng xử lý, cấu trúc dữ liệu và Stored Procedure trước khi triển khai.
- Phát triển chức năng thêm mới, import dữ liệu và tra cứu lịch sử thẻ xe trong hệ thống quản lý cư dân.
- Phối hợp với đội Frontend để hoàn thiện luồng end-to-end: tái sử dụng component giao diện có sẵn của đội FE và điều chỉnh cho các chức năng mình phụ trách.

### Project: UniHRM — Hệ thống Quản trị Nhân sự & Tiền lương
*05/2024 – 04/10/2026 | Hà Nội*  
**Role:** Backend .NET & SQL Developer | **Team size:** 10 thành viên  
**Tech:** C#, ASP.NET Core, SQL Server, Dapper, FlexCel  

- Tối ưu hiệu năng luồng xử lý biến động bảo hiểm xã hội: áp dụng kỹ thuật Multiple Result Sets cùng Dapper, truy xuất đồng thời toàn bộ danh mục đối chiếu và dữ liệu mẫu chỉ trong 1 truy vấn duy nhất, giảm tải mạng.
- Tự động hóa quy trình thông báo lịch phỏng vấn và tiếp nhận nhân sự: xây dựng logic lọc dữ liệu ứng viên theo đơn vị, tự động gom nhóm để kích hoạt hệ thống push notification hàng loạt.
- Phát triển module báo cáo bảo hiểm và bảng lương: tích hợp và ánh xạ dữ liệu phức tạp từ SQL Server lên API; xử lý linh hoạt cấu hình gom nhóm, các trường thông tin động và chu kỳ lương doanh nghiệp.

### Project: Bizzone & Cổng thông tin nhân sự — Enterprise HRM Portal
*05/2024 – 04/10/2026 | Hà Nội*  
**Role:** Backend .NET & SQL Developer | **Team size:** 12 thành viên  
**Tech:** C#, ASP.NET Core, SQL Server, FlexCel, Keycloak  

- Tham gia bảo trì, sửa lỗi và phát triển bổ sung Bizzone cho khách hàng Yamaha; xây dựng function SQL phân giải thông báo đa ngôn ngữ dùng chung.
- Xây dựng hệ thống Stored Procedure báo cáo đánh giá năng lực đa chiều: xử lý ma trận tiêu chí khảo sát, tính điểm trung bình và phân vị xếp hạng theo bộ phận và toàn công ty cho hơn 5.000 nhân sự trên Web Portal.
- Tự động hóa kết xuất báo cáo doanh nghiệp bằng FlexCel: ánh xạ dữ liệu từ cơ sở dữ liệu vào biểu mẫu động, tự động hóa xuất báo cáo khảo sát định dạng Excel và PDF.
- Đồng bộ vòng đời nhân sự và bảo trì hệ thống Core HRM: xây dựng luồng chuyển đổi tự động từ ứng viên trúng tuyển sang nhân viên chính thức; xử lý nghiệp vụ thai sản, cam kết đào tạo và bảo trì tích hợp xác thực tập trung Keycloak.

---

## Quy trình & Đóng góp kỹ thuật khác

- **Phạm vi SQL:** xây dựng và tối ưu khoảng 80 stored procedure tại UniCloud, tập trung vào truy vấn dữ liệu và logic nghiệp vụ.
- **Quản lý phiên bản và đồng bộ cơ sở dữ liệu:** xây dựng quy trình triển khai bằng migration scripts, bảo đảm tính nhất quán cấu trúc dữ liệu giữa các môi trường.
- **Bảo trì thư viện dùng chung:** phát triển và tối ưu các module tiện ích dùng chung (xử lý chuỗi, chuẩn hóa mã phản hồi API và cấu hình tài nguyên hệ thống).

---

## Học vấn

**Trường Cao đẳng Cộng đồng Hà Tây**  
Chuyên ngành Công nghệ Thông tin · Tốt nghiệp năm 2024
