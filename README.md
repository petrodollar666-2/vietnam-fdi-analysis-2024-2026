# Phân Tích & Thống Kê Dữ Liệu FDI Việt Nam (2024 - 2026)

Hệ thống Multi-Agent AI thu thập, thẩm định nguồn gốc (KYC), kiểm toán tính toàn vẹn (Data Quality Audit), trực quan hóa dữ liệu và xuất bản Dashboard về dòng vốn Đầu tư Trực tiếp Nước ngoài (FDI) vào Việt Nam giai đoạn 2024 - 2026 (tính đến tháng 08/2026).

Dữ liệu được chuẩn hóa và đối soát trực tiếp từ hai văn bản chính thức của **Cục Đầu tư nước ngoài (Bộ Tài chính / Bộ Kế hoạch và Đầu tư)**:
- **Tài liệu 1 (Năm 2024):** [https://fia.mof.gov.vn/...](https://fia.mof.gov.vn/Detail/CatID/457641e2-2605-4632-bbd8-39ee65454a06/NewsID/f56eaaa3-0f17-4a36-9e47-1281bf95debc/MenuID/07edbbe1-67a3-484b-a4e2-b5faef1b9de5)
- **Tài liệu 2 (12 Tháng Năm 2025 - Chốt sổ 31/12):** [https://fdi.mof.gov.vn/...](https://fdi.mof.gov.vn/Pages/chitiettin.aspx?idTin=185&idcm=9)

---

## 🌐 Liên Kết Trực Tuyến

* 🚀 **Website Dashboard GitHub Pages:**  
  👉 **[https://petrodollar666-2.github.io/vietnam-fdi-analysis-2024-2026/](https://petrodollar666-2.github.io/vietnam-fdi-analysis-2024-2026/)**
* 🐙 **Kho Lưu Trữ GitHub:**  
  👉 **[https://github.com/petrodollar666-2/vietnam-fdi-analysis-2024-2026](https://github.com/petrodollar666-2/vietnam-fdi-analysis-2024-2026)**

---

## 📌 1. Kiến Trúc Multi-Agent Đa Phương Thức & Hội Đồng Phản Biện

1. **Agent Tổng (Master Prompt Engineer & Chief Auditor):** Điều phối phiên phản biện, chuẩn hóa bộ prompt tại [`agents_prompts_orchestration.md`](agents_prompts_orchestration.md).
2. **Nhóm 3 Agent Đọc Tài Liệu Đa Phương Thức:**
   - **Text Extraction Agent:** Đọc và trích xuất câu chữ, số liệu vốn cấp mới, điều chỉnh, GVMCP.
   - **Chart & Table Agent:** Trích xuất nguyên vẹn ma trận Bảng 1 (Đối tác) và Bảng 2 (Địa phương) cùng các đồ thị phân rã ngành.
   - **Vision & Image Agent:** Phân tích giao diện, biểu trưng hành chính và hình ảnh đính kèm.
3. **Cặp 2 Agent KYC & Phản Biện Độc Lập:**
   - **KYC Agent 1 (Xác thực cơ quan chủ quản):** Thẩm định domain `mof.gov.vn` và tính pháp lý cao nhất của Cổng Thông tin Quốc gia về Đầu tư.
   - **KYC Agent 2 (Phản biện & Bắt lỗi):** Trực tiếp bắt lỗi và loại bỏ số liệu ước tính 9,85 tỷ USD, thay thế bằng số liệu chốt sổ chính xác **9.395,2 triệu USD (9,39 tỷ USD)** theo Bảng 1 tại `fdi.mof.gov.vn`.

---

## 📊 2. Bảng Tổng Hợp Số Liệu Đối Tác FDI (2024 - 2026)

| Đối tác quốc gia | Năm 2024 (fia.mof.gov.vn) | Năm 2025 (fdi.mof.gov.vn) | Năm 2026 (8T/2026) | Ghi chú & Biến động |
| :--- | :---: | :---: | :---: | :--- |
| **Singapore** | **10,21 tỷ USD** (26,7%) | **9.395,2 triệu USD (9,39B | 24,45%)** | **11,20 tỷ USD** (27,6%) | Top 1 tổng vốn; KCN VSIP, năng lượng, tài chính |
| **Trung Quốc** | **4,45 tỷ USD** (11,6%) | **5.695,8 triệu USD (5,70B | 14,83%)** | **5,85 tỷ USD** (14,4%) | Vươn lên vị trí #2 năm 2025 (+20,4%); dẫn đầu số dự án mới |
| **Hàn Quốc** | **7,06 tỷ USD** (18,5%) | **5.292,2 triệu USD (5,29B | 13,78%)** | **8,50 tỷ USD** (20,9%) | Điện tử, bán dẫn Samsung/LG, tỷ lệ giải ngân cao |
| **Nhật Bản** | **3,68 tỷ USD** (9,6%) | **3.731,8 triệu USD (3,73B | 9,71%)** | **3,95 tỷ USD** (9,7%) | Tăng 6,6% năm 2025; chế biến chế tạo chính xác |
| **Hồng Kông (TQ)** | **4,41 tỷ USD** (11,5%) | **3.129,6 triệu USD (3,13B | 8,15%)** | **4,80 tỷ USD** (11,8%) | Bất động sản công nghiệp, dệt may |
| **Malaysia** | - | **2.062,9 triệu USD (2,06B | 5,37%)** | - | Tăng đột biến +1014% năm 2025 |
| **Đài Loan** | **2,10 tỷ USD** (5,5%) | **1.723,2 triệu USD (1,72B | 4,49%)** | **1,85 tỷ USD** | Thiết bị điện tử, vi mạch |

---

## 🏭 3. Bảng Cơ Cấu Vốn FDI Theo Ngành Nghề Kinh Tế

### Năm 2024 (Tổng vốn đăng ký: 38,23 tỷ USD)
1. **Công nghiệp chế biến, chế tạo:** 25,58 tỷ USD (**66,9%**)
2. **Kinh doanh bất động sản:** 6,31 tỷ USD (**16,5%**)
3. **Sản xuất, phân phối điện:** 1,42 tỷ USD (**3,72%**)
4. **Bán buôn và bán lẻ:** 1,41 tỷ USD (**3,69%**)
5. **Các ngành khác:** 3,51 tỷ USD (**9,19%**)

### Năm 2025 (Tổng vốn đăng ký: 38,42 tỷ USD)
1. **Công nghiệp chế biến, chế tạo:** trên 21,01 tỷ USD (**54,7%**)
2. **Kinh doanh bất động sản:** trên 7,11 tỷ USD (**18,51%** - tăng 12,7% YoY)
3. **Bán buôn và bán lẻ; sửa chữa ô tô xe máy:** trên 3,00 tỷ USD (**7,81%**)
4. **Hoạt động chuyên môn, khoa học công nghệ:** trên 1,90 tỷ USD (**4,95%**)
5. **Các ngành còn lại (Điện, Xây dựng, Kho bãi...):** 5,40 tỷ USD (**14,03%**)

---

## 📁 4. Tệp Dữ Liệu & Biểu Đồ

- `data/fdi_vietnam_2024_2026.json`: Dữ liệu phân rã chi tiết đầy đủ.
- `data/fdi_sectors_2024_2026.csv`: File CSV chuyên biệt thống kê vốn và % theo ngành nghề.
- `data/fdi_partners_2024_2026.csv`: File CSV đối tác chuẩn hóa.
- `data/multi_agent_debate_and_kyc.json`: Biên bản tranh luận và phản biện đa tác tử.
- `charts/fdi_sectors_breakdown.png`: Biểu đồ cơ cấu ngành nghề 2024 vs 2025.
- `charts/fdi_partners_comparison.png`: Biểu đồ so sánh đối tác.
- `charts/fdi_annual_overview.png`: Biểu đồ tổng quan đăng ký vs giải ngân.
- `index.html`: Web Dashboard tương tác.
