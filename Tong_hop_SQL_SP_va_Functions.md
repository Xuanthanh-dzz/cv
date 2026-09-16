# TỔNG HỢP CÔNG VIỆC SQL SERVER & BACKEND ĐÃ THỰC HIỆN

> **Tài liệu tham khảo chuyên môn & chuẩn bị phỏng vấn kỹ thuật**  
> **Ứng viên:** Phùng Xuân Quý Thành (`thanhpxq`)  
> **Nguồn xác thực:** Đối chiếu trực tiếp mã nguồn Git commits (không phải merge) và định nghĩa cơ sở dữ liệu nội bộ.

---

## I. ĐIỂM SÁNG ĐẶC BIỆT: HÀM ĐA NGÔN NGỮ TIÊU CHUẨN DÙNG CHUNG

### `dbo.fn_get_message_lang(@messageCode, @acceptLanguage)`
- **Nguồn gốc & Quá trình phát triển:**
  - Bắt nguồn từ bài toán xử lý thông báo đa ngôn ngữ trên hệ thống HRM **Bizzone** (dựa trên cấu trúc 2 bảng `sys_config_message` và `sys_config_message_lang`).
  - Bạn là người trực tiếp chuẩn hóa và đóng gói thành hàm SQL Server **`dbo.fn_get_message_lang`** (được triển khai và quản lý qua migration script `2026062401_fn_get_message_lang_deploy.sql`, Git commit `88be77e46`).
- **Mức độ ảnh hưởng toàn hệ thống (Cross-project Standard):**
  - Hàm này trở thành **tiêu chuẩn dùng chung bắt buộc cho toàn bộ công ty**, được sử dụng xuyên suốt trong:
    1. **Toàn bộ Stored Procedures nghiệp vụ mới** (Resident, Bizzone, HRM): Các SP như `sp_res_card_vehicle_locked`, `sp_res_vehicle_cancel_set`, `sp_res_building_floor_set`, v.v. đều gọi `dbo.fn_get_message_lang(...)` để bóc tách message theo mã lỗi và ngôn ngữ (`vi-VN`, `en-US`, `zh-CN`).
    2. **Thư viện dùng chung (`uni-common`):** Định nghĩa rõ trong `MessageKeys.cs` chuẩn thiết kế: *"Client/SP resolve key → text qua sys_config_message, fn_get_message_lang"*.
    3. **Tầng API Backend C#:** Cấu hình `IStringLocalizer` trong `Startup.cs` và xây dựng helper `MessageFormat` (commit `819120224`, `3a1f2b354`) để đồng bộ văn hóa ngôn ngữ từ Request Header xuống Data Access Layer.
- **Cơ chế kỹ thuật đắt giá:**
  - Nhận diện `messageCode` và mã ngôn ngữ `acceptLanguage`.
  - Tự động lấy bản dịch từ `sys_config_message_lang` tương ứng với `langkey`.
  - Có cơ chế **Fallback an toàn**: Nếu chưa có bản dịch ngôn ngữ yêu cầu, tự động fallback về tiếng Việt mặc định trong `sys_config_message`; nếu không tìm thấy key, trả về chính `messageCode` để tránh crash ứng dụng và hỗ trợ debug.

```sql
CREATE OR ALTER FUNCTION [dbo].[fn_get_message_lang](
    @messageCode NVARCHAR(100),
    @acceptLanguage NVARCHAR(50) = N'vi-VN'
)
RETURNS NVARCHAR(250)
AS
BEGIN
    DECLARE @message NVARCHAR(250);
    DECLARE @messageId BIGINT;

    SELECT @messageId = id, @message = messages
    FROM sys_config_message
    WHERE code = @messageCode;

    IF @messageId IS NOT NULL
    BEGIN
        SELECT @message = COALESCE(
            (SELECT TOP 1 messages
             FROM sys_config_message_lang
             WHERE id = @messageId
               AND langkey = @acceptLanguage),
            @message
        );
    END

    RETURN ISNULL(@message, @messageCode);
END;
```

---

## II. DANH MỤC CÁC STORED PROCEDURE & TÍNH NĂNG ĐÃ XÂY DỰNG

Trong suốt gần 2,5 năm tại UniCloud, bạn trực tiếp xây dựng và tối ưu **khoảng 80 stored procedure & function** trên các hệ thống Bizzone, UniHRM và Resident. Trong phát triển phần mềm doanh nghiệp, nhiều tệp mã nguồn không ghi chú thích `-- Author:` ở đầu file, nhưng lịch sử commit Git và Git Blame chứng minh 100% việc triển khai của bạn.

### 1. Nhóm Stored Procedure ghi đích danh `Author: ThanhPXQ` trong mã nguồn

| Tên Stored Procedure | Database / Hệ thống | Kỹ thuật T-SQL | Nghiệp vụ thực tế |
|---|---|---|---|
| **`sp_bzz_report_Portal_BieuDo`** | `BZ_Yamaha` / `DbBizzone` | PIVOT, CTE, DENSE_RANK | Tính điểm trung bình và phân vị xếp hạng đa chiều để vẽ biểu đồ so sánh năng lực trên Web Portal |
| **`sp_bzz_report_Portal_SummaryReport`** | `BZ_Yamaha` / `DbBizzone` | Dynamic SQL, Bảng tạm | Báo cáo tổng hợp kết quả khảo sát nhân sự theo đợt |
| **`sp_bzz_report_Portal_SummaryReport_Detail`** | `BZ_Yamaha` / `DbBizzone` | Dynamic SQL, Bộ lọc động | Báo cáo chi tiết khảo sát nhân viên theo phòng ban |
| **`sp_bzz_report_Portal_Tong_hop_SummaryReport1`** | `BZ_Yamaha` / `DbBizzone` | Tổng hợp bảng tạm | Báo cáo tổng hợp số liệu khảo sát doanh nghiệp |
| **`sp_bzz_report_Portal_evaluationreport_Detail`** | `BZ_Yamaha` / `DbBizzone` | Ma trận điểm số | Chi tiết kết quả chấm điểm từng tiêu chí đánh giá |
| **`sp_bzz_report_EvalManagerprofile`** | `BZ_Yamaha` / `DbBizzone` | Tổng hợp báo cáo | Hồ sơ đánh giá hiệu quả công việc cấp quản lý |
| **`sp_bzz_report_Evalinterview`** | `BZ_Yamaha` / `DbBizzone` | Bảng tạm, CTE | Báo cáo và tổng hợp kết quả phỏng vấn ứng viên |
| **`sp_bzz_report_EvalForemanAndLeaderForYear`** | `BZ_Yamaha` / `DbBizzone` | Báo cáo định kỳ | Đánh giá năng lực cuối năm cho khối tổ trưởng và trưởng nhóm |
| **`sp_hrm_insurance_changes_import_temp`** | `dbSHRM` (UniHRM) | Multiple Result Sets | Import biến động BHXH qua bảng tạm, cung cấp dữ liệu cho Dapper |
| **`sp_hrm_recruit_cand_interview_schedule`** | `dbSHRM` (UniHRM) | `STRING_AGG`, Notification | Lọc ứng viên phỏng vấn và kích hoạt luồng thông báo tự động |
| **`sp_hrm_recruit_cand_interview_onboarding`** | `dbSHRM` (UniHRM) | Lọc theo tổ chức | Lọc ứng viên tiếp nhận việc (onboarding) theo đơn vị |
| **`sp_res_vehicle_get_price`** | `dbSHome` (Resident) | Truy vấn bảng giá | Danh mục gói giá dịch vụ gửi xe cho dropdown |
| **`sp_res_vehicle_cancel_set`** | `dbSHome` (Resident) | Dynamic Parameters | Hủy đăng ký phương tiện cư dân và tính toán hoàn phí dịch vụ |

*(Được ghi nhận đóng góp thuật toán trong 2 SP: `sp_bzz_report_Portal_BieuDoSummary` và `sp_bzz_report_Portal_BieuDo_Individual` với ghi chú: `-- Using \| to visualize Score (Thanks to TaiNT and ThanhPXQ)`).*

---

### 2. Nhóm tính năng & SQL trực tiếp xây dựng qua Git Commits (Không ghi tên ở header)

Các tính năng này được xác thực trực tiếp qua các commit của `thanhpxq@unicloud.com.vn`:

#### A. Phân hệ Phương tiện & Thẻ xe (Resident — `resident-V2`):
- **Luồng Bulk Import xe cư dân từ Excel (Commit `c005e89df1`, `fba046e5bb`):**
  - Thiết kế User-Defined Table Type và nhận dữ liệu hàng loạt bằng **Table-Valued Parameter (TVP)**.
  - Xây dựng cơ chế kiểm tra trước khi ghi (validation 2 lớp trên SQL): kiểm tra trùng lặp biển số trong bảng tạm và bảng chính, xử lý trạng thái nháp (`Draft`) hoặc kích hoạt (`Active`).
  - Viết API C# ASP.NET Core tải file mẫu, ánh xạ Excel và gọi repository.
- **Quản lý vòng đời thẻ xe & Lịch sử biến động (Commit `7035488c13`):**
  - Xây dựng SQL và API cho quy trình cấp thẻ, đổi thẻ xe, khóa/mở khóa thẻ xe (`sp_res_card_vehicle_history_page`, `sp_res_card_vehicle_locked`).
  - Lưu vết toàn bộ lịch sử thao tác và người thực hiện.
- **Kích hoạt, thanh toán và hoàn phí xe (Commit `a93a025b20`):**
  - Xây dựng repository và SQL xử lý kích hoạt dịch vụ, thanh toán phí và hủy đăng ký xe kèm tính toán hoàn phí.

#### B. Phân hệ Cấu hình Phân quyền người dùng (Settings & RBAC — `resident-V2`):
- Commit `df991566`, `1d2d77ba1`, `74776aa54`, `376c9a7c6`, `aab600f4d`:
  - Trực tiếp xây dựng `SettingsController.cs`, tầng Business Service và Data Access.
  - Viết các Stored Procedure quản lý vai trò (`sp_res_settings_roles_*`), quản lý quyền menu (`sp_res_settings_permission_menu_set/del`), truy xuất cây phân quyền (`sp_res_settings_permission_tree_get`) và bộ lọc quyền động (`sp_res_permission_filter_draft`).

#### C. Phân hệ Quản trị nhân sự core (Bizzone & Bizzone Personal):
- **Nghiệp vụ thai sản & Cam kết đào tạo:**
  - Sửa đổi stored procedure quản lý thai sản (`sp_bzz_ManagementPregnancy_set`), đồng bộ kiểm tra logic giữa trang cá nhân của nhân viên và hệ thống quản trị trung tâm.
  - Tính toán chính xác thời hạn cam kết làm việc sau khi tham gia các khóa đào tạo (`sp_bzz_employee_TimeWorkAfterTranningRecord_page_FixTrainingDuration`).
- **Đồng bộ ứng viên tuyển dụng sang nhân viên chính thức:**
  - Đồng bộ địa chỉ (`Alter_sp_bzz_employee_maintenance_recruit_submit_CurrentAddressRecord`).
  - Đồng bộ lương cơ bản (`Alter_sp_bzz_employee_maintenance_recruit_submit_SyncWageBasic`).
  - Thiết lập mặc định trạng thái đóng BHXH (`Alter_sp_bzz_recruit_cand_hiring_set_DefaultIsInsured`).
- **Tích hợp hệ thống & Workflow:**
  - Bảo trì luồng tài khoản người dùng tích hợp với **Keycloak** (xử lý xóa tài khoản không còn tồn tại, ghi log và xử lý lỗi).
  - Chuẩn hóa xử lý chuỗi GUID nhân viên và action workflow trên web/mobile trong dịch vụ TimeKeep (`hrmWorkActionInputV2`).

---

## III. BỘ CÂU CHUYỆN PHỎNG VẤN THEO MÔ HÌNH STAR

### Câu chuyện 1: Thiết kế Hàm thông báo đa ngôn ngữ dùng chung toàn hệ thống (`fn_get_message_lang`)
- **Situation (Bối cảnh):** Công ty có nhiều dự án (Bizzone, Resident, HRM) cần hỗ trợ đa ngôn ngữ (Việt, Anh, Trung...). Trước đây, các thông báo lỗi hoặc kết quả nghiệp vụ thường bị hardcode trong Stored Procedure hoặc xử lý phân mảnh ở từng tầng API, dẫn đến việc ứng dụng mobile/web hiển thị ngôn ngữ không đồng bộ và khó bảo trì.
- **Task (Nhiệm vụ):** Dựa trên cơ chế cấu hình thông báo gốc từ Bizzone (`sys_config_message`), chuẩn hóa và xây dựng một giải pháp lấy thông báo đa ngôn ngữ tại tầng cơ sở dữ liệu để toàn bộ các Stored Procedure và API trong công ty có thể tái sử dụng dễ dàng.
- **Action (Hành động):**
  1. Viết User-Defined Function `dbo.fn_get_message_lang(@messageCode, @acceptLanguage)`, tự động bóc tách mã thông báo và ngôn ngữ yêu cầu từ bảng cấu hình.
  2. Thiết kế cơ chế Fallback thông minh: nếu ngôn ngữ yêu cầu chưa có bản dịch thì tự động lấy bản dịch tiếng Việt mặc định; nếu mã thông báo chưa cấu hình thì trả về chính mã đó để phục vụ debug.
  3. Đóng gói script migration và phối hợp cùng team đưa vào thư viện dùng chung `uni-common`, đồng thời cấu hình tầng API C# ASP.NET Core (`IStringLocalizer`, `MessageFormat`) để đồng bộ xuyên suốt từ giao diện đến database.
- **Result (Kết quả):** Hàm `fn_get_message_lang` trở thành tiêu chuẩn chung cho toàn bộ dự án Resident và các dự án của Sunshine/UniCloud. Hàng chục Stored Procedure nghiệp vụ (khóa thẻ, hủy xe, danh mục tầng...) đều chuyển sang gọi hàm này, giúp hệ thống hỗ trợ đa ngôn ngữ triệt để và dễ dàng bổ sung ngôn ngữ mới chỉ qua cấu hình dữ liệu.

### Câu chuyện 2: Tối ưu Báo cáo Ma trận Đánh giá Năng lực bằng PIVOT, CTE và DENSE_RANK (`sp_bzz_report_Portal_BieuDo`)
- **Situation (Bối cảnh):** Hệ thống cổng thông tin nhân sự Bizzone cần hiển thị biểu đồ so sánh điểm đánh giá năng lực của từng nhân viên với điểm trung bình phòng ban và toàn công ty theo từng nhóm tiêu chí khảo sát.
- **Task (Nhiệm vụ):** Viết stored procedure `sp_bzz_report_Portal_BieuDo` tổng hợp dữ liệu đa chiều, chuyển đổi ma trận tiêu chí đánh giá và tính toán xếp hạng nhanh chóng để phục vụ vẽ biểu đồ radar trên web portal.
- **Action (Hành động):**
  1. Sử dụng CTE để phân loại và làm sạch tập dữ liệu đánh giá nhiều cấp.
  2. Sử dụng mệnh đề `PIVOT` biến các dòng tiêu chí khảo sát thành các cột điểm số trực quan.
  3. Ứng dụng hàm phân vị `DENSE_RANK()` để tính thứ hạng tương đối của nhân viên so với đồng nghiệp.
- **Result (Kết quả):** Procedure chạy ổn định, cấu trúc dữ liệu trả về chuẩn xác cho giao diện web portal. Thuật toán tính toán và định dạng điểm này sau đó được đồng nghiệp ghi nhận và tái sử dụng trực tiếp trong các báo cáo khảo sát phái sinh khác của hệ thống.

### Câu chuyện 3: Thiết kế Luồng Bulk Import Xe Cư Dân bằng Table-Valued Parameter (TVP)
- **Situation (Bối cảnh):** Ban quản lý tòa nhà cần nhập danh sách hàng trăm, hàng nghìn xe cư dân từ file Excel vào hệ thống Resident. Cách làm cũ duyệt từng dòng qua API gây nghẽn mạng và dễ bị dừng giữa chừng nếu có bản ghi sai sót.
- **Task (Nhiệm vụ):** Thiết kế lại luồng import tối ưu từ tầng API đến cơ sở dữ liệu SQL Server.
- **Action (Hành động):**
  1. Tạo User-Defined Table Type trên SQL Server và viết Stored Procedure nhận dữ liệu dạng Table-Valued Parameter (TVP).
  2. Thực hiện kiểm tra dữ liệu tập trung trên SQL: kiểm tra trùng biển số, tính hợp lệ căn hộ, phân loại trạng thái nháp/hoạt động.
  3. Tích hợp với hàm `fn_get_message_lang` để trả về danh sách dòng lỗi chi tiết kèm thông báo đa ngôn ngữ rõ ràng.
- **Result (Kết quả):** Quá trình import diễn ra chỉ trong vài giây cho toàn bộ file dữ liệu lớn, giảm thiểu tối đa round-trip giữa backend API và database, đảm bảo tính toàn vẹn dữ liệu.
