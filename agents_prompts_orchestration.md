# HỆ THỐNG PROMPT TỐI ƯU HÓA ĐA AGENT: PHÂN TÍCH DỮ LIỆU FDI VIỆT NAM (2024 - 2026)

## 1. Vai Trò & Kiến Trúc Tổng Thể

Hệ thống phân rã bài toán thành các chuyên gia Agent phối hợp:
1. **Agent Tổng (Master Prompt Architect & Data Orchestrator):** Chuẩn hóa cấu trúc dữ liệu, tiêu chuẩn trích xuất và điều phối luồng làm việc.
2. **Data Harvester Agent 1 (FDI 2024 Specialist):** Thu thập dữ liệu toàn diện năm 2024 (diễn biến 12 tháng, cơ cấu đối tác Nhật, Trung, Hàn, Singapore...).
3. **Data Harvester Agent 2 (FDI 2025 Specialist):** Thu thập dữ liệu toàn diện năm 2025 (diễn biến 12 tháng, cơ cấu đối tác trọng điểm).
4. **Data Harvester Agent 3 (FDI 2026 Specialist):** Thu thập dữ liệu cập nhật năm 2026 (các tháng đầu năm đến mới nhất, cơ cấu đối tác).
5. **KYC & Source Verifier Agent:** Thẩm định tính chính danh, nguồn gốc, thẩm quyền cơ quan phát hành và xếp hạng Tier uy tín của nguồn dữ liệu.
6. **Data Integrity & Quality Auditor Agent:** Kiểm toán số học, tính nhất quán (vốn đăng ký vs thực hiện, lũy kế YTD vs phát sinh tháng, quy chuẩn đơn vị USD).

## 2. Đặc Tả Bộ Prompt Tối Ưu Cho Từng Agent

### 2.1. Prompt Cho 3 Agent Thu Thập Dữ Liệu (Harvesters 2024, 2025, 2026)
- **Mục tiêu:** Thu thập dữ liệu chi tiết, có cấu trúc về FDI vào Việt Nam cho từng năm cụ thể.
- **Yêu cầu dữ liệu:**
  1. Tổng vốn FDI đăng ký (Registered Capital) & Vốn FDI thực hiện/giải ngân (Disbursed Capital).
  2. Phân rã cấu phần vốn đăng ký: Cấp mới, Điều chỉnh tăng thêm, Góp vốn mua cổ phần (M&A).
  3. Phân rã theo thời gian: Diễn biến từng tháng (hoặc lũy kế các mốc tháng).
  4. Phân rã theo đối tác đầu tư trọng điểm: Singapore, Trung Quốc, Nhật Bản, Hàn Quốc, Hồng Kông...
  5. Metadata nguồn bắt buộc: Cơ quan phát hành, link báo cáo, ngày công bố, đơn vị tiền tệ.

### 2.2. Prompt Cho Agent KYC (Xác Minh Nguồn Gốc)
- **Mục tiêu:** Thẩm định tính chính thống và phân loại cấp độ uy tín (Tiering) của nguồn:
  - Tier 1: Cục Đầu tư nước ngoài (FIA / MPI), Tổng cục Thống kê (GSO), Báo Điện tử Chính phủ (baochinhphu.vn).
  - Tier 2: World Bank, ADB, CEIC, Trading Economics.
  - Tier 3: Thời báo Ngân hàng, Thời báo Tài chính Việt Nam, VietnamPlus, Lao Động, VnEconomy.
  - Cảnh báo: Blog, mạng xã hội không kiểm chứng.

### 2.3. Prompt Cho Agent Kiểm Toán Dữ Liệu (Data Auditor)
- **Mục tiêu:** Rà soát, kiểm toán chất lượng, phát hiện các điểm xung đột:
  - Phân tách rõ ràng: Vốn Đăng ký vs Vốn Thực hiện.
  - Phân tách rõ ràng: Lũy kế từ đầu năm (Cumulative YTD) vs Số phát sinh tháng (Monthly Incremental).
  - Kiểm tra tính toán số học: Tổng vốn = Cấp mới + Điều chỉnh + Góp vốn/mua cổ phần.
  - Quy đổi thống nhất đơn vị về Triệu USD / Tỷ USD.
