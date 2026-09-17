# PHÙNG XUÂN QUÝ THÀNH

**LẬP TRÌNH VIÊN BACKEND .NET · SQL SERVER**

0975 748 203 · phungxuanquythanh@gmail.com · [github.com/Xuanthanh-dzz](https://github.com/Xuanthanh-dzz) · Hà Nội

---

## Tóm tắt chuyên môn

Lập trình viên Backend .NET với gần 2,5 năm kinh nghiệm thực chiến tại UniCloud (05/2024 – Hiện tại), có thế mạnh chuyên sâu về SQL Server và xử lý logic nghiệp vụ phức tạp tại tầng dữ liệu. Trực tiếp xây dựng và tối ưu khoảng 80 Stored Procedure, thiết kế giải pháp bulk import dữ liệu lớn và chuẩn hóa cơ chế thông báo đa ngôn ngữ dùng chung toàn hệ thống. Thành thạo phát triển Web API trên nền tảng .NET theo Clean Architecture và mô hình CQRS.

---

## Kỹ năng chuyên môn

- **CƠ SỞ DỮ LIỆU:** SQL Server, T-SQL, Thiết kế CSDL, Tối ưu hóa truy vấn, Stored Procedure
- **BACKEND .NET:** C#, ASP.NET Core Web API, Clean Architecture, CQRS, Dapper, Entity Framework
- **KIẾN TRÚC & TÍCH HỢP:** RESTful API, Repository Pattern, Shared Libraries, FlexCel, Keycloak
- **QUY TRÌNH & CÔNG CỤ:** Git, GitLab, CI/CD, Database Migration, Docker, Postman, ADR

---

## Kinh nghiệm làm việc

**UniCloud — Enterprise Software & Cloud Solutions**  
*05/2024 – Hiện tại | Hà Nội*

### Project: Resident — Hệ thống Quản lý Cư dân & Đô thị thông minh
*05/2024 – Hiện tại | Hà Nội*  
**Role:** Backend .NET & SQL Developer | **Team size:** 8 thành viên  
**Tech:** C#, ASP.NET Core, SQL Server, Repository Pattern  

- Thiết kế giải pháp bulk import phương tiện: xử lý đồng thời hơn 1.000 bản ghi/lần từ file Excel, rút ngắn thời gian xử lý từ 2 phút xuống dưới 3 giây và loại bỏ 95% round-trip giữa API và Database nhờ cơ chế kiểm soát dữ liệu 2 lớp tại tầng SQL.
- Xây dựng giải pháp thông báo đa ngôn ngữ dùng chung: tự động phân giải thông điệp theo ngôn ngữ yêu cầu kèm cơ chế fallback dự phòng an toàn; được chuẩn hóa áp dụng nhất quán cho 100% Stored Procedure mới và Web API trên toàn hệ thống.
- Phát triển trọn vẹn nghiệp vụ & API quản lý phương tiện và thẻ cư dân: quy trình cấp phát, đổi thẻ, khóa/mở khóa thẻ kèm lưu vết lịch sử; tính toán biểu phí dịch vụ và hoàn phí tự động; triển khai phân quyền người dùng theo vai trò và cây chức năng.

### Project: UniHRM — Hệ thống Quản trị Nhân sự & Tiền lương
*05/2024 – Hiện tại | Hà Nội*  
**Role:** Backend .NET & SQL Developer | **Team size:** 10 thành viên  
**Tech:** C#, ASP.NET Core, SQL Server, Dapper, FlexCel  

- Tối ưu hiệu năng luồng xử lý biến động bảo hiểm xã hội: áp dụng kỹ thuật Multiple Result Sets cùng Dapper, truy xuất đồng thời toàn bộ danh mục đối chiếu và dữ liệu mẫu chỉ trong 1 truy vấn duy nhất, giảm thiểu tối đa tải mạng.
- Tự động hóa quy trình thông báo lịch phỏng vấn và tiếp nhận nhân sự: xây dựng logic lọc dữ liệu ứng viên theo đơn vị, tự động gom nhóm để kích hoạt hệ thống push notification hàng loạt.
- Phát triển module báo cáo bảo hiểm và bảng lương: tích hợp và ánh xạ dữ liệu phức tạp từ SQL Server lên API; xử lý linh hoạt cấu hình gom nhóm, các trường thông tin động và chu kỳ lương doanh nghiệp.

### Project: Bizzone & Cổng thông tin nhân sự — Enterprise HRM Portal
*05/2024 – Hiện tại | Hà Nội*  
**Role:** Backend .NET & SQL Developer | **Team size:** 12 thành viên  
**Tech:** C#, ASP.NET Core, SQL Server, FlexCel, Keycloak  

- Xây dựng hệ thống Stored Procedure báo cáo đánh giá năng lực đa chiều: xử lý ma trận tiêu chí khảo sát, tính điểm trung bình và phân vị xếp hạng theo bộ phận và toàn công ty cho hơn 5.000 nhân sự trên Web Portal.
- Tự động hóa kết xuất báo cáo doanh nghiệp bằng FlexCel: ánh xạ dữ liệu từ cơ sở dữ liệu vào biểu mẫu động, tự động hóa xuất báo cáo khảo sát định dạng Excel và PDF với độ chính xác cao.
- Đồng bộ vòng đời nhân sự và bảo trì hệ thống Core HRM: xây dựng luồng chuyển đổi tự động từ ứng viên trúng tuyển sang nhân viên chính thức; xử lý nghiệp vụ thai sản, cam kết đào tạo và bảo trì tích hợp xác thực tập trung Keycloak.

---

## Dự án cá nhân & Open Source (GitHub)

### Project: AI-Powered Cinema Platform
*[https://github.com/Xuanthanh-dzz/AI-Powered-Cinema-Platform](https://github.com/Xuanthanh-dzz/AI-Powered-Cinema-Platform)*  
**Role:** Personal Project (Owner) | **Team size:** 1 thành viên  
**Tech:** C#, .NET 10, Clean Architecture, CQRS, MediatR, FluentValidation, Docker  

- Thiết kế hệ thống theo Clean Architecture kết hợp mô hình CQRS phân tách Command và Query qua MediatR và FluentValidation.
- Chuẩn hóa quy trình kỹ thuật qua Architecture Decision Records (ADR) nhằm lưu vết các quyết định thiết kế kiến trúc hệ thống.

### Project: Full-Stack Engineering Handbook
*[https://github.com/Xuanthanh-dzz/full-stack](https://github.com/Xuanthanh-dzz/full-stack)*  
**Role:** Technical Writer & Developer | **Team size:** 1 thành viên  
**Tech:** Computer Science, C / C++, C# (.NET 10), Markdown, GitHub Pages  

- Hệ thống hóa kiến thức nền tảng khoa học máy tính và tối ưu tài nguyên: quản lý bộ nhớ C/C++, nguyên lý hướng đối tượng và kỹ thuật chuyên sâu trên nền tảng .NET.

---

## Quy trình & Đóng góp kỹ thuật khác

- **Quản lý phiên bản và đồng bộ cơ sở dữ liệu: xây dựng quy trình triển khai bằng migration scripts, bảo đảm tính nhất quán cấu trúc dữ liệu giữa các môi trường.
- **Bảo trì thư viện dùng chung: phát triển và tối ưu các module tiện ích dùng chung (xử lý chuỗi, chuẩn hóa mã phản hồi API và cấu hình tài nguyên hệ thống).

---

## Học vấn

**Trường Cao đẳng Cộng đồng Hà Tây**  
Chuyên ngành Công nghệ Thông tin · Tốt nghiệp năm 2024
